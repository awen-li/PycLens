"""RQ3 crash deduplication for CPython bytecode fuzzing results."""

from __future__ import annotations

import csv
import hashlib
import os
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import cpython_fuzz


FINDING_FIELDNAMES = [
    "finding_id",
    "python_tag",
    "version_dir",
    "kind",
    "path",
    "sha256",
    "bytes",
    "signal",
    "stack_hash",
    "stack_source",
    "status",
    "reason",
    "signature",
    "unique_bug_id",
]

UNIQUE_FIELDNAMES = [
    "unique_bug_id",
    "python_tag",
    "status",
    "signal",
    "stack_source",
    "signature",
    "findings",
    "bug_type",
    "bug_context",
    "top_frame",
    "fault_address",
    "instruction",
    "example",
    "artifact_path",
]

BUG_TYPE_FIELDNAMES = ["bug_type", "unique_bugs", "findings"]
BUG_CONTEXT_FIELDNAMES = ["bug_context", "unique_bugs", "findings"]
VALGRIND_FIELDNAMES = [
    "unique_bug_id",
    "python_tag",
    "bug_type",
    "bug_context",
    "pyc",
    "valgrind_status",
    "valgrind_category",
    "returncode",
    "error_summary",
    "detail",
]
SUMMARY_FIELDNAMES = ["metric", "value"]


@dataclass(frozen=True)
class CrashFinding:
    finding_id: str
    python_tag: str
    version_dir: str
    kind: str
    path: str
    sha256: str
    bytes: int
    signal: str
    stack_hash: str
    stack_source: str
    status: str
    reason: str
    signature: str
    unique_bug_id: str


@dataclass(frozen=True)
class UniqueBug:
    unique_bug_id: str
    python_tag: str
    status: str
    signal: str
    stack_source: str
    signature: str
    findings: int
    bug_type: str
    bug_context: str
    top_frame: str
    fault_address: str
    instruction: str
    example: str
    artifact_path: str


@dataclass(frozen=True)
class ValgrindReplay:
    unique_bug_id: str
    python_tag: str
    bug_type: str
    bug_context: str
    pyc: str
    valgrind_status: str
    valgrind_category: str
    returncode: int
    error_summary: str
    detail: str


def analyze_crashes(
    data_dir: Path,
    tags: Sequence[str],
    timeout: int,
    include_timeouts: bool = False,
) -> tuple[list[CrashFinding], list[UniqueBug]]:
    rq3_dir = data_dir / "rq3"
    harness = rq3_dir / "harness.py"
    cpython_fuzz.write_harness(harness)
    interpreters = load_rq3_interpreters(data_dir)
    if tags:
        selected_tags = sorted({cpython_fuzz.version_to_tag(tag) for tag in tags})
    else:
        selected_tags = discover_rq3_tags(rq3_dir)

    clean_unique_bug_artifacts(rq3_dir, selected_tags)

    findings: list[CrashFinding] = []
    unique_bugs: list[UniqueBug] = []

    for tag in selected_tags:
        version_name = cpython_fuzz.version_dir_name(tag)
        interpreter = valid_interpreter_for_tag(interpreters.get(tag) or default_instrumented_interpreter(rq3_dir, tag), tag)
        paths = finding_paths(rq3_dir, tag, include_timeouts=include_timeouts)
        if not paths:
            print(f"[rq3-crash] {tag}: no crash findings")
            continue
        print(f"[rq3-crash] {tag}: findings={len(paths)} interpreter={interpreter or 'missing'}")

        grouped: dict[str, list[tuple[str, Path, dict[str, str], str, int]]] = {}
        for kind, crash_path in paths:
            data = crash_path.read_bytes()
            digest = hashlib.sha256(data).hexdigest()
            metadata = parse_honggfuzz_filename(crash_path)
            group_key = initial_bug_key(kind, crash_path, metadata, digest)
            grouped.setdefault(group_key, []).append((kind, crash_path, metadata, digest, len(data)))

        print(f"[rq3-crash] {tag}: initial stack groups={len(grouped)}")
        for group_index, (group_key, rows) in enumerate(sorted(grouped.items()), start=1):
            status = "crash" if rows[0][0] == "crash" else rows[0][0]
            signal_name = rows[0][2].get("signal", "")
            stack_source = "honggfuzz-filename" if rows[0][2].get("stack_hash") else "filename"
            signature = group_key
            reason = ""
            representative = rows[0]

            if interpreter:
                for candidate in rows:
                    gdb_status, gdb_reason, gdb_signal, gdb_stack = run_under_gdb(
                        interpreter,
                        harness,
                        candidate[1],
                        timeout,
                    )
                    reason = gdb_reason
                    if gdb_stack:
                        status = gdb_status
                        signal_name = gdb_signal or signal_name
                        signature = f"{signal_name or 'SIGUNKNOWN'}:{gdb_stack}"
                        stack_source = "gdb-rerun"
                        representative = candidate
                        break
                if not reason:
                    reason = "gdb did not return output"
            else:
                reason = f"missing interpreter for {tag}"

            unique_bug_id = bug_id(tag, "stack", signature)
            artifact_path = collect_unique_bug_pyc(
                rq3_dir,
                version_name,
                unique_bug_id,
                representative[1],
            )

            group_findings: list[CrashFinding] = []
            for item_index, (kind, crash_path, metadata, digest, size) in enumerate(rows, start=1):
                row = CrashFinding(
                    finding_id=f"{tag}-{kind}-{group_index:06d}-{item_index:04d}",
                    python_tag=tag,
                    version_dir=version_name,
                    kind=kind,
                    path=str(crash_path),
                    sha256=digest,
                    bytes=size,
                    signal=signal_name or metadata.get("signal", ""),
                    stack_hash=metadata.get("stack_hash", ""),
                    stack_source=stack_source,
                    status=status,
                    reason=reason if crash_path == representative[1] else "grouped with representative rerun",
                    signature=signature,
                    unique_bug_id=unique_bug_id,
                )
                findings.append(row)
                group_findings.append(row)

            unique_bugs.append(
                make_unique_bug(
                    unique_bug_id=unique_bug_id,
                    python_tag=tag,
                    status=status,
                    signal=signal_name or rows[0][2].get("signal", ""),
                    stack_source=stack_source,
                    signature=signature,
                    findings=len(rows),
                    example=representative[1],
                    artifact_path=artifact_path,
                )
            )
            if group_index == 1 or group_index % 25 == 0 or group_index == len(grouped):
                print(
                    f"[rq3-crash {tag} group {group_index}/{len(grouped)}] "
                    f"source={stack_source} findings={len(group_findings)} unique={len(unique_bugs)}"
                )

    return findings, merge_unique_bug_rows(unique_bugs)


