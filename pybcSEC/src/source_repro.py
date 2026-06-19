"""RQ4 source-level reproducibility analysis for bytecode findings."""

from __future__ import annotations

import csv
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
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
FINDING_FIELDNAMES = [
    "python_tag",
    "finding",
    "category",
    "reason",
    "bytecode_status",
    "bytecode_reason",
    "reproduced_by",
    "decompiler_statuses",
    "source_statuses",
]
TOOL_FAILURE_FIELDNAMES = [
    "python_tag",
    "finding",
    "decompiler",
    "stage",
    "status",
    "failure_class",
    "reason",
    "bytecode_status",
    "source_path",
    "compiled_pyc",
]
DECOMPILERS = ("decompyle3", "pylingual")
CSV_WRITE_KWARGS = {
    "quoting": csv.QUOTE_MINIMAL,
    "escapechar": "\\",
    "lineterminator": "\n",
}


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
    workers: int = 1,
) -> list[ReproductionResult]:
    versions_csv = data_dir / "scan" / "cpython_versions.csv"
    interpreters = tool_analysis.load_interpreter_environment(versions_csv, data_dir=data_dir)
    for tag in tags:
        if tag not in interpreters:
            interpreters[tag] = tool_analysis.find_interpreter(tag, tool_analysis.scanner.python_tag_to_executable(tag), data_dir)
    tool_envs = tool_analysis.load_tool_environment(data_dir, interpreters)
    global_tools = tool_analysis.available_tools(data_dir)
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
        print(f"[rq4] {tag}: findings={len(findings)}, workers={max(1, workers)}")
        if workers <= 1:
            for index, finding in enumerate(findings, start=1):
                finding_results = analyze_finding(
                    tag,
                    interpreter,
                    finding,
                    decompilers,
                    data_dir,
                    harness,
                    timeout,
                )
                results.extend(finding_results)
                print_progress(tag, index, len(findings), finding, finding_results)
        else:
            with ThreadPoolExecutor(max_workers=workers) as executor:
                futures = [
                    executor.submit(
                        analyze_finding,
                        tag,
                        interpreter,
                        finding,
                        decompilers,
                        data_dir,
                        harness,
                        timeout,
                    )
                    for finding in findings
                ]
                for index, future in enumerate(as_completed(futures), start=1):
                    finding_results = future.result()
                    results.extend(finding_results)
                    finding = Path(finding_results[0].finding) if finding_results else Path("<unknown>")
                    print_progress(tag, index, len(findings), finding, finding_results)
    return results


