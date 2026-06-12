"""RQ3 crash deduplication for CPython bytecode fuzzing results."""

from __future__ import annotations

import csv
import hashlib
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
    "example",
    "artifact_path",
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
    example: str
    artifact_path: str


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

    findings: list[CrashFinding] = []
    unique_groups: dict[tuple[str, str, str], list[CrashFinding]] = {}

    for tag in selected_tags:
        version_name = cpython_fuzz.version_dir_name(tag)
        interpreter = interpreters.get(tag) or default_instrumented_interpreter(rq3_dir, tag)
        paths = finding_paths(rq3_dir, tag, include_timeouts=include_timeouts)
        if not paths:
            print(f"[rq3-crash] {tag}: no crash findings")
            continue
        if not interpreter:
            print(f"[rq3-crash] {tag}: missing interpreter; recording findings without reproduction")
        else:
            print(f"[rq3-crash] {tag}: findings={len(paths)} interpreter={interpreter}")

        for index, (kind, crash_path) in enumerate(paths, start=1):
            data = crash_path.read_bytes()
            digest = hashlib.sha256(data).hexdigest()
            metadata = parse_honggfuzz_filename(crash_path)
            if interpreter:
                status, reason, signal_name, stack_sig, stack_source = reproduce_finding(
                    interpreter,
                    harness,
                    crash_path,
                    timeout,
                    metadata,
                )
            else:
                status = "unavailable_interpreter"
                reason = f"missing interpreter for {tag}"
                signal_name = metadata.get("signal", "")
                stack_sig = metadata.get("stack_hash", "")
                stack_source = "honggfuzz-filename" if stack_sig else "none"
            signature = make_signature(status, reason, stack_sig, metadata)
            identity_status = "stack" if stack_sig else status
            unique_bug_id = bug_id(tag, identity_status, signature)
            row = CrashFinding(
                finding_id=f"{tag}-{kind}-{index:06d}",
                python_tag=tag,
                version_dir=version_name,
                kind=kind,
                path=str(crash_path),
                sha256=digest,
                bytes=len(data),
                signal=signal_name,
                stack_hash=metadata.get("stack_hash", ""),
                stack_source=stack_source,
                status=status,
                reason=reason,
                signature=signature,
                unique_bug_id=unique_bug_id,
            )
            findings.append(row)
            unique_groups.setdefault((tag, identity_status, signature), []).append(row)
            if index == 1 or index % 100 == 0 or index == len(paths):
                print(
                    f"[rq3-crash {tag} {index}/{len(paths)}] "
                    f"status={status} stack_source={stack_source} unique={len(unique_groups)}"
                )

    unique_bugs: list[UniqueBug] = []
    for (tag, status, signature), rows in sorted(unique_groups.items()):
        unique_bug_id = bug_id(tag, status, signature)
        example = rows[0].path
        artifact_path = collect_unique_bug_pyc(
            rq3_dir,
            cpython_fuzz.version_dir_name(tag),
            unique_bug_id,
            Path(example),
        )
        unique_bugs.append(
            UniqueBug(
                unique_bug_id=unique_bug_id,
                python_tag=tag,
                status=rows[0].status,
                signal=rows[0].signal,
                stack_source=rows[0].stack_source,
                signature=signature,
                findings=len(rows),
                example=example,
                artifact_path=artifact_path,
            )
        )
    return findings, unique_bugs


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
    command = [
        "gdb",
        "-q",
        "--batch",
        "-ex",
        "set pagination off",
        "-ex",
        "set confirm off",
        "-ex",
        "run",
        "-ex",
        "bt",
        "--args",
        interpreter,
        str(harness),
        str(pyc_path),
    ]
    try:
        completed = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
            text=True,
            errors="replace",
        )
    except subprocess.TimeoutExpired:
        return "timeout", f"gdb_timeout_after_{timeout}s", "", ""
    except OSError as exc:
        return "error", f"gdb_{type(exc).__name__}:{exc}", "", ""
    output = compact(completed.stdout, limit=6000)
    signal_name, frames = parse_gdb_stack(output)
    if frames:
        return "crash", output, signal_name, stack_signature(frames)
    return "not_reproduced", output, signal_name, ""


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
    try:
        completed = subprocess.run(
            [interpreter, str(harness), str(pyc_path)],
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
    findings_by_bug: dict[str, list[CrashFinding]] = {}
    for finding in findings:
        findings_by_bug.setdefault(finding.unique_bug_id, []).append(finding)

    by_version: dict[str, list[UniqueBug]] = {}
    for bug in unique_bugs:
        by_version.setdefault(bug.python_tag, []).append(bug)

    lines = [
        "# RQ3 Unique Bug Report",
        "",
        "## Summary",
        "",
        f"- Crash findings: {len(findings)}",
        f"- Unique bugs: {len(unique_bugs)}",
        f"- Representative pyc artifacts: {sum(1 for bug in unique_bugs if bug.artifact_path)}",
        "",
        "## By CPython Version",
        "",
    ]
    for tag in sorted(by_version):
        version_findings = sum(bug.findings for bug in by_version[tag])
        lines.append(f"- {tag}: unique_bugs={len(by_version[tag])}, findings={version_findings}")
    lines.extend(["", "## Unique Bugs", ""])

    for tag in sorted(by_version):
        lines.extend([f"### {tag}", ""])
        bugs = sorted(by_version[tag], key=lambda bug: (-bug.findings, bug.unique_bug_id))
        for index, bug in enumerate(bugs, start=1):
            examples = findings_by_bug.get(bug.unique_bug_id, [])[:5]
            lines.extend(
                [
                    f"#### {index}. {bug.unique_bug_id}",
                    "",
                    f"- Status: {bug.status}",
                    f"- Signal: {bug.signal or 'unknown'}",
                    f"- Stack source: {bug.stack_source}",
                    f"- Signature: `{bug.signature}`",
                    f"- Findings: {bug.findings}",
                    f"- Representative pyc: `{bug.artifact_path or 'missing'}`",
                    f"- Representative original: `{bug.example}`",
                ]
            )
            if examples:
                lines.append("- Example finding inputs:")
                for finding in examples:
                    lines.append(f"  - `{finding.path}`")
                if bug.findings > len(examples):
                    lines.append(f"  - ... {bug.findings - len(examples)} more")
            lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


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