def merge_unique_bug_rows(rows: Sequence[UniqueBug]) -> list[UniqueBug]:
    merged: dict[str, UniqueBug] = {}
    counts: dict[str, int] = {}
    for row in rows:
        if row.unique_bug_id not in merged:
            merged[row.unique_bug_id] = row
            counts[row.unique_bug_id] = row.findings
        else:
            counts[row.unique_bug_id] += row.findings
            current = merged[row.unique_bug_id]
            if current.stack_source != "gdb-rerun" and row.stack_source == "gdb-rerun":
                merged[row.unique_bug_id] = row
    result: list[UniqueBug] = []
    for bug_id_value, row in sorted(merged.items()):
        result.append(
            UniqueBug(
                unique_bug_id=row.unique_bug_id,
                python_tag=row.python_tag,
                status=row.status,
                signal=row.signal,
                stack_source=row.stack_source,
                signature=row.signature,
                findings=counts[bug_id_value],
                bug_type=row.bug_type,
                bug_context=row.bug_context,
                top_frame=row.top_frame,
                fault_address=row.fault_address,
                instruction=row.instruction,
                example=row.example,
                artifact_path=row.artifact_path,
            )
        )
    return result


def initial_bug_key(kind: str, path: Path, metadata: dict[str, str], digest: str) -> str:
    signal_name = metadata.get("signal") or kind
    stack_hash = metadata.get("stack_hash")
    if stack_hash:
        return f"{signal_name}:{stack_hash}"
    return f"{kind}:sha256:{digest[:16]}"


def make_unique_bug(
    unique_bug_id: str,
    python_tag: str,
    status: str,
    signal: str,
    stack_source: str,
    signature: str,
    findings: int,
    example: Path,
    artifact_path: str,
) -> UniqueBug:
    metadata = parse_honggfuzz_filename(example)
    functions = signature_functions(signature)
    top_frame = first_meaningful_frame(functions)
    fault_address = metadata.get("fault_address", "")
    instruction = metadata.get("instruction", "")
    bug_type = classify_bug_type(signal, fault_address, instruction, functions)
    bug_context = classify_bug_context(functions)
    return UniqueBug(
        unique_bug_id=unique_bug_id,
        python_tag=python_tag,
        status=status,
        signal=signal,
        stack_source=stack_source,
        signature=signature,
        findings=findings,
        bug_type=bug_type,
        bug_context=bug_context,
        top_frame=top_frame,
        fault_address=fault_address,
        instruction=instruction,
        example=str(example),
        artifact_path=artifact_path,
    )


def signature_functions(signature: str) -> list[str]:
    if ":" in signature:
        signature = signature.split(":", 1)[1]
    return [part.strip() for part in signature.split("|") if part.strip()]


def first_meaningful_frame(functions: Sequence[str]) -> str:
    wrappers = {"??", "pthread_kill", "raise", "abort", "fatal_error_exit", "fatal_error"}
    for function in functions:
        if function not in wrappers:
            return function
    return functions[0] if functions else ""


def classify_bug_type(signal: str, fault_address: str, instruction: str, functions: Sequence[str]) -> str:
    signal_upper = (signal or "").upper()
    stack = "|".join(functions)
    addr = parse_int_address(fault_address)
    if "SIGABRT" in signal_upper:
        if "FatalError" in stack or "fatal_error" in stack or "_Py_FatalErrorFunc" in stack:
            return "abort_fatal_error"
        if any(token in stack for token in ("malloc", "free", "realloc", "PyMem_", "PyObject_Free")):
            return "abort_heap_allocator"
        return "abort_signal"
    if repeated_stack_frame(functions):
        return "stack_recursion_pattern"
    if "SIGSEGV" in signal_upper:
        if addr is not None and addr <= 0x1000:
            return "null_or_near_null_pointer_deref"
        if "[NOT_MMAPED]" in instruction or "NOT_MMAPED" in stack:
            return "invalid_unmapped_access"
        if any(token in stack for token in ("malloc", "free", "realloc", "PyMem_", "PyObject_Free")):
            return "heap_or_lifetime_corruption"
        return "invalid_pointer_deref"
    if "TIMEOUT" in signal_upper:
        return "timeout"
    return "unknown_abnormal_termination"


def classify_bug_context(functions: Sequence[str]) -> str:
    stack = "|".join(functions)
    if any(token in stack for token in ("marshal_loads", "r_object", "read_object", "_PyCode_New", "_PyCode_Quicken", "_Py_GetBaseOpcode")):
        return "code_object_loading"
    if any(token in stack for token in ("marshal_dumps", "_PyMarshal_WriteObjectToString", "deopt_code", "_PyCode_GetCode")):
        return "code_object_serialization"
    if any(token in stack for token in ("get_tools_for_instruction", "call_instrumentation", "_Py_call_instrumentation")):
        return "interpreter_instrumentation"
    if any(token in stack for token in ("gc_collect", "visit_decref", "traverse", "_Py_Finalize", "Py_Finalize", "dealloc", "_Py_Dealloc")):
        return "gc_or_finalization"
    if any(token in stack for token in ("PyDict", "dict_", "setitem", "PySet", "list_", "tuple", "unicode", "PyObject_", "_PyObject")):
        return "object_runtime"
    if any(token in stack for token in ("_PyEval_EvalFrameDefault", "PyEval_EvalCode", "run_eval_code_obj")):
        return "frame_evaluation"
    return "unknown_context"