def analyze_finding(
    tag: str,
    interpreter: str,
    finding: Path,
    decompilers: dict[str, str | None],
    data_dir: Path,
    harness: Path,
    timeout: int,
) -> list[ReproductionResult]:
    bytecode_status, bytecode_reason = run_harness(interpreter, harness, finding, timeout)
    return reproduce_finding(
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


def print_progress(tag: str, index: int, total: int, finding: Path, rows: Sequence[ReproductionResult]) -> None:
    bytecode_status = rows[0].bytecode_status if rows else "unknown"
    reproduced = any(item.reproduced for item in rows)
    failures = sum(1 for item in rows if tool_failure(item)[0])
    print(
        f"[rq4 {tag} {index}/{total}] bytecode={bytecode_status} reproduced={reproduced} "
        f"tool_failures={failures} finding={finding.name}",
        flush=True,
    )


def find_findings(data_dir: Path, tag: str) -> list[Path]:
    """Return deduplicated RQ3 finding representatives for source reproduction."""
    version_dir = cpython_fuzz.version_dir(data_dir / "rq3", tag)
    candidate_dirs = [
        version_dir / "unique_bug_pyc",
        cpython_fuzz.version_fuzz_dir(data_dir / "rq3", tag) / "crashes",
        data_dir / "rq3" / "fuzz" / tag / "crashes",
        data_dir / "rq3" / "fuzz" / tag / "findings",
    ]
    for findings_dir in candidate_dirs:
        if findings_dir.exists():
            return sorted(item for item in findings_dir.iterdir() if item.is_file() and item.suffix == ".pyc")
    return []


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
        return "error", compact_reason(text) or compact_reason(completed.stderr) or "no source emitted"
    source_path.write_text(sanitize_decompiler_output(text), encoding="utf-8")
    return "ok", ""


def looks_like_python_source(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    bad_prefixes = ("Usage:", "usage:", "Traceback", "Error:", "ERROR:")
    bad_fragments = (
        "Unsupported Python version",
        "Unknown magic number",
        "Unknown type",
        "ModuleNotFoundError",
        "ImportError",
        "SyntaxError:",
        "Fatal Python error",
        "Cannot decompile",
        "Failed to decompile",
        "failed to decompile",
        "Traceback (most recent call last)",
        "The University of Texas at Dallas",
        "pylingual.io",
        "decompiler.py:",
        "main.py:",
        "INFO     Loading",
        "ERROR    Failed",
        "no source emitted",
    )
    if stripped.startswith(bad_prefixes):
        return False
    first_line = stripped.splitlines()[0].strip()
    if first_line.startswith(("─", "╭", "│", "╰", "â”", "â•")):
        return False
    if "â”" in stripped or "â•" in stripped:
        return False
    return not any(fragment in stripped for fragment in bad_fragments)


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
        writer = csv.DictWriter(handle, fieldnames=REPRO_FIELDNAMES, **CSV_WRITE_KWARGS)
        writer.writeheader()
        writer.writerows(sanitize_csv_row(row.__dict__) for row in rows)


def write_finding_report_csv(path: Path, rows: Sequence[ReproductionResult]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FINDING_FIELDNAMES, **CSV_WRITE_KWARGS)
        writer.writeheader()
        writer.writerows(sanitize_csv_row(row) for row in finding_report_rows(rows))


def finding_report_rows(rows: Sequence[ReproductionResult]) -> list[dict[str, str]]:
    by_finding: dict[str, list[ReproductionResult]] = {}
    for row in rows:
        by_finding.setdefault(row.finding, []).append(row)
    report = []
    for finding, items in sorted(by_finding.items()):
        category = classify_finding(items)
        report.append(
            {
                "python_tag": items[0].python_tag,
                "finding": finding,
                "category": category,
                "reason": failure_reason(category, items),
                "bytecode_status": items[0].bytecode_status,
                "bytecode_reason": items[0].bytecode_reason,
                "reproduced_by": ";".join(sorted({row.decompiler for row in items if row.reproduced})),
                "decompiler_statuses": ";".join(
                    f"{row.decompiler or 'none'}:{row.decompile_status}:{row.decompile_reason}" for row in items
                ),
                "source_statuses": ";".join(
                    f"{row.decompiler or 'none'}:{row.source_status}:{row.source_reason}" for row in items
                ),
            }
        )
    return report


def write_tool_failure_csv(path: Path, rows: Sequence[ReproductionResult]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=TOOL_FAILURE_FIELDNAMES, **CSV_WRITE_KWARGS)
        writer.writeheader()
        writer.writerows(sanitize_csv_row(row) for row in tool_failure_rows(rows))


def tool_failure_rows(rows: Sequence[ReproductionResult]) -> list[dict[str, str]]:
    failures: list[dict[str, str]] = []
    for row in rows:
        stage, status, reason = tool_failure(row)
        if not stage:
            continue
        failures.append(
            {
                "python_tag": row.python_tag,
                "finding": row.finding,
                "decompiler": row.decompiler or "none",
                "stage": stage,
                "status": status,
                "failure_class": classify_tool_failure(row, stage, status, reason),
                "reason": reason,
                "bytecode_status": row.bytecode_status,
                "source_path": row.source_path,
                "compiled_pyc": row.compiled_pyc,
            }
        )
    return failures


def tool_failure(row: ReproductionResult) -> tuple[str, str, str]:
    if row.decompile_status not in {"ok", "not_run"}:
        return "decompile", row.decompile_status, row.decompile_reason
    if row.decompile_status == "ok" and row.source_status not in {"ok", "crash", "timeout"} and not row.source_status.startswith("exit_"):
        return "compile", row.source_status, row.source_reason
    if row.decompile_status == "ok" and is_executed_source_status(row.source_status) and not row.reproduced:
        return "rerun", row.source_status, row.source_reason or "behavior diverged from original bytecode"
    return "", "", ""


def classify_tool_failure(row: ReproductionResult, stage: str, status: str, reason: str) -> str:
    reason_text = (reason or "").lower()
    if status == "timeout" or status == "crash" or status.startswith("signal_"):
        return "tool_robustness_failure"
    if "segmentation fault" in reason_text or "core dumped" in reason_text:
        return "tool_robustness_failure"
    if "traceback" in reason_text and not is_expected_rejection_reason(reason):
        return "tool_robustness_failure"
    if status in {"unavailable", "not_run"} or "missing interpreter" in reason_text or "no decompiler available" in reason_text:
        return "environment_failure"
    if stage == "decompile" and is_expected_rejection_reason(reason):
        return "expected_rejection"
    if stage in {"compile", "rerun"}:
        return "translation_failure"
    return "expected_rejection"


def is_expected_rejection_reason(reason: str) -> bool:
    text = (reason or "").lower()
    expected_fragments = (
        "syntaxerror",
        "bad marshal data",
        "unknown magic number",
        "unsupported python version",
        "unsupported bytecode",
        "unknown type",
        "invalid",
        "cannot decompile",
        "no source emitted",
    )
    return any(fragment in text for fragment in expected_fragments)


def failure_reason(category: str, rows: Sequence[ReproductionResult]) -> str:
    if category == "source_reproduced":
        tools = sorted({row.decompiler for row in rows if row.reproduced})
        return "reproduced by " + ";".join(tools)
    if category == "unavailable_interpreter":
        return first_nonempty(row.bytecode_reason for row in rows) or "missing interpreter"
    if category == "unconfirmed":
        status = rows[0].bytecode_status if rows else "unknown"
        reason = rows[0].bytecode_reason if rows else ""
        return compact_reason(f"original bytecode status {status}: {reason}")
    if category == "no_source":
        return first_nonempty(row.decompile_reason for row in rows) or "no selected decompiler emitted source"
    if category == "compile_failure":
        return first_nonempty(row.source_reason for row in rows if row.decompile_status == "ok") or "recovered source did not compile"
    if category == "behavior_divergence":
        statuses = sorted({row.source_status for row in rows if row.decompile_status == "ok"})
        return "source-derived bytecode behavior diverged: " + ";".join(statuses)
    return "not reproduced by selected tools"


def first_nonempty(values) -> str:
    for value in values:
        if value:
            return compact_reason(str(value))
    return ""


def write_summary_csv(path: Path, rows: Sequence[ReproductionResult]) -> None:
    findings = {row.finding for row in rows}
    reproduced_findings = {row.finding for row in rows if row.reproduced}
    finding_categories = classify_findings(rows)
    tool_failures = tool_failure_rows(rows)
    summary = [
        {"metric": "findings", "value": str(len(findings))},
        {"metric": "rows", "value": str(len(rows))},
        {"metric": "source_reproduced_findings", "value": str(len(reproduced_findings))},
        {"metric": "not_reproduced_by_selected_tools", "value": str(len(findings - reproduced_findings))},
        {"metric": "decompile_ok_rows", "value": str(sum(1 for row in rows if row.decompile_status == "ok"))},
        {"metric": "source_compile_ok_rows", "value": str(sum(1 for row in rows if is_executed_source_status(row.source_status)))},
        {"metric": "tool_failure_rows", "value": str(len(tool_failures))},
        {"metric": "tool_timeout_rows", "value": str(sum(1 for row in tool_failures if row["status"] == "timeout"))},
    ]
    for failure_class in sorted({row["failure_class"] for row in tool_failures}):
        class_rows = [row for row in tool_failures if row["failure_class"] == failure_class]
        summary.append({"metric": f"tool_failure_class:{failure_class}", "value": str(len(class_rows))})
    for stage in sorted({row["stage"] for row in tool_failures}):
        stage_rows = [row for row in tool_failures if row["stage"] == stage]
        summary.append({"metric": f"tool_failure_stage:{stage}", "value": str(len(stage_rows))})
        summary.append({"metric": f"tool_timeout_stage:{stage}", "value": str(sum(1 for row in stage_rows if row["status"] == "timeout"))})
    for category in [
        "source_reproduced",
        "unconfirmed",
        "unavailable_interpreter",
        "no_source",
        "compile_failure",
        "behavior_divergence",
    ]:
        summary.append({"metric": f"category:{category}", "value": str(sum(1 for value in finding_categories.values() if value == category))})
    for tool in sorted({row.decompiler for row in rows if row.decompiler}):
        tool_rows = [row for row in rows if row.decompiler == tool]
        tool_failure_subset = [row for row in tool_failures if row["decompiler"] == tool]
        summary.append({"metric": f"{tool}_rows", "value": str(len(tool_rows))})
        summary.append({"metric": f"{tool}_decompile_ok", "value": str(sum(1 for row in tool_rows if row.decompile_status == "ok"))})
        summary.append({"metric": f"{tool}_reproduced", "value": str(sum(1 for row in tool_rows if row.reproduced))})
        summary.append({"metric": f"{tool}_failure_rows", "value": str(len(tool_failure_subset))})
        summary.append({"metric": f"{tool}_timeout_rows", "value": str(sum(1 for row in tool_failure_subset if row["status"] == "timeout"))})
        for failure_class in sorted({row["failure_class"] for row in tool_failure_subset}):
            count = sum(1 for row in tool_failure_subset if row["failure_class"] == failure_class)
            summary.append({"metric": f"{tool}_failure_class:{failure_class}", "value": str(count)})
    for tag in sorted({row.python_tag for row in rows}):
        tag_findings = {row.finding for row in rows if row.python_tag == tag}
        tag_reproduced = {row.finding for row in rows if row.python_tag == tag and row.reproduced}
        summary.append({"metric": f"{tag}_findings", "value": str(len(tag_findings))})
        summary.append({"metric": f"{tag}_reproduced", "value": str(len(tag_reproduced))})
        for category in sorted(set(finding_categories.values())):
            count = sum(1 for finding in tag_findings if finding_categories.get(finding) == category)
            summary.append({"metric": f"{tag}_{category}", "value": str(count)})
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=SUMMARY_FIELDNAMES, **CSV_WRITE_KWARGS)
        writer.writeheader()
        writer.writerows(sanitize_csv_row(row) for row in summary)


def sanitize_csv_row(row: dict[str, object]) -> dict[str, str]:
    return {key: sanitize_csv_value(value) for key, value in row.items()}


def sanitize_csv_value(value: object) -> str:
    text = str(value)
    return text.replace("\x00", "\\0")


def classify_findings(rows: Sequence[ReproductionResult]) -> dict[str, str]:
    by_finding: dict[str, list[ReproductionResult]] = {}
    for row in rows:
        by_finding.setdefault(row.finding, []).append(row)
    return {finding: classify_finding(items) for finding, items in by_finding.items()}


def classify_finding(rows: Sequence[ReproductionResult]) -> str:
    if any(row.reproduced for row in rows):
        return "source_reproduced"
    if all(row.bytecode_status == "unavailable_interpreter" for row in rows):
        return "unavailable_interpreter"
    if all(not behavior_class(row.bytecode_status) in {"crash", "timeout", "exception"} for row in rows):
        return "unconfirmed"
    if any(row.decompile_status == "ok" and row.source_status == "ok" for row in rows):
        return "behavior_divergence"
    if any(row.decompile_status == "ok" for row in rows):
        return "compile_failure"
    return "no_source"


def is_executed_source_status(status: str) -> bool:
    return status in {"ok", "crash", "timeout"} or status.startswith("exit_")


def compact_reason(text: str, limit: int = 240) -> str:
    compact = " ".join((text or "").split())
    if len(compact) > limit:
        return compact[: limit - 3] + "..."
    return compact
