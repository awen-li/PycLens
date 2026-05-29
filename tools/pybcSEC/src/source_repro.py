"""RQ4 source-level reproducibility analysis for bytecode findings."""

from __future__ import annotations

import csv
import subprocess
import tempfile
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import cpython_fuzz
import tool_analysis


REPRO_FIELDNAMES = [
    "python_tag",
    "finding",
    "interpreter",
    "bytecode_status",
    "bytecode_reason",
    "decompiler",
    "decompile_status",
    "decompile_reason",
    "source_path",
    "compiled_pyc",
    "source_status",
    "source_reason",
    "reproduced",
]
SUMMARY_FIELDNAMES = ["metric", "value"]
DECOMPILERS = ("uncompyle6", "decompyle3", "pylingual")


@dataclass(frozen=True)
class ReproductionResult:
    python_tag: str
    finding: str
    interpreter: str
    bytecode_status: str
    bytecode_reason: str
    decompiler: str
    decompile_status: str
    decompile_reason: str
    source_path: str
    compiled_pyc: str
    source_status: str
    source_reason: str
    reproduced: bool


def analyze_reproducibility(
    tags: Sequence[str],
    data_dir: Path,
    timeout: int,
) -> list[ReproductionResult]:
    versions_csv = data_dir / "scan" / "cpython_versions.csv"
    interpreters = tool_analysis.load_interpreter_environment(versions_csv, data_dir=data_dir)
    for tag in tags:
        if tag not in interpreters:
            interpreters[tag] = tool_analysis.find_interpreter(tag, tool_analysis.scanner.python_tag_to_executable(tag), data_dir)
    tool_envs = tool_analysis.load_tool_environment(data_dir, interpreters)
    global_tools = tool_analysis.available_tools()
    harness = data_dir / "rq4" / "harness.py"
    cpython_fuzz.write_harness(harness)

    results: list[ReproductionResult] = []
    for tag in tags:
        findings = find_findings(data_dir, tag)
        interpreter = interpreters.get(tag)
        if not findings:
            print(f"[rq4] {tag}: no findings")
            continue
        if not interpreter:
            print(f"[rq4] {tag}: missing interpreter")
            for finding in findings:
                results.append(
                    ReproductionResult(
                        python_tag=tag,
                        finding=str(finding),
                        interpreter="",
                        bytecode_status="unavailable_interpreter",
                        bytecode_reason=f"missing interpreter for {tag}",
                        decompiler="",
                        decompile_status="not_run",
                        decompile_reason="",
                        source_path="",
                        compiled_pyc="",
                        source_status="not_run",
                        source_reason="",
                        reproduced=False,
                    )
                )
            continue

        decompilers = tools_for_tag(tag, global_tools, tool_envs)
        print(f"[rq4] {tag}: findings={len(findings)}")
        for index, finding in enumerate(findings, start=1):
            bytecode_status, bytecode_reason = run_harness(interpreter, harness, finding, timeout)
            finding_results = reproduce_finding(
                tag,
                interpreter,
                finding,
                bytecode_status,
                bytecode_reason,
                decompilers,
                data_dir,
                harness,
                timeout,
            )
            results.extend(finding_results)
            reproduced = any(item.reproduced for item in finding_results)
            print(f"[rq4 {tag} {index}/{len(findings)}] bytecode={bytecode_status} reproduced={reproduced} finding={finding.name}")
    return results


def find_findings(data_dir: Path, tag: str) -> list[Path]:
    findings_dir = data_dir / "rq3" / "fuzz" / tag / "findings"
    if not findings_dir.exists():
        return []
    return sorted(item for item in findings_dir.iterdir() if item.is_file())


def tools_for_tag(
    tag: str,
    global_tools: dict[str, str | None],
    tool_envs: dict[str, dict[str, str | None]],
) -> dict[str, str | None]:
    tools = {tool: global_tools.get(tool) for tool in DECOMPILERS}
    for tool, executable in tool_envs.get(tag, {}).items():
        if tool in tools and executable:
            tools[tool] = executable
    return tools


def reproduce_finding(
    tag: str,
    interpreter: str,
    finding: Path,
    bytecode_status: str,
    bytecode_reason: str,
    decompilers: dict[str, str | None],
    data_dir: Path,
    harness: Path,
    timeout: int,
) -> list[ReproductionResult]:
    rows: list[ReproductionResult] = []
    out_dir = data_dir / "rq4" / "source_candidates" / tag / finding.stem
    out_dir.mkdir(parents=True, exist_ok=True)
    available = [(name, path) for name, path in decompilers.items() if path]
    if not available:
        return [
            ReproductionResult(
                python_tag=tag,
                finding=str(finding),
                interpreter=interpreter,
                bytecode_status=bytecode_status,
                bytecode_reason=bytecode_reason,
                decompiler="",
                decompile_status="unavailable",
                decompile_reason="no decompiler available",
                source_path="",
                compiled_pyc="",
                source_status="not_run",
                source_reason="",
                reproduced=False,
            )
        ]

    for decompiler, executable in available:
        source_path = out_dir / f"{decompiler}.py"
        compiled_pyc = out_dir / f"{decompiler}.pyc"
        decompile_status, decompile_reason = run_decompiler(decompiler, executable, finding, source_path, timeout)
        source_status = "not_run"
        source_reason = ""
        reproduced = False
        if decompile_status == "ok":
            compile_status, compile_reason = compile_source_to_pyc(interpreter, source_path, compiled_pyc, timeout)
            if compile_status == "ok":
                source_status, source_reason = run_harness(interpreter, harness, compiled_pyc, timeout)
                reproduced = same_behavior(bytecode_status, source_status)
            else:
                source_status = compile_status
                source_reason = compile_reason
        rows.append(
            ReproductionResult(
                python_tag=tag,
                finding=str(finding),
                interpreter=interpreter,
                bytecode_status=bytecode_status,
                bytecode_reason=bytecode_reason,
                decompiler=decompiler,
                decompile_status=decompile_status,
                decompile_reason=decompile_reason,
                source_path=str(source_path) if source_path.exists() else "",
                compiled_pyc=str(compiled_pyc) if compiled_pyc.exists() else "",
                source_status=source_status,
                source_reason=source_reason,
                reproduced=reproduced,
            )
        )
    return rows


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
    if completed.returncode == 0:
        return "ok", ""
    if completed.returncode < 0:
        return "crash", f"signal_{-completed.returncode}:{compact_reason(completed.stderr)}"
    return f"exit_{completed.returncode}", compact_reason(completed.stderr) or compact_reason(completed.stdout)