def parse_int_address(value: str) -> int | None:
    if not value:
        return None
    try:
        return int(value, 16 if value.lower().startswith("0x") else 10)
    except ValueError:
        return None


def repeated_stack_frame(functions: Sequence[str]) -> bool:
    counts: dict[str, int] = {}
    for function in functions[:32]:
        if function in {"??", "_PyEval_EvalFrameDefault", "_PyEval_EvalFrame", "_PyEval_Vector"}:
            continue
        counts[function] = counts.get(function, 0) + 1
        if counts[function] >= 6:
            return True
    return False


def clean_unique_bug_artifacts(rq3_dir: Path, tags: Sequence[str]) -> None:
    for tag in sorted(set(tags)):
        out_dir = rq3_dir / cpython_fuzz.version_dir_name(tag) / "unique_bug_pyc"
        if out_dir.exists():
            shutil.rmtree(out_dir)


def collect_unique_bug_pyc(
    rq3_dir: Path,
    version_dir: str,
    unique_bug_id: str,
    example: Path,
) -> str:
    if not example.exists():
        return ""
    out_dir = rq3_dir / version_dir / "unique_bug_pyc"
    out_dir.mkdir(parents=True, exist_ok=True)
    suffix = example.suffix if example.suffix else ".pyc"
    out_path = out_dir / f"{unique_bug_id}{suffix}"
    shutil.copy2(example, out_path)
    return str(out_path)


def discover_rq3_tags(rq3_dir: Path) -> list[str]:
    tags: set[str] = set()
    if rq3_dir.exists():
        for path in rq3_dir.glob("cpython-*"):
            if path.is_dir():
                tag = cpython_fuzz.directory_name_to_tag(path.name)
                if tag:
                    tags.add(tag)
        legacy = rq3_dir / "fuzz"
        if legacy.exists():
            for path in legacy.glob("cpython-*"):
                if path.is_dir():
                    tag = cpython_fuzz.directory_name_to_tag(path.name)
                    if tag:
                        tags.add(tag)
                    else:
                        tags.add(path.name)
    return sorted(tags)


def finding_paths(rq3_dir: Path, tag: str, include_timeouts: bool) -> list[tuple[str, Path]]:
    candidates: list[tuple[str, Path]] = []
    for fuzz_dir in fuzz_dirs(rq3_dir, tag):
        crash_dir = fuzz_dir / "crashes"
        if crash_dir.exists():
            candidates.extend(("crash", path) for path in sorted(crash_dir.iterdir()) if path.is_file())
        if include_timeouts:
            timeout_dir = fuzz_dir / "timeouts"
            if timeout_dir.exists():
                candidates.extend(("timeout", path) for path in sorted(timeout_dir.iterdir()) if path.is_file())
    seen: set[Path] = set()
    unique: list[tuple[str, Path]] = []
    for kind, path in candidates:
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        unique.append((kind, path))
    return unique


def fuzz_dirs(rq3_dir: Path, tag: str) -> list[Path]:
    dirs = [
        cpython_fuzz.version_fuzz_dir(rq3_dir, tag),
        rq3_dir / "fuzz" / tag,
        rq3_dir / "fuzz" / cpython_fuzz.version_dir_name(tag),
    ]
    return [path for path in dirs if path.exists()]


def load_rq3_interpreters(data_dir: Path) -> dict[str, str]:
    interpreters: dict[str, str] = {}
    rq3_dir = data_dir / "rq3"
    csv_paths = [rq3_dir / "fuzz_runs.csv", *sorted(rq3_dir.glob("cpython-*/fuzz_runs.csv"))]
    for csv_path in csv_paths:
        if not csv_path.exists():
            continue
        with csv_path.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                tag = row.get("python_tag", "")
                interpreter = row.get("interpreter", "")
                if tag and interpreter and Path(interpreter).exists():
                    interpreters[tag] = interpreter
    return interpreters


def valid_interpreter_for_tag(interpreter: str, tag: str) -> str:
    if not interpreter:
        return ""
    expected = expected_version_tuple(tag)
    actual = interpreter_version_tuple(Path(interpreter))
    if expected and actual is None:
        print(f"[rq3-crash] {tag}: unable to verify interpreter version {interpreter}")
        return ""
    if expected and actual != expected:
        print(f"[rq3-crash] {tag}: interpreter version mismatch {interpreter} actual={actual[0]}.{actual[1]}")
        return ""
    return interpreter


def expected_version_tuple(tag: str) -> tuple[int, int] | None:
    version = cpython_fuzz.tool_analysis.cpython_tag_version(tag)
    if not version:
        return None
    parts = version.split(".")
    if len(parts) < 2:
        return None
    try:
        return int(parts[0]), int(parts[1])
    except ValueError:
        return None


