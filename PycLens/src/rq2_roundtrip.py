"""RQ2 round-trip validation for decompiler-emitted source."""

from __future__ import annotations

import csv
import json
import subprocess
import tempfile
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Sequence

import scanner
import tool_analysis

FIELDNAMES = [
    "sample_sets",
    "artifact",
    "artifact_type",
    "pyc_path",
    "python_tag",
    "source_present",
    "overall_level",
    "overall_label",
    "decompiler",
    "role",
    "interpreter",
    "tool_executable",
    "status",
    "reason",
    "source_path",
    "source_bytes",
]
SUMMARY_FIELDNAMES = ["sample_set", "python_tag", "decompiler", "status", "count"]


@dataclass(frozen=True)
class RoundTripResult:
    sample_sets: str
    artifact: str
    artifact_type: str
    pyc_path: str
    python_tag: str
    source_present: str
    overall_level: str
    overall_label: str
    decompiler: str
    role: str
    interpreter: str
    tool_executable: str
    status: str
    reason: str
    source_path: str
    source_bytes: int


def validate_sample(
    sample_csv: Path,
    data_dir: Path,
    timeout: int = 600,
    workers: int = 1,
    include_secondary: bool = False,
    limit: int = 0,
) -> list[RoundTripResult]:
    rows = read_sample(sample_csv)
    if limit:
        rows = rows[:limit]
    versions_csv = data_dir / "rq1" / "rq1_versions.csv"
    interpreters = tool_analysis.load_interpreter_environment(versions_csv, data_dir=data_dir)
    tool_envs = tool_analysis.load_tool_environment(data_dir, interpreters)
    global_tools = tool_analysis.available_tools(data_dir)
    tasks = []
    for row in rows:
        for decompiler, role in selected_decompilers(row, include_secondary):
            tasks.append((row, decompiler, role))
    print(
        f"RQ2 round-trip validation: rows={len(rows)}, tasks={len(tasks)}, workers={max(1, workers)}, "
        f"include_secondary={include_secondary}",
        flush=True,
    )
    results: list[RoundTripResult] = []
    if workers <= 1:
        for index, task in enumerate(tasks, start=1):
            result = run_task(task, data_dir, interpreters, tool_envs, global_tools, timeout)
            results.append(result)
            print_progress(index, len(tasks), result)
    else:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(run_task, task, data_dir, interpreters, tool_envs, global_tools, timeout) for task in tasks]
            for index, future in enumerate(as_completed(futures), start=1):
                result = future.result()
                results.append(result)
                print_progress(index, len(tasks), result)
    return results


def read_sample(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle))


def selected_decompilers(row: dict[str, str], include_secondary: bool) -> list[tuple[str, str]]:
    primary = ""
    if row.get("overall_level") == "4" and row.get("pylingual") == "ok":
        primary = "pylingual"
    elif row.get("decompyle3") == "ok":
        primary = "decompyle3"
    elif row.get("pylingual") == "ok":
        primary = "pylingual"
    items: list[tuple[str, str]] = []
    if primary:
        items.append((primary, "primary"))
    if include_secondary:
        for tool in ("pylingual", "decompyle3"):
            if tool != primary and row.get(tool) == "ok":
                items.append((tool, "secondary"))
    return items


def run_task(
    task: tuple[dict[str, str], str, str],
    data_dir: Path,
    interpreters: dict[str, str | None],
    tool_envs: dict[str, dict[str, str | None]],
    global_tools: dict[str, str | None],
    timeout: int,
) -> RoundTripResult:
    row, decompiler, role = task
    tag = row.get("python_tag", "")
    interpreter = interpreters.get(tag) or ""
    executable = tool_executable(decompiler, tag, tool_envs, global_tools) or ""
    base = base_result(row, decompiler, role, interpreter, executable)
    if not interpreter:
        return replace_result(base, "load_fail", f"missing_interpreter:{tag}")
    if not executable:
        return replace_result(base, "no_source", f"missing_decompiler:{decompiler}")
    try:
        data = extract_pyc(row, data_dir)
    except Exception as exc:
        return replace_result(base, "load_fail", f"extract_failed:{type(exc).__name__}:{exc}")
    with tempfile.TemporaryDirectory(prefix="pyclens-rq2-roundtrip-") as tmp:
        tmp_path = Path(tmp)
        pyc_path = tmp_path / "sample.pyc"
        source_path = tmp_path / f"{decompiler}.py"
        pyc_path.write_bytes(data)
        decomp_status, decomp_reason, source = run_decompiler(decompiler, executable, pyc_path, timeout)
        if decomp_status != "ok" or not source.strip():
            reason = decomp_reason or decomp_status
            return replace_result(base, "no_source", reason, source_path="", source_bytes=len(source.encode("utf-8", "replace")))
        source_path.write_text(source, encoding="utf-8", errors="replace")
        status, reason = run_strict_compare(interpreter, pyc_path, source_path, timeout)
        return replace_result(base, status, reason, source_path=str(source_path), source_bytes=len(source.encode("utf-8", "replace")))