def run_decompiler(
    tool: str,
    executable: str,
    pyc_path: Path,
    source_path: Path,
    timeout: int,
) -> tuple[str, str]:
    if tool == "pylingual":
        command = [executable, str(pyc_path)]
    else:
        command = [executable, str(pyc_path)]
    try:
        completed = subprocess.run(
            command,
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
    text = completed.stdout
    if completed.returncode != 0:
        return f"exit_{completed.returncode}", compact_reason(completed.stderr) or compact_reason(text)
    if not looks_like_python_source(text):
        return "error", "no source emitted"
    source_path.write_text(sanitize_decompiler_output(text), encoding="utf-8")
    return "ok", ""


def looks_like_python_source(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    bad_prefixes = ("Usage:", "usage:", "Traceback", "Error:", "ERROR:")
    return not stripped.startswith(bad_prefixes)


def sanitize_decompiler_output(text: str) -> str:
    lines = []
    for line in text.splitlines():
        if line.startswith("# uncompyle6") or line.startswith("# decompyle3"):
            lines.append(line)
            continue
        lines.append(line)
    return "\n".join(lines).rstrip() + "\n"


def compile_source_to_pyc(interpreter: str, source_path: Path, pyc_path: Path, timeout: int) -> tuple[str, str]:
    script = textwrap.dedent(
        """\
        import importlib.util
        import marshal
        import py_compile
        import struct
        import sys
        from pathlib import Path

        source = Path(sys.argv[1])
        out = Path(sys.argv[2])
        code = compile(source.read_text(encoding="utf-8"), str(source), "exec")
        with out.open("wb") as handle:
            handle.write(importlib.util.MAGIC_NUMBER)
            handle.write(struct.pack("<I", 0))
            handle.write(struct.pack("<I", 0))
            handle.write(struct.pack("<I", 0))
            marshal.dump(code, handle)
        """
    )
    try:
        completed = subprocess.run(
            [interpreter, "-c", script, str(source_path), str(pyc_path)],
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
    if completed.returncode == 0:
        return "ok", ""
    return f"exit_{completed.returncode}", compact_reason(completed.stderr) or compact_reason(completed.stdout)


def same_behavior(bytecode_status: str, source_status: str) -> bool:
    return behavior_class(bytecode_status) == behavior_class(source_status)


def behavior_class(status: str) -> str:
    if status == "crash":
        return "crash"
    if status == "timeout":
        return "timeout"
    if status.startswith("exit_"):
        return "exception"
    if status == "ok":
        return "ok"
    return status


def write_csv(path: Path, rows: Sequence[ReproductionResult]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=REPRO_FIELDNAMES)
        writer.writeheader()
        writer.writerows(row.__dict__ for row in rows)


def write_summary_csv(path: Path, rows: Sequence[ReproductionResult]) -> None:
    findings = {row.finding for row in rows}
    reproduced_findings = {row.finding for row in rows if row.reproduced}
    tool_not_reproduced_findings = findings - reproduced_findings
    summary = [
        {"metric": "findings", "value": str(len(findings))},
        {"metric": "rows", "value": str(len(rows))},
        {"metric": "tool_reproduced_findings", "value": str(len(reproduced_findings))},
        {"metric": "not_reproduced_by_selected_tools", "value": str(len(tool_not_reproduced_findings))},
        {"metric": "decompile_ok_rows", "value": str(sum(1 for row in rows if row.decompile_status == "ok"))},
        {"metric": "source_compile_ok_rows", "value": str(sum(1 for row in rows if row.source_status in {"ok", "crash", "timeout"} or row.source_status.startswith("exit_")))},
    ]
    for tool in sorted({row.decompiler for row in rows if row.decompiler}):
        tool_rows = [row for row in rows if row.decompiler == tool]
        summary.append({"metric": f"{tool}_rows", "value": str(len(tool_rows))})
        summary.append({"metric": f"{tool}_decompile_ok", "value": str(sum(1 for row in tool_rows if row.decompile_status == "ok"))})
        summary.append({"metric": f"{tool}_reproduced", "value": str(sum(1 for row in tool_rows if row.reproduced))})
    for tag in sorted({row.python_tag for row in rows}):
        tag_findings = {row.finding for row in rows if row.python_tag == tag}
        tag_reproduced = {row.finding for row in rows if row.python_tag == tag and row.reproduced}
        summary.append({"metric": f"{tag}_findings", "value": str(len(tag_findings))})
        summary.append({"metric": f"{tag}_reproduced", "value": str(len(tag_reproduced))})
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=SUMMARY_FIELDNAMES)
        writer.writeheader()
        writer.writerows(summary)


def compact_reason(text: str, limit: int = 240) -> str:
    compact = " ".join((text or "").split())
    if len(compact) > limit:
        return compact[: limit - 3] + "..."
    return compact