def interpreter_version_tuple(interpreter: Path) -> tuple[int, int] | None:
    interpreter = interpreter.resolve()
    if not interpreter.exists():
        return None
    try:
        completed = subprocess.run(
            [str(interpreter), "-S", "-c", "import sys; print(f'{sys.version_info[0]}.{sys.version_info[1]}')"],
            cwd=str(interpreter.parent),
            env=cpython_runtime_env(interpreter),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=10,
            check=False,
            text=True,
            errors="replace",
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if completed.returncode != 0:
        return None
    match = re.match(r"^(\d+)\.(\d+)$", completed.stdout.strip())
    if not match:
        return None
    return int(match.group(1)), int(match.group(2))


def default_instrumented_interpreter(rq3_dir: Path, tag: str) -> str:
    candidates = [
        cpython_fuzz.version_build_dir(rq3_dir, tag) / "python",
        cpython_fuzz.version_build_dir(rq3_dir, tag) / "python.exe",
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return ""


def parse_honggfuzz_filename(path: Path) -> dict[str, str]:
    match = re.match(
        r"(?P<signal>SIG[^.]+)\.PC\.(?P<pc>[^.]+)\.STACK\.(?P<stack>[^.]+)"
        r"\.CODE\.(?P<code>[^.]+)\.ADDR\.(?P<addr>[^.]+)\.INSTR\.(?P<instr>.*?)(?:\.[^.]+)?$",
        path.name,
    )
    if not match:
        return {}
    return {
        "signal": match.group("signal"),
        "pc": f"0x{match.group('pc')}",
        "stack_hash": match.group("stack").lstrip("0") or match.group("stack"),
        "fault_address": f"0x{match.group('addr')}",
        "instruction": match.group("instr"),
    }


def reproduce_finding(
    interpreter: str,
    harness: Path,
    pyc_path: Path,
    timeout: int,
    metadata: dict[str, str],
) -> tuple[str, str, str, str, str]:
    gdb_status, gdb_reason, gdb_signal, gdb_stack = run_under_gdb(interpreter, harness, pyc_path, timeout)
    if gdb_stack:
        return gdb_status, gdb_reason, gdb_signal, gdb_stack, "gdb-rerun"

    status, reason = run_harness(interpreter, harness, pyc_path, timeout)
    signal_name = metadata.get("signal", "")
    stack_hash = metadata.get("stack_hash", "")
    if status == "crash" and stack_hash:
        return status, reason, signal_name, stack_hash, "honggfuzz-filename"
    return status, reason or gdb_reason, signal_name, stack_hash, "honggfuzz-filename" if stack_hash else "none"


def run_under_gdb(interpreter: str, harness: Path, pyc_path: Path, timeout: int) -> tuple[str, str, str, str]:
    if not shutil.which("gdb"):
        return "gdb_unavailable", "gdb not found", "", ""
    interpreter_path = Path(interpreter).resolve()
    harness_path = harness.resolve()
    pyc_path = pyc_path.resolve()
    inferior_env = cpython_runtime_env(interpreter_path)
    gdb_env = clean_gdb_env()
    cwd = str(interpreter_path.parent)
    command = [
        "gdb",
        "-q",
        "--batch",
        "-ex",
        "set pagination off",
        "-ex",
        "set confirm off",
        "-ex",
        f"set environment PYTHONHOME {inferior_env.get('PYTHONHOME', '')}",
        "-ex",
        f"set environment PYTHONPATH {inferior_env.get('PYTHONPATH', '')}",
        "-ex",
        "set environment PYTHONNOUSERSITE 1",
        "-ex",
        "run",
        "-ex",
        "bt",
        "--args",
        str(interpreter_path),
        "-S",
        str(harness_path),
        str(pyc_path),
    ]
    debug_header = rerun_debug_header(command, cwd, inferior_env)
    try:
        completed = subprocess.run(
            command,
            cwd=cwd,
            env=gdb_env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
            text=True,
            errors="replace",
        )
    except subprocess.TimeoutExpired:
        return "timeout", debug_header + f"\ngdb_timeout_after_{timeout}s", "", ""
    except OSError as exc:
        return "error", debug_header + f"\ngdb_{type(exc).__name__}:{exc}", "", ""
    output = compact(debug_header + completed.stdout, limit=30000)
    signal_name, frames = parse_gdb_stack(output)
    if frames:
        return "crash", output, signal_name, stack_signature(frames)
    return "not_reproduced", output, signal_name, ""


def rerun_debug_header(command: Sequence[str], cwd: str, env: dict[str, str]) -> str:
    lines = [
        "[pybcsec-rerun] command=" + " ".join(command),
        "[pybcsec-rerun] cwd=" + cwd,
        "[pybcsec-rerun] PYTHONHOME=" + env.get("PYTHONHOME", ""),
        "[pybcsec-rerun] PYTHONPATH=" + env.get("PYTHONPATH", ""),
        "[pybcsec-rerun] PYTHONNOUSERSITE=" + env.get("PYTHONNOUSERSITE", ""),
    ]
    return "\n".join(lines) + "\n"


def clean_gdb_env() -> dict[str, str]:
    env = os.environ.copy()
    env.pop("PYTHONHOME", None)
    env.pop("PYTHONPATH", None)
    env.pop("PYTHONNOUSERSITE", None)
    return env


def cpython_runtime_env(interpreter: Path) -> dict[str, str]:
    env = os.environ.copy()
    env["PYTHONNOUSERSITE"] = "1"
    version_root = interpreter.resolve().parent.parent
    source_dir = cpython_source_dir_for_version(version_root)
    paths: list[str] = []
    if source_dir:
        env["PYTHONHOME"] = str(source_dir)
        paths.append(str(source_dir / "Lib"))
    build_dir = version_root / "instrumented" / "build"
    if build_dir.exists():
        paths.extend(str(path) for path in sorted(build_dir.glob("lib.*")) if path.is_dir())
    old_path = env.get("PYTHONPATH", "")
    if old_path:
        paths.append(old_path)
    if paths:
        env["PYTHONPATH"] = os.pathsep.join(paths)
    return env


def cpython_source_dir_for_version(version_root: Path) -> Path | None:
    source_root = version_root / "source"
    if not source_root.exists():
        return None
    candidates = [path for path in sorted(source_root.glob("cpython-*")) if (path / "Lib" / "encodings").is_dir()]
    return candidates[0] if candidates else None


def parse_gdb_stack(output: str) -> tuple[str, list[str]]:
    signal_name = ""
    frames: list[str] = []
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith("Program received signal "):
            signal_name = stripped.removeprefix("Program received signal ").rstrip(".")
        if re.match(r"^#\d+\s+", stripped):
            frames.append(stripped)
    return signal_name, frames


def stack_signature(frames: Sequence[str]) -> str:
    wrapper_functions = {
        "__pthread_kill_implementation",
        "__pthread_kill_internal",
        "__GI___pthread_kill",
        "__GI_raise",
        "__GI_abort",
        "__libc_message",
        "raise",
        "abort",
    }
    normalized: list[str] = []
    for frame in frames:
        function = frame_function(frame)
        if not function:
            continue
        if function.startswith("__sanitizer_cov_trace_"):
            continue
        if function in wrapper_functions:
            continue
        normalized.append(function)
        if len(normalized) >= 16:
            break
    return "|".join(normalized)


def frame_function(frame: str) -> str:
    text = re.sub(r"^#\d+\s+", "", frame).strip()
    text = re.sub(r"^0x[0-9a-fA-F]+\s+in\s+", "", text)
    if " in " in text:
        text = text.split(" in ", 1)[1]
    text = re.sub(r"\s+at\s+[^:]+:\d+.*$", "", text)
    text = re.sub(r"\s+from\s+\S+.*$", "", text)
    text = text.split(" (", 1)[0]
    text = re.sub(r"<[^>]*>", "", text)
    return text.strip()


def run_harness(interpreter: str, harness: Path, pyc_path: Path, timeout: int) -> tuple[str, str]:
    interpreter_path = Path(interpreter).resolve()
    try:
        completed = subprocess.run(
            [str(interpreter_path), "-S", str(harness.resolve()), str(pyc_path.resolve())],
            cwd=str(interpreter_path.parent),
            env=cpython_runtime_env(interpreter_path),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
            text=True,
            errors="replace",
        )
    except subprocess.TimeoutExpired:
        return "timeout", f"timeout_after_{timeout}s"
    except OSError as exc:
        return "error", f"{type(exc).__name__}:{exc}"
    stderr = compact(completed.stderr)
    stdout = compact(completed.stdout)
    reason = stderr or stdout
    if completed.returncode == 0:
        return "ok", reason
    if completed.returncode < 0:
        return "crash", f"signal_{-completed.returncode}:{reason}"
    return f"exit_{completed.returncode}", reason


def make_signature(
    status: str,
    reason: str,
    stack_signature_value: str,
    metadata: dict[str, str],
) -> str:
    signal_name = metadata.get("signal", "")
    if stack_signature_value:
        return f"{signal_name or 'SIGUNKNOWN'}:{stack_signature_value}"
    normalized = normalize_reason(reason)
    if status == "timeout":
        return "timeout"
    if status.startswith("exit_"):
        first_line = normalized.splitlines()[0] if normalized else ""
        return f"{status}:{first_line}"
    return f"{status}:{normalized.splitlines()[0] if normalized else ''}"


def normalize_reason(text: str) -> str:
    text = compact(text)
    text = re.sub(r"0x[0-9a-fA-F]+", "0xADDR", text)
    text = re.sub(r"/[^\s:]+", "/PATH", text)
    text = re.sub(r"line \d+", "line N", text)
    text = re.sub(r"\d{4,}", "N", text)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines[-6:])


def compact(text: str, limit: int = 2000) -> str:
    text = (text or "").replace("\x00", "")
    text = "\n".join(line.rstrip() for line in text.splitlines() if line.strip())
    if len(text) > limit:
        return text[-limit:]
    return text


def bug_id(tag: str, status: str, signature: str) -> str:
    digest = hashlib.sha256(f"{tag}\0{status}\0{signature}".encode("utf-8", errors="replace")).hexdigest()[:12]
    return f"{tag}-{digest}"


def write_unique_report(path: Path, findings: Sequence[CrashFinding], unique_bugs: Sequence[UniqueBug]) -> None:
    lines = build_unique_report_lines(findings, unique_bugs, title="RQ3 Unique Bug Report")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def write_benchmark_unique_reports(rq3_dir: Path, findings: Sequence[CrashFinding], unique_bugs: Sequence[UniqueBug]) -> list[Path]:
    findings_by_tag: dict[str, list[CrashFinding]] = {}
    bugs_by_tag: dict[str, list[UniqueBug]] = {}
    for finding in findings:
        findings_by_tag.setdefault(finding.python_tag, []).append(finding)
    for bug in unique_bugs:
        bugs_by_tag.setdefault(bug.python_tag, []).append(bug)

    written: list[Path] = []
    for tag, version_bugs in sorted(bugs_by_tag.items()):
        version_dir = cpython_fuzz.version_dir_name(tag)
        out_path = rq3_dir / version_dir / "unique_bug_report.md"
        lines = build_unique_report_lines(
            findings_by_tag.get(tag, []),
            version_bugs,
            title=f"RQ3 Unique Bug Report: {version_dir}",
            include_version_summary=False,
        )
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text("\n".join(lines), encoding="utf-8")
        written.append(out_path)
    return written


def build_unique_report_lines(
    findings: Sequence[CrashFinding],
    unique_bugs: Sequence[UniqueBug],
    title: str,
    include_version_summary: bool = True,
) -> list[str]:
    findings_by_bug: dict[str, list[CrashFinding]] = {}
    for finding in findings:
        findings_by_bug.setdefault(finding.unique_bug_id, []).append(finding)

    by_version: dict[str, list[UniqueBug]] = {}
    for bug in unique_bugs:
        by_version.setdefault(bug.python_tag, []).append(bug)

    lines = [
        f"# {title}",
        "",
        "## Summary",
        "",
        f"- Crash findings: {len(findings)}",
        f"- Unique bugs: {len(unique_bugs)}",
        f"- Representative pyc artifacts: {sum(1 for bug in unique_bugs if bug.artifact_path)}",
        "",
    ]
    if include_version_summary:
        lines.extend(["## By CPython Version", ""])
        for tag in sorted(by_version):
            version_findings = sum(bug.findings for bug in by_version[tag])
            lines.append(f"- {tag}: unique_bugs={len(by_version[tag])}, findings={version_findings}")
        lines.append("")
    lines.extend(["## Unique Bugs", ""])

    for tag in sorted(by_version):
        if include_version_summary:
            lines.extend([f"### {tag}", ""])
            heading_prefix = "####"
        else:
            heading_prefix = "###"
        bugs = sorted(by_version[tag], key=lambda bug: (-bug.findings, bug.unique_bug_id))
        for index, bug in enumerate(bugs, start=1):
            examples = findings_by_bug.get(bug.unique_bug_id, [])
            representative = examples[0] if examples else None
            metadata = parse_honggfuzz_filename(Path(bug.example))
            frames = representative_stack_frames(representative)
            normalized_stack = normalized_stack_functions(frames)
            lines.extend(
                [
                    f"{heading_prefix} {index}. {bug.unique_bug_id}",
                    "",
                    f"- Status: {bug.status}",
                    f"- Signal: {bug.signal or metadata.get('signal') or 'unknown'}",
                    f"- Stack source: {bug.stack_source}",
                    f"- Stack signature: `{bug.signature}`",
                    f"- Honggfuzz stack hash: `{metadata.get('stack_hash', representative.stack_hash if representative else '') or 'unknown'}`",
                    f"- PC: `{metadata.get('pc', 'unknown')}`",
                    f"- Fault address: `{metadata.get('fault_address', 'unknown')}`",
                    f"- Instruction: `{metadata.get('instruction', 'unknown')}`",
                    f"- Findings: {bug.findings}",
                    f"- Likely failure type: `{bug.bug_type}`",
                    f"- Runtime context: `{bug.bug_context}`",
                    f"- Top frame: `{bug.top_frame or 'unknown'}`",
                    f"- Representative pyc: `{bug.artifact_path or 'missing'}`",
                    f"- Representative original: `{bug.example}`",
                ]
            )
            if frames:
                lines.append("- Normalized function stack:")
                for function in normalized_stack[:16]:
                    lines.append(f"  - `{function}`")
                lines.append("- Reproduced stack frames:")
                for frame in frames[:16]:
                    lines.append(f"  - `{frame}`")
            else:
                lines.append("- Reproduced stack frames: `not available; rerun did not produce a native backtrace`")
                command = manual_gdb_command(representative)
                if command:
                    lines.append(f"- Manual gdb command: `{command}`")
                diagnostic = rerun_diagnostic_excerpt(representative)
                if diagnostic:
                    lines.append("- Rerun diagnostic excerpt:")
                    for line in diagnostic:
                        lines.append(f"  - `{line}`")
            if examples:
                lines.append("- Example finding inputs:")
                for finding in examples[:5]:
                    lines.append(f"  - `{finding.path}`")
                if bug.findings > min(len(examples), 5):
                    lines.append(f"  - ... {bug.findings - min(len(examples), 5)} more")
            lines.append("")
    return lines


def normalized_stack_functions(frames: Sequence[str]) -> list[str]:
    functions: list[str] = []
    for frame in frames:
        function = frame_function(frame)
        if function and function not in functions:
            functions.append(function)
    return functions


def representative_stack_frames(finding: CrashFinding | None) -> list[str]:
    if finding is None or finding.stack_source != "gdb-rerun":
        return []
    _signal, frames = parse_gdb_stack(finding.reason)
    return frames


def rerun_diagnostic_excerpt(finding: CrashFinding | None, limit: int = 12) -> list[str]:
    if finding is None or not finding.reason:
        return []
    lines = [line.strip() for line in finding.reason.splitlines() if line.strip()]
    if not lines:
        return []
    return lines[-limit:]


def manual_gdb_command(finding: CrashFinding | None) -> str:
    if finding is None:
        return ""
    version_dir = cpython_fuzz.version_dir_name(finding.python_tag)
    interpreter = Path("data") / "rq3" / version_dir / "instrumented" / "python"
    source_root = Path("data") / "rq3" / version_dir / "source"
    source_dirs = [path for path in sorted(source_root.glob("cpython-*")) if (path / "Lib" / "encodings").is_dir()]
    if source_dirs:
        source = source_dirs[0]
        return f"PYTHONHOME={source} PYTHONPATH={source / 'Lib'} PYTHONNOUSERSITE=1 gdb -q --args {interpreter} -S data/rq3/harness.py {finding.path}"
    return f"PYTHONNOUSERSITE=1 gdb -q --args {interpreter} -S data/rq3/harness.py {finding.path}"


def load_unique_bugs_csv(path: Path) -> list[UniqueBug]:
    rows: list[UniqueBug] = []
    if not path.exists():
        return rows
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            example = Path(row.get("example", ""))
            if "bug_type" in row and row.get("bug_type"):
                rows.append(
                    UniqueBug(
                        unique_bug_id=row.get("unique_bug_id", ""),
                        python_tag=row.get("python_tag", ""),
                        status=row.get("status", ""),
                        signal=row.get("signal", ""),
                        stack_source=row.get("stack_source", ""),
                        signature=row.get("signature", ""),
                        findings=int(row.get("findings", "0") or 0),
                        bug_type=row.get("bug_type", ""),
                        bug_context=row.get("bug_context", ""),
                        top_frame=row.get("top_frame", ""),
                        fault_address=row.get("fault_address", ""),
                        instruction=row.get("instruction", ""),
                        example=row.get("example", ""),
                        artifact_path=row.get("artifact_path", ""),
                    )
                )
            else:
                rows.append(
                    make_unique_bug(
                        unique_bug_id=row.get("unique_bug_id", ""),
                        python_tag=row.get("python_tag", ""),
                        status=row.get("status", ""),
                        signal=row.get("signal", ""),
                        stack_source=row.get("stack_source", ""),
                        signature=row.get("signature", ""),
                        findings=int(row.get("findings", "0") or 0),
                        example=example,
                        artifact_path=row.get("artifact_path", ""),
                    )
                )
    return rows


def replay_unique_bugs_with_valgrind(
    data_dir: Path,
    tags: Sequence[str],
    timeout: int,
) -> list[ValgrindReplay]:
    rq3_dir = data_dir / "rq3"
    unique_bugs = load_unique_bugs_csv(rq3_dir / "unique_bugs.csv")
    if tags:
        selected = {cpython_fuzz.version_to_tag(tag) for tag in tags}
        unique_bugs = [bug for bug in unique_bugs if bug.python_tag in selected]
    interpreters = load_rq3_interpreters(data_dir)
    harness = rq3_dir / "harness.py"
    cpython_fuzz.write_harness(harness)
    results: list[ValgrindReplay] = []
    for tag in sorted({bug.python_tag for bug in unique_bugs}):
        version_bugs = [bug for bug in unique_bugs if bug.python_tag == tag]
        interpreter = valid_interpreter_for_tag(interpreters.get(tag) or default_instrumented_interpreter(rq3_dir, tag), tag)
        print(f"[rq3-valgrind] {tag}: unique_bugs={len(version_bugs)} interpreter={interpreter or 'missing'}")
        for index, bug in enumerate(version_bugs, start=1):
            pyc = Path(bug.artifact_path or bug.example)
            result = run_valgrind_replay(bug, interpreter, harness, pyc, timeout)
            results.append(result)
            if index == 1 or index % 25 == 0 or index == len(version_bugs):
                print(
                    f"[rq3-valgrind {tag} {index}/{len(version_bugs)}] "
                    f"status={result.valgrind_status} category={result.valgrind_category} bug={bug.unique_bug_id}"
                )
    return results


def run_valgrind_replay(
    bug: UniqueBug,
    interpreter: str,
    harness: Path,
    pyc: Path,
    timeout: int,
) -> ValgrindReplay:
    if not shutil.which("valgrind"):
        return make_valgrind_row(bug, pyc, "valgrind_unavailable", "not_run", 0, "valgrind not found", "")
    if not interpreter:
        return make_valgrind_row(bug, pyc, "missing_interpreter", "not_run", 0, f"missing interpreter for {bug.python_tag}", "")
    if not pyc.exists():
        return make_valgrind_row(bug, pyc, "missing_input", "not_run", 0, f"missing pyc {pyc}", "")
    interpreter_path = Path(interpreter).resolve()
    command = [
        "valgrind",
        "--tool=memcheck",
        "--track-origins=yes",
        "--leak-check=no",
        "--error-exitcode=99",
        str(interpreter_path),
        "-S",
        str(harness.resolve()),
        str(pyc.resolve()),
    ]
    try:
        completed = subprocess.run(
            command,
            cwd=str(interpreter_path.parent),
            env=cpython_runtime_env(interpreter_path),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
            text=True,
            errors="replace",
        )
    except subprocess.TimeoutExpired as exc:
        output = compact((exc.stdout or "") + (exc.stderr or ""), limit=12000)
        return make_valgrind_row(bug, pyc, "timeout", "timeout", 0, f"timeout_after_{timeout}s", output)
    except OSError as exc:
        return make_valgrind_row(bug, pyc, "error", "tool_error", 0, f"{type(exc).__name__}:{exc}", "")
    output = compact(completed.stdout, limit=12000)
    category = classify_valgrind_output(output, completed.returncode)
    status = "ok"
    if completed.returncode == 99 or category != "no_memcheck_error_detected":
        status = "memcheck_error"
    elif completed.returncode < 0:
        status = "crash"
    elif completed.returncode != 0:
        status = f"exit_{completed.returncode}"
    summary = valgrind_error_summary(output) or category
    return make_valgrind_row(bug, pyc, status, category, completed.returncode, summary, output)


def make_valgrind_row(
    bug: UniqueBug,
    pyc: Path,
    status: str,
    category: str,
    returncode: int,
    summary: str,
    detail: str,
) -> ValgrindReplay:
    return ValgrindReplay(
        unique_bug_id=bug.unique_bug_id,
        python_tag=bug.python_tag,
        bug_type=bug.bug_type,
        bug_context=bug.bug_context,
        pyc=str(pyc),
        valgrind_status=status,
        valgrind_category=category,
        returncode=returncode,
        error_summary=summary,
        detail=detail,
    )


def classify_valgrind_output(output: str, returncode: int) -> str:
    lowered = output.lower()
    if "stack overflow" in lowered:
        return "stack_overflow"
    if "invalid write" in lowered:
        if "after a block of size" in lowered or "inside a block of size" in lowered:
            return "heap_buffer_overflow_or_uaf_write"
        return "invalid_write"
    if "invalid read" in lowered:
        if "0 bytes inside a block of size" in lowered and "free'd" in lowered:
            return "use_after_free_read"
        if "not stack'd, malloc'd or" in lowered:
            return "invalid_pointer_read"
        return "invalid_read"
    if "jump to the invalid address" in lowered or "bad permissions for mapped region" in lowered:
        return "invalid_control_flow"
    if "use of uninitialised value" in lowered or "conditional jump or move depends on uninitialised" in lowered:
        return "uninitialized_value"
    if "invalid free" in lowered or "mismatched free" in lowered:
        return "invalid_free"
    if "error summary: 0 errors" in lowered:
        return "no_memcheck_error_detected"
    if returncode != 0:
        return "abnormal_exit_without_memcheck_category"
    return "no_memcheck_error_detected"


def valgrind_error_summary(output: str) -> str:
    for line in output.splitlines():
        stripped = line.strip()
        if "ERROR SUMMARY:" in stripped:
            return stripped
    for line in output.splitlines():
        stripped = line.strip()
        if any(token in stripped for token in ("Invalid read", "Invalid write", "Invalid free", "Use of uninitialised", "Jump to the invalid")):
            return stripped
    return ""


def write_valgrind_csv(path: Path, rows: Sequence[ValgrindReplay]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=VALGRIND_FIELDNAMES)
        writer.writeheader()
        writer.writerows(row.__dict__ for row in rows)


def write_benchmark_valgrind_csvs(rq3_dir: Path, rows: Sequence[ValgrindReplay]) -> list[Path]:
    by_version: dict[str, list[ValgrindReplay]] = {}
    for row in rows:
        version_dir = cpython_fuzz.version_dir_name(row.python_tag)
        by_version.setdefault(version_dir, []).append(row)
    written: list[Path] = []
    for version_dir, version_rows in sorted(by_version.items()):
        out_path = rq3_dir / version_dir / "valgrind_report.csv"
        write_valgrind_csv(out_path, version_rows)
        written.append(out_path)
    return written


def write_valgrind_summary_csv(path: Path, rows: Sequence[ValgrindReplay]) -> None:
    by_status: dict[str, int] = {}
    by_category: dict[str, int] = {}
    by_tag: dict[str, int] = {}
    for row in rows:
        by_status[row.valgrind_status] = by_status.get(row.valgrind_status, 0) + 1
        by_category[row.valgrind_category] = by_category.get(row.valgrind_category, 0) + 1
        by_tag[row.python_tag] = by_tag.get(row.python_tag, 0) + 1
    out_rows = [{"metric": "replayed_unique_bugs", "value": str(len(rows))}]
    out_rows.extend({"metric": f"status_{key}", "value": str(value)} for key, value in sorted(by_status.items()))
    out_rows.extend({"metric": f"category_{key}", "value": str(value)} for key, value in sorted(by_category.items()))
    out_rows.extend({"metric": f"version_{key}", "value": str(value)} for key, value in sorted(by_tag.items()))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=SUMMARY_FIELDNAMES)
        writer.writeheader()
        writer.writerows(out_rows)