def base_result(row: dict[str, str], decompiler: str, role: str, interpreter: str, executable: str) -> RoundTripResult:
    return RoundTripResult(
        sample_sets=row.get("sample_sets", ""),
        artifact=row.get("artifact", ""),
        artifact_type=row.get("artifact_type", ""),
        pyc_path=row.get("pyc_path", ""),
        python_tag=row.get("python_tag", ""),
        source_present=row.get("source_present", ""),
        overall_level=row.get("overall_level", ""),
        overall_label=row.get("overall_label", ""),
        decompiler=decompiler,
        role=role,
        interpreter=interpreter,
        tool_executable=executable,
        status="not_run",
        reason="",
        source_path="",
        source_bytes=0,
    )


def replace_result(result: RoundTripResult, status: str, reason: str, source_path: str = "", source_bytes: int = 0) -> RoundTripResult:
    return RoundTripResult(**{**asdict(result), "status": status, "reason": compact(reason), "source_path": source_path, "source_bytes": source_bytes})


def tool_executable(decompiler: str, tag: str, tool_envs: dict[str, dict[str, str | None]], global_tools: dict[str, str | None]) -> str | None:
    if decompiler == "pylingual":
        return global_tools.get("pylingual")
    return tool_envs.get(tag, {}).get(decompiler)


def extract_pyc(row: dict[str, str], data_dir: Path) -> bytes:
    artifact = Path(row["artifact"])
    candidates = [artifact]
    if not artifact.is_absolute():
        candidates.append(data_dir.parent / artifact)
    artifact_path = next((path for path in candidates if path.exists()), candidates[0])
    wanted = scanner.normalize_path(row["pyc_path"])
    for entry in scanner.iter_entries(artifact_path):
        if not entry.is_dir and scanner.normalize_path(entry.path) == wanted:
            return entry.data or b""
    raise FileNotFoundError(f"{wanted} in {artifact_path}")