def write_finding_csv(path: Path, rows: Sequence[CrashFinding]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FINDING_FIELDNAMES)
        writer.writeheader()
        writer.writerows(row.__dict__ for row in rows)


def write_unique_csv(path: Path, rows: Sequence[UniqueBug]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=UNIQUE_FIELDNAMES)
        writer.writeheader()
        writer.writerows(row.__dict__ for row in rows)


def write_bug_type_summary_csv(path: Path, rows: Sequence[UniqueBug]) -> None:
    write_grouped_bug_summary(path, rows, "bug_type", BUG_TYPE_FIELDNAMES)


def write_bug_context_summary_csv(path: Path, rows: Sequence[UniqueBug]) -> None:
    write_grouped_bug_summary(path, rows, "bug_context", BUG_CONTEXT_FIELDNAMES)


def write_grouped_bug_summary(path: Path, rows: Sequence[UniqueBug], field: str, fieldnames: Sequence[str]) -> None:
    grouped: dict[str, list[int]] = {}
    for row in rows:
        key = getattr(row, field)
        if key not in grouped:
            grouped[key] = [0, 0]
        grouped[key][0] += 1
        grouped[key][1] += row.findings
    out_rows = [
        {field: key, "unique_bugs": str(values[0]), "findings": str(values[1])}
        for key, values in sorted(grouped.items(), key=lambda item: (-item[1][0], item[0]))
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out_rows)


def write_benchmark_unique_csvs(rq3_dir: Path, rows: Sequence[UniqueBug]) -> list[Path]:
    by_version: dict[str, list[UniqueBug]] = {}
    for row in rows:
        version_dir = cpython_fuzz.version_dir_name(row.python_tag)
        by_version.setdefault(version_dir, []).append(row)

    written: list[Path] = []
    for version_dir, version_rows in sorted(by_version.items()):
        out_path = rq3_dir / version_dir / "unique_bugs.csv"
        write_unique_csv(out_path, version_rows)
        written.append(out_path)
    return written


def write_summary_csv(path: Path, findings: Sequence[CrashFinding], unique_bugs: Sequence[UniqueBug]) -> None:
    by_tag: dict[str, int] = {}
    unique_by_tag: dict[str, int] = {}
    by_status: dict[str, int] = {}
    by_stack_source: dict[str, int] = {}
    for finding in findings:
        by_tag[finding.python_tag] = by_tag.get(finding.python_tag, 0) + 1
        by_status[finding.status] = by_status.get(finding.status, 0) + 1
        by_stack_source[finding.stack_source] = by_stack_source.get(finding.stack_source, 0) + 1
    for bug in unique_bugs:
        unique_by_tag[bug.python_tag] = unique_by_tag.get(bug.python_tag, 0) + 1
    rows = [
        {"metric": "findings", "value": str(len(findings))},
        {"metric": "unique_bugs", "value": str(len(unique_bugs))},
        {"metric": "unique_bug_pyc", "value": str(sum(1 for bug in unique_bugs if bug.artifact_path))},
    ]
    rows.extend({"metric": f"findings_{tag}", "value": str(count)} for tag, count in sorted(by_tag.items()))
    rows.extend({"metric": f"unique_bugs_{tag}", "value": str(count)} for tag, count in sorted(unique_by_tag.items()))
    rows.extend({"metric": f"status_{status}", "value": str(count)} for status, count in sorted(by_status.items()))
    rows.extend({"metric": f"stack_source_{source}", "value": str(count)} for source, count in sorted(by_stack_source.items()))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=SUMMARY_FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