def run_decompiler(decompiler: str, executable: str, pyc_path: Path, timeout: int) -> tuple[str, str, str]:
    try:
        completed = subprocess.run(
            [executable, str(pyc_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
            text=True,
            errors="replace",
        )
    except subprocess.TimeoutExpired:
        return "timeout", f"timeout_after_{timeout}s", ""
    except OSError as exc:
        return "error", f"{type(exc).__name__}:{exc}", ""
    source = completed.stdout or ""
    if completed.returncode == 0:
        if decompiler == "pylingual":
            source = clean_pylingual_output(source)
        return "ok", "", source
    return f"exit_{completed.returncode}", compact(completed.stderr or completed.stdout), source


def clean_pylingual_output(text: str) -> str:
    lines = text.splitlines()
    # PyLingual success output is normally source. If a UI separator appears, keep only plausible Python lines.
    if lines and any(line.startswith("────") or line.startswith("----") for line in lines[:5]):
        lines = [line for line in lines if not line.startswith("────") and not line.startswith("----")]
    return "\n".join(lines).strip() + ("\n" if lines else "")


def run_strict_compare(interpreter: str, pyc_path: Path, source_path: Path, timeout: int) -> tuple[str, str]:
    script = STRICT_COMPARE_SCRIPT
    try:
        completed = subprocess.run(
            [interpreter, "-c", script, str(pyc_path), str(source_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
            text=True,
            errors="replace",
        )
    except subprocess.TimeoutExpired:
        return "normalize_fail", f"timeout_after_{timeout}s"
    except OSError as exc:
        return "normalize_fail", f"{type(exc).__name__}:{exc}"
    text = completed.stdout.strip()
    if completed.returncode != 0 and not text:
        return "normalize_fail", compact(completed.stderr)
    try:
        payload = json.loads(text.splitlines()[-1])
    except Exception as exc:
        return "normalize_fail", f"json_decode_failed:{type(exc).__name__}:{compact(completed.stdout or completed.stderr)}"
    return payload.get("status", "normalize_fail"), payload.get("reason", "")


STRICT_COMPARE_SCRIPT = r'''
import dis, json, marshal, sys, types
pyc_path, source_path = sys.argv[1], sys.argv[2]

def load_pyc(path):
    data = open(path, 'rb').read()
    errors = []
    for offset in (16, 12, 8):
        try:
            obj = marshal.loads(data[offset:])
        except Exception as exc:
            errors.append(f"offset{offset}:{type(exc).__name__}")
            continue
        if isinstance(obj, types.CodeType):
            return obj
        errors.append(f"offset{offset}:not_code")
    raise RuntimeError('marshal_failed:' + ','.join(errors))

def const_norm(value):
    if isinstance(value, types.CodeType):
        return normalize(value)
    if isinstance(value, (tuple, list)):
        return [const_norm(item) for item in value]
    if isinstance(value, frozenset):
        return sorted([const_norm(item) for item in value], key=repr)
    try:
        json.dumps(value)
        return value
    except Exception:
        return repr(value)

def instr_norm(code):
    out = []
    for ins in dis.get_instructions(code):
        out.append((ins.opname, repr(ins.argval)))
    return out

def normalize(code):
    return {
        'argcount': code.co_argcount,
        'posonlyargcount': getattr(code, 'co_posonlyargcount', 0),
        'kwonlyargcount': code.co_kwonlyargcount,
        'nlocals': code.co_nlocals,
        'stacksize': code.co_stacksize,
        'flags': code.co_flags,
        'names': tuple(code.co_names),
        'varnames': tuple(code.co_varnames),
        'freevars': tuple(code.co_freevars),
        'cellvars': tuple(code.co_cellvars),
        'consts': [const_norm(item) for item in code.co_consts],
        'instructions': instr_norm(code),
    }
try:
    original = load_pyc(pyc_path)
except Exception as exc:
    print(json.dumps({'status': 'load_fail', 'reason': f'{type(exc).__name__}:{exc}'}))
    raise SystemExit(0)
try:
    source = open(source_path, 'r', encoding='utf-8', errors='replace').read()
    compiled = compile(source, '<roundtrip>', 'exec')
except Exception as exc:
    print(json.dumps({'status': 'compile_fail', 'reason': f'{type(exc).__name__}:{exc}'}))
    raise SystemExit(0)
try:
    left = normalize(original)
    right = normalize(compiled)
except Exception as exc:
    print(json.dumps({'status': 'normalize_fail', 'reason': f'{type(exc).__name__}:{exc}'}))
    raise SystemExit(0)
if left == right:
    print(json.dumps({'status': 'equivalent', 'reason': ''}))
else:
    reason = 'normalized_code_object_diff'
    if left.get('instructions') != right.get('instructions'):
        reason = 'instruction_diff'
    elif left.get('consts') != right.get('consts'):
        reason = 'const_diff'
    elif left.get('names') != right.get('names'):
        reason = 'names_diff'
    elif left.get('varnames') != right.get('varnames'):
        reason = 'varnames_diff'
    print(json.dumps({'status': 'diverged', 'reason': reason}))
'''


def compact(text: str, limit: int = 300) -> str:
    value = " ".join((text or "").strip().split())
    return value if len(value) <= limit else value[: limit - 3] + "..."


def print_progress(index: int, total: int, result: RoundTripResult) -> None:
    if index == 1 or index == total or index % 25 == 0:
        print(
            f"[rq2-roundtrip {index}/{total}] {result.python_tag} {result.decompiler}/{result.role} "
            f"status={result.status} reason={result.reason} pyc={result.pyc_path}",
            flush=True,
        )


def write_csv(path: Path, rows: Sequence[RoundTripResult]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def write_summary_csv(path: Path, rows: Sequence[RoundTripResult]) -> None:
    counts: Counter[tuple[str, str, str, str]] = Counter()
    for row in rows:
        sets = row.sample_sets.split(";") if row.sample_sets else [""]
        for sample_set in sets:
            counts[(sample_set, row.python_tag, row.decompiler, row.status)] += 1
            counts[(sample_set, "ALL", row.decompiler, row.status)] += 1
            counts[("ALL", row.python_tag, row.decompiler, row.status)] += 1
            counts[("ALL", "ALL", row.decompiler, row.status)] += 1
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=SUMMARY_FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        for (sample_set, tag, decompiler, status), count in sorted(counts.items()):
            writer.writerow({"sample_set": sample_set, "python_tag": tag, "decompiler": decompiler, "status": status, "count": count})
