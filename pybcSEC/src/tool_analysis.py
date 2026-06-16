"""Evaluate practical analyzability of packaged Python bytecode artifacts."""

from __future__ import annotations

import csv
from collections import Counter
import dis
import importlib.util
import json
import marshal
import os
import re
import shlex
import signal
import shutil
import subprocess
import sys
import tempfile
from multiprocessing import Pool
from dataclasses import asdict, dataclass
from pathlib import Path
from types import CodeType
from typing import Sequence

import scanner


TOOL_ANALYSIS_FIELDNAMES = [
    "artifact",
    "artifact_type",
    "pyc_path",
    "python_tag",
    "magic_number",
    "magic_matches_runtime",
    "source_present",
    "stdlib_marshal",
    "stdlib_marshal_reason",
    "stdlib_marshal_level",
    "stdlib_dis",
    "stdlib_dis_reason",
    "stdlib_dis_level",
    "uncompyle6",
    "uncompyle6_reason",
    "uncompyle6_level",
    "decompyle3",
    "decompyle3_reason",
    "decompyle3_level",
    "pylingual",
    "pylingual_reason",
    "pylingual_level",
    "overall_level",
    "overall_label",
    "error",
]
OPTIONAL_TOOLS = ("uncompyle6", "decompyle3", "pylingual")
DECOMPILER_TOOLS = OPTIONAL_TOOLS
PER_INTERPRETER_TOOLS = ("uncompyle6", "decompyle3")
GLOBAL_TOOLS = ("pylingual",)
PYLINGUAL_GIT_URL = "https://github.com/syssec-utd/pylingual.git"
PYLINGUAL_COMMIT = "99c74eeff5262c0200a3d378298af1f736e20b01"

GLOBAL_TOOL_PACKAGES = {
    "pylingual": f"git+{PYLINGUAL_GIT_URL}@{PYLINGUAL_COMMIT}",
}
GLOBAL_TOOL_PACKAGE_ENVS = {
    "pylingual": "PYBCSEC_PYLINGUAL_PACKAGE",
}
GLOBAL_TOOL_INSTALL_CMD_ENVS = {
    "pylingual": "PYBCSEC_PYLINGUAL_INSTALL_CMD",
}
GLOBAL_TOOL_PYTHON_TAGS = {
    "pylingual": "cpython-312",
}
RQ2_MIN_CPYTHON_MINOR = 8
RQ2_MAX_CPYTHON_MINOR = 14
ARTIFACT_ANALYSIS_TIMEOUT = 600


@dataclass
class ToolAnalysisResult:
    artifact: str
    artifact_type: str
    pyc_path: str
    python_tag: str
    magic_number: str
    magic_matches_runtime: bool
    source_present: bool
    stdlib_marshal: str
    stdlib_marshal_reason: str
    stdlib_marshal_level: int
    stdlib_dis: str
    stdlib_dis_reason: str
    stdlib_dis_level: int
    uncompyle6: str = "unavailable"
    uncompyle6_reason: str = ""
    uncompyle6_level: int = 0
    decompyle3: str = "unavailable"
    decompyle3_reason: str = ""
    decompyle3_level: int = 0
    pylingual: str = "unavailable"
    pylingual_reason: str = ""
    pylingual_level: int = 0
    overall_level: int = 0
    overall_label: str = "not_analyzable"
    error: str = ""


def read_bytecode_artifacts(scan_csv: Path) -> list[Path]:
    if not scan_csv.exists():
        raise FileNotFoundError(f"scan CSV not found: {scan_csv}")
    artifacts: list[Path] = []
    with scan_csv.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row.get("has_bytecode") == "True" or int(row.get("pyc_files") or 0) > 0:
                artifacts.append(Path(row["input"]))
    return artifacts


def audit_rq2_denominator(
    artifacts: Sequence[Path],
    scan_csv: Path,
    interpreters: dict[str, str | None],
    magic_tags: dict[str, str],
    out_dir: Path,
) -> tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    summary_path = out_dir / "rq2_denominator_summary.csv"
    artifact_path = out_dir / "rq2_denominator_artifacts.csv"
    full_scan_total = scan_pyc_total(scan_csv)
    selected_scan_total = scan_pyc_total(scan_csv, artifacts)
    summary = Counter()
    tag_counts: Counter[str] = Counter()
    in_scope_tag_counts: Counter[str] = Counter()
    excluded_tag_counts: Counter[str] = Counter()
    filename_tag_counts: Counter[str] = Counter()
    magic_counts: Counter[str] = Counter()
    rows = []

    total_artifacts = len(artifacts)
    print(f"RQ2 denominator audit: artifacts={total_artifacts}", flush=True)
    for artifact_index, artifact in enumerate(artifacts, start=1):
        if artifact_index == 1 or artifact_index == total_artifacts or artifact_index % 100 == 0:
            print(f"[rq2-count {artifact_index}/{total_artifacts}] {artifact}", flush=True)
        row = {
            "artifact": artifact_name_from_path(str(artifact)),
            "package": package_name_from_artifact(str(artifact)),
            "version": package_version_from_artifact(str(artifact))[1],
            "artifact_type": scanner.input_type(artifact),
            "pyc_files": 0,
            "rq2_in_scope_pyc": 0,
            "out_of_scope_pyc": 0,
            "unknown_tag_pyc": 0,
            "unsupported_tag_pyc": 0,
            "missing_interpreter_pyc": 0,
            "resolved_tags": "",
            "filename_tags": "",
            "magic_numbers": "",
            "status": "ok",
            "reason": "",
        }
        resolved_tags: Counter[str] = Counter()
        filename_tags: Counter[str] = Counter()
        artifact_magic: Counter[str] = Counter()
        try:
            entries = list(scanner.iter_entries(artifact))
        except Exception as exc:
            row["status"] = "open_failed"
            row["reason"] = f"{type(exc).__name__}:{exc}"
            summary["open_failed_artifacts"] += 1
            rows.append(row)
            continue

        for entry in entries:
            entry_path = scanner.normalize_path(entry.path)
            if entry.is_dir or not entry_path.endswith(".pyc"):
                continue
            data = entry.data or b""
            filename_tag = scanner.pyc_filename_tag(entry_path) or "unknown"
            magic = scanner.pyc_magic(data) or "unknown"
            resolved = scanner.resolve_pyc_tag(entry_path, data, magic_tags) or "unknown"
            row["pyc_files"] += 1
            filename_tags[filename_tag] += 1
            artifact_magic[magic] += 1
            resolved_tags[resolved] += 1
            filename_tag_counts[filename_tag] += 1
            magic_counts[magic] += 1
            tag_counts[resolved] += 1
            if resolved == "unknown":
                row["unknown_tag_pyc"] += 1
                excluded_tag_counts["unknown"] += 1
            elif not rq2_supported_cpython_tag(resolved):
                row["unsupported_tag_pyc"] += 1
                excluded_tag_counts[resolved] += 1
            elif not interpreters.get(resolved):
                row["missing_interpreter_pyc"] += 1
                excluded_tag_counts[f"{resolved}:missing_interpreter"] += 1
            else:
                row["rq2_in_scope_pyc"] += 1
                in_scope_tag_counts[resolved] += 1

        row["out_of_scope_pyc"] = row["pyc_files"] - row["rq2_in_scope_pyc"]
        row["resolved_tags"] = format_counter(resolved_tags)
        row["filename_tags"] = format_counter(filename_tags)
        row["magic_numbers"] = format_counter(artifact_magic)
        summary["artifacts"] += 1
        summary["pyc_files_from_artifacts"] += int(row["pyc_files"])
        summary["rq2_in_scope_pyc"] += int(row["rq2_in_scope_pyc"])
        summary["out_of_scope_pyc"] += int(row["out_of_scope_pyc"])
        summary["unknown_tag_pyc"] += int(row["unknown_tag_pyc"])
        summary["unsupported_tag_pyc"] += int(row["unsupported_tag_pyc"])
        summary["missing_interpreter_pyc"] += int(row["missing_interpreter_pyc"])
        rows.append(row)

    summary_rows = [
        {"metric": "scan_csv_pyc_files_full", "value": full_scan_total},
        {"metric": "scan_csv_pyc_files_selected_artifacts", "value": selected_scan_total},
        {"metric": "artifact_paths", "value": len(artifacts)},
        {"metric": "readable_artifacts", "value": summary["artifacts"]},
        {"metric": "open_failed_artifacts", "value": summary["open_failed_artifacts"]},
        {"metric": "pyc_files_from_artifacts", "value": summary["pyc_files_from_artifacts"]},
        {"metric": "rq2_in_scope_pyc", "value": summary["rq2_in_scope_pyc"]},
        {"metric": "out_of_scope_pyc", "value": summary["out_of_scope_pyc"]},
        {"metric": "unknown_tag_pyc", "value": summary["unknown_tag_pyc"]},
        {"metric": "unsupported_tag_pyc", "value": summary["unsupported_tag_pyc"]},
        {"metric": "missing_interpreter_pyc", "value": summary["missing_interpreter_pyc"]},
    ]
    for tag, count in sorted(in_scope_tag_counts.items(), key=lambda item: (-item[1], item[0])):
        summary_rows.append({"metric": f"in_scope_tag:{tag}", "value": count})
    for tag, count in sorted(excluded_tag_counts.items(), key=lambda item: (-item[1], item[0])):
        summary_rows.append({"metric": f"excluded_tag:{tag}", "value": count})
    for tag, count in sorted(tag_counts.items(), key=lambda item: (-item[1], item[0])):
        summary_rows.append({"metric": f"resolved_tag:{tag}", "value": count})
    for tag, count in sorted(filename_tag_counts.items(), key=lambda item: (-item[1], item[0])):
        summary_rows.append({"metric": f"filename_tag:{tag}", "value": count})
    for magic, count in sorted(magic_counts.items(), key=lambda item: (-item[1], item[0])):
        summary_rows.append({"metric": f"magic:{magic}", "value": count})

    write_dict_rows(summary_path, ["metric", "value"], summary_rows)
    print(
        "RQ2 denominator audit summary: scan_pyc={scan}, artifact_pyc={artifact_pyc}, "
        "in_scope={in_scope}, out_of_scope={out_scope}".format(
            scan=full_scan_total,
            artifact_pyc=summary["pyc_files_from_artifacts"],
            in_scope=summary["rq2_in_scope_pyc"],
            out_scope=summary["out_of_scope_pyc"],
        ),
        flush=True,
    )
    write_dict_rows(
        artifact_path,
        [
            "artifact",
            "package",
            "version",
            "artifact_type",
            "pyc_files",
            "rq2_in_scope_pyc",
            "out_of_scope_pyc",
            "unknown_tag_pyc",
            "unsupported_tag_pyc",
            "missing_interpreter_pyc",
            "resolved_tags",
            "filename_tags",
            "magic_numbers",
            "status",
            "reason",
        ],
        rows,
    )
    return summary_path, artifact_path


def scan_pyc_total(scan_csv: Path, artifacts: Sequence[Path] | None = None) -> int:
    if not scan_csv.exists():
        return 0
    selected = {str(path) for path in artifacts} if artifacts is not None else None
    total = 0
    with scan_csv.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if selected is not None and row.get("input", "") not in selected:
                continue
            total += int(row.get("pyc_files") or 0)
    return total


def format_counter(counts: Counter[str]) -> str:
    return ";".join(f"{key}:{count}" for key, count in sorted(counts.items()))


def analyze_artifacts(
    artifacts: Sequence[Path],
    workers: int,
    external_timeout: int,
    interpreters: dict[str, str | None],
    tool_envs: dict[str, dict[str, str | None]],
    data_dir: Path | None = None,
    magic_tags: dict[str, str] | None = None,
) -> list[ToolAnalysisResult]:
    selected_tools = available_tools(data_dir)
    magic_tags = magic_tags if magic_tags is not None else load_magic_tag_map(interpreters, external_timeout)
    print_rq2_scope(interpreters)
    print(
        "tool analysis inputs: artifacts={artifacts}, workers={workers}, optional_tools={tools}".format(
            artifacts=len(artifacts),
            workers=max(1, workers),
            tools=",".join(
                f"{tool}:{'yes' if analysis_tool_available(tool, selected_tools, tool_envs) else 'no'}"
                for tool in OPTIONAL_TOOLS
            ),
        )
    )
    if not artifacts:
        return []

    if workers <= 1:
        results: list[ToolAnalysisResult] = []
        try:
            for index, artifact in enumerate(artifacts, start=1):
                artifact_results = analyze_artifact(
                    artifact,
                    selected_tools,
                    interpreters,
                    tool_envs,
                    external_timeout,
                    magic_tags,
                    progress_label=f"artifact {index}/{len(artifacts)}",
                )
                results.extend(artifact_results)
                print_progress(index, len(artifacts), artifact, artifact_results)
        except KeyboardInterrupt:
            print(f"interrupted; returning {len(results)} completed pyc-analysis rows")
        return results

    results = []
    jobs = [
        (index, len(artifacts), artifact, selected_tools, interpreters, tool_envs, external_timeout, magic_tags)
        for index, artifact in enumerate(artifacts, start=1)
    ]
    completed = 0
    pool = Pool(processes=workers)
    try:
        for index, artifact, artifact_results in pool.imap_unordered(analyze_artifact_job, jobs):
            results.extend(artifact_results)
            completed += 1
            print_progress(completed, len(artifacts), artifact, artifact_results)
    except KeyboardInterrupt:
        pool.terminate()
        pool.join()
        print(f"interrupted; terminated active workers and returning {len(results)} completed pyc-analysis rows")
        return results
    pool.close()
    pool.join()
    return results


class ArtifactAnalysisTimeout(Exception):
    pass


def artifact_timeout_handler(signum: int, frame: object) -> None:
    raise ArtifactAnalysisTimeout()


def analyze_artifact_job(job: tuple[int, int, Path, dict[str, str | None], dict[str, str | None], dict[str, dict[str, str | None]], int, dict[str, str]]) -> tuple[int, Path, list[ToolAnalysisResult]]:
    index, total, artifact, selected_tools, interpreters, tool_envs, external_timeout, magic_tags = job
    old_handler = signal.signal(signal.SIGALRM, artifact_timeout_handler)
    signal.alarm(ARTIFACT_ANALYSIS_TIMEOUT)
    try:
        artifact_results = analyze_artifact(
            artifact,
            selected_tools,
            interpreters,
            tool_envs,
            external_timeout,
            magic_tags,
            progress_label=f"artifact {index}/{total}",
        )
    except ArtifactAnalysisTimeout:
        reason = f"artifact_timeout_after_{ARTIFACT_ANALYSIS_TIMEOUT}s"
        print(f"[tool-analysis-timeout artifact {index}/{total}] {reason} artifact={artifact}", flush=True)
        artifact_results = [artifact_error_result(artifact, reason)]
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)
    return index, artifact, artifact_results


def print_progress(
    completed: int,
    total: int,
    artifact: Path,
    artifact_results: Sequence[ToolAnalysisResult],
) -> None:
    pyc_count = len(artifact_results)
    marshal_ok = sum(1 for item in artifact_results if item.stdlib_marshal == "ok")
    dis_ok = sum(1 for item in artifact_results if item.stdlib_dis == "ok")
    pylingual_ok = sum(1 for item in artifact_results if item.pylingual == "ok")
    failed = sum(1 for item in artifact_results if item.overall_level == 0)
    levels = ",".join(
        f"L{level}={sum(1 for item in artifact_results if item.overall_level == level)}"
        for level in range(5)
    )
    print(
        f"[tool-analysis {completed}/{total}] pyc_files={pyc_count} marshal_ok={marshal_ok} "
        f"dis_ok={dis_ok} pylingual_ok={pylingual_ok} failed={failed} {levels} latest={artifact}"
    )


def available_tools(data_dir: Path | None = None) -> dict[str, str | None]:
    return {tool: find_global_tool(tool, data_dir) for tool in OPTIONAL_TOOLS}


def analysis_tool_available(
    tool: str,
    global_tools: dict[str, str | None],
    tool_envs: dict[str, dict[str, str | None]],
) -> bool:
    return bool(global_tools.get(tool)) or any(bool(env.get(tool)) for env in tool_envs.values())


def tools_for_tag(
    tag: str,
    global_tools: dict[str, str | None],
    tool_envs: dict[str, dict[str, str | None]],
) -> dict[str, str | None]:
    tools = dict(global_tools)
    for tool, executable in tool_envs.get(tag, {}).items():
        if executable:
            tools[tool] = executable
    return tools


def load_interpreter_environment(
    versions_csv: Path,
    data_dir: Path | None = None,
) -> dict[str, str | None]:
    interpreters: dict[str, str | None] = {}
    if not versions_csv.exists():
        return interpreters
    with versions_csv.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            interpreter = row.get("interpreter", "").strip()
            if not interpreter:
                continue
            raw_tag = row.get("python_tag", "") or row.get("name", "")
            tag = tag_from_interpreter(interpreter) or scanner.canonical_pyc_tag(raw_tag)
            if not tag or tag == "unknown" or not rq2_supported_cpython_tag(tag):
                continue
            interpreters[tag] = find_interpreter(tag, interpreter, data_dir)
    return interpreters


def find_interpreter(tag: str, interpreter: str, data_dir: Path | None) -> str | None:
    version = cpython_tag_version(tag)
    candidates: list[Path | str | None] = []
    if data_dir:
        candidates.append(data_dir / "rq2" / "envs" / tag / "bin" / "python")
    candidates.extend(
        [
            shutil.which(interpreter) if interpreter else None,
            shutil.which(f"python{version}") if version else None,
            Path("/usr/bin") / f"python{version}" if version else None,
            Path("/usr/local/bin") / f"python{version}" if version else None,
            Path.home() / ".pyenv" / "versions" / version / "bin" / "python" if version else None,
            Path.home() / ".asdf" / "installs" / "python" / version / "bin" / "python" if version else None,
            Path("/opt") / f"python{version}" / "bin" / "python" if version else None,
            manylinux_python_path(tag),
        ]
    )
    candidates.extend(uv_python_candidates(version))
    for candidate in candidates:
        if candidate is None:
            continue
        path = Path(candidate)
        if path.exists():
            return str(path)
        if isinstance(candidate, str):
            return candidate
    return None


def uv_python_candidates(version: str) -> list[Path]:
    if not version:
        return []
    candidates: list[Path] = []
    executable = f"python{version}"
    roots: list[Path] = []
    if os.environ.get("UV_PYTHON_INSTALL_DIR"):
        roots.append(Path(os.environ["UV_PYTHON_INSTALL_DIR"]))
    if os.environ.get("XDG_DATA_HOME"):
        roots.append(Path(os.environ["XDG_DATA_HOME"]) / "uv" / "python")
    roots.extend(
        [
            Path.home() / ".local" / "share" / "uv" / "python",
            Path.home() / ".local" / "bin",
            Path("/root/.local/share/uv/python"),
            Path("/root/.local/bin"),
        ]
    )
    for root in roots:
        if root.name == "bin":
            candidates.append(root / executable)
            continue
        if not root.exists():
            continue
        candidates.extend(sorted(root.glob(f"cpython-{version}*/bin/{executable}")))
        candidates.extend(sorted(root.glob(f"cpython-{version}*/bin/python")))
    return candidates


def cpython_tag_version(tag: str) -> str:
    if not tag.startswith("cpython-"):
        return ""
    raw = tag.removeprefix("cpython-")
    if len(raw) == 2:
        return f"{raw[0]}.{raw[1]}"
    if len(raw) == 3:
        return f"{raw[0]}.{raw[1:]}"
    return ""


def manylinux_python_path(tag: str) -> Path | None:
    if not tag.startswith("cpython-"):
        return None
    raw = tag.removeprefix("cpython-")
    cp_tag = f"cp{raw}"
    return Path("/opt/python") / f"{cp_tag}-{cp_tag}" / "bin" / "python"


def load_tool_environment(data_dir: Path, interpreters: dict[str, str | None]) -> dict[str, dict[str, str | None]]:
    envs: dict[str, dict[str, str | None]] = {}
    for tag in interpreters:
        env_bin = data_dir / "rq2" / "envs" / tag / "bin"
        envs[tag] = {
            tool: str(env_bin / tool) if (env_bin / tool).exists() else None
            for tool in PER_INTERPRETER_TOOLS
        }
    return envs


def print_interpreter_environment(interpreters: dict[str, str | None]) -> None:
    if not interpreters:
        print("CPython interpreter environment: no version summary found")
        return
    print(
        "CPython interpreter environment: "
        + ", ".join(
            f"{tag}:{path if path else 'missing'}" for tag, path in sorted(interpreters.items())
        )
    )


def print_rq2_scope(interpreters: dict[str, str | None]) -> None:
    in_scope = [
        tag
        for tag in sorted(interpreters)
        if rq2_in_scope_tag(tag, interpreters)
    ]
    print(
        "RQ2 bytecode scope: "
        + (
            ", ".join(in_scope)
            if in_scope
            else f"no prepared CPython 3.{RQ2_MIN_CPYTHON_MINOR}--3.{RQ2_MAX_CPYTHON_MINOR} interpreters"
        )
    )


def prepare_analysis_environment(
    data_dir: Path,
    versions_csv: Path,
    timeout: int,
    extra_tags: Sequence[str] = (),
) -> Path:
    interpreters = load_interpreter_environment(versions_csv, data_dir=data_dir)
    for tag in extra_tags:
        if not rq2_supported_cpython_tag(tag):
            print(f"[prepare-env] {tag}: outside RQ2 CPython scope; skipping")
            continue
        interpreters.setdefault(
            tag,
            find_interpreter(tag, scanner.python_tag_to_executable(tag), data_dir),
        )
    out_csv = data_dir / "rq2" / "analysis_environment.csv"
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    if not interpreters:
        rows.append(
            {
                "python_tag": "",
                "interpreter": "",
                "env_dir": "",
                "tool": "",
                "status": "no_versions",
                "reason": f"missing or empty {versions_csv}",
            }
        )
    for tag, interpreter in sorted(interpreters.items()):
        env_dir = data_dir / "rq2" / "envs" / tag
        if interpreter is None:
            print(f"[prepare-env] {tag}: missing interpreter; attempting automatic install")
            install_status, install_reason = install_cpython(tag, timeout)
            interpreter = find_interpreter(tag, scanner.python_tag_to_executable(tag), None)
            rows.append(
                {
                    "python_tag": tag,
                    "interpreter": interpreter or "",
                    "env_dir": str(env_dir),
                    "tool": "cpython",
                    "status": install_status if interpreter is None else "ok",
                    "reason": install_reason,
                }
            )
            if interpreter is None:
                print(f"[prepare-env] {tag}: cpython {install_status} ({install_reason})")
                continue
            print(f"[prepare-env] {tag}: cpython ok {interpreter}")
        create_status, create_reason = create_venv(interpreter, env_dir, timeout)
        rows.append(
            {
                "python_tag": tag,
                "interpreter": interpreter,
                "env_dir": str(env_dir),
                "tool": "venv",
                "status": create_status,
                "reason": create_reason,
            }
        )
        print(f"[prepare-env] {tag}: venv {create_status} {env_dir}")
        if create_status != "ok":
            continue
        for tool in PER_INTERPRETER_TOOLS:
            status, reason = install_env_tool(env_dir, tool, timeout)
            rows.append(
                {
                    "python_tag": tag,
                    "interpreter": interpreter,
                    "env_dir": str(env_dir),
                    "tool": tool,
                    "status": status,
                    "reason": reason,
                }
            )
            print(f"[prepare-env] {tag}: {tool} {status}")

    for tool in GLOBAL_TOOLS:
        status, reason, executable = install_global_tool(tool, timeout, data_dir)
        rows.append(
            {
                "python_tag": "global",
                "interpreter": "",
                "env_dir": "",
                "tool": tool,
                "status": status,
                "reason": reason,
            }
        )
        location = f" {executable}" if executable else ""
        print(f"[prepare-env] global: {tool} {status}{location}")

    with out_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["python_tag", "interpreter", "env_dir", "tool", "status", "reason"])
        writer.writeheader()
        writer.writerows(rows)
    write_tool_versions(data_dir, load_interpreter_environment(versions_csv, data_dir=data_dir))
    return out_csv


def write_tool_versions(data_dir: Path, interpreters: dict[str, str | None]) -> Path:
    out_csv = data_dir / "rq2" / "tool_versions.csv"
    rows = []
    for tag, interpreter in sorted(interpreters.items()):
        if not interpreter:
            rows.append({"python_tag": tag, "tool": "cpython", "executable": "", "version": "missing"})
            continue
        rows.append(
            {
                "python_tag": tag,
                "tool": "cpython",
                "executable": interpreter,
                "version": command_version([interpreter, "--version"]),
            }
        )
        env_bin = data_dir / "rq2" / "envs" / tag / "bin"
        for tool in PER_INTERPRETER_TOOLS:
            executable = env_bin / tool
            rows.append(
                {
                    "python_tag": tag,
                    "tool": tool,
                    "executable": str(executable) if executable.exists() else "",
                    "version": tool_version(tool, str(executable)) if executable.exists() else "missing",
                }
            )
    for tool in GLOBAL_TOOLS:
        executable = find_global_tool(tool, data_dir)
        rows.append(
            {
                "python_tag": "global",
                "tool": tool,
                "executable": executable or "",
                "version": tool_version(tool, executable) if executable else "missing",
            }
        )
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["python_tag", "tool", "executable", "version"])
        writer.writeheader()
        writer.writerows(rows)
    return out_csv


def tool_version(tool: str, executable: str | None) -> str:
    if not executable:
        return "missing"
    if tool == "pylingual":
        help_text = command_version([executable, "--help"])
        if help_text.startswith("Usage: pylingual"):
            return "installed (version unavailable)"
        return help_text
    return command_version([executable, "--version"])


def find_global_tool(tool: str, data_dir: Path | None = None) -> str | None:
    candidates: list[Path | str | None] = []
    if data_dir:
        candidates.append(global_tool_env_dir(data_dir, tool) / "bin" / tool)
    candidates.extend(
        [
            shutil.which(tool),
            Path(sys.executable).resolve().parent / tool,
            Path(sys.prefix) / "bin" / tool,
            Path.home() / ".local" / "bin" / tool,
            Path("/root/.local/bin") / tool,
            Path("/usr/local/bin") / tool,
            Path("/usr/bin") / tool,
        ]
    )
    for candidate in candidates:
        if not candidate:
            continue
        path = Path(candidate)
        if path.exists():
            return str(path)
        if isinstance(candidate, str):
            return candidate
    return None


def install_global_tool(tool: str, timeout: int, data_dir: Path | None = None) -> tuple[str, str, str | None]:
    if tool in GLOBAL_TOOL_PYTHON_TAGS and data_dir is not None:
        managed_executable = global_tool_env_dir(data_dir, tool) / "bin" / tool
        if managed_executable.exists():
            return "ok", "exists", str(managed_executable)
        return install_global_tool_env(tool, data_dir, timeout)
    executable = find_global_tool(tool, data_dir)
    if executable:
        return "ok", "exists", executable
    package = global_tool_package(tool)
    commands = [
        [sys.executable, "-m", "pip", "install", "--user", package],
        [sys.executable, "-m", "pip", "install", package],
    ]
    last_status = "installer_unavailable"
    last_reason = f"{tool} not found"
    for command in commands:
        status, reason = run_installer(command, timeout)
        if status != "ok":
            last_status, last_reason = status, reason
            continue
        executable = find_global_tool(tool, data_dir)
        if executable:
            return "ok", reason, executable
        last_status = "installer_unavailable"
        last_reason = f"installed {package}, but {tool} executable was not found"
    return last_status, last_reason, None


def global_tool_package(tool: str) -> str:
    env_name = GLOBAL_TOOL_PACKAGE_ENVS.get(tool)
    if env_name and os.environ.get(env_name):
        return os.environ[env_name]
    return GLOBAL_TOOL_PACKAGES.get(tool, tool)


def global_tool_env_dir(data_dir: Path, tool: str) -> Path:
    return data_dir / "rq2" / "envs" / f"global-{tool}"


def install_global_tool_env(tool: str, data_dir: Path, timeout: int) -> tuple[str, str, str | None]:
    tag = GLOBAL_TOOL_PYTHON_TAGS[tool]
    interpreter = find_interpreter(tag, scanner.python_tag_to_executable(tag), data_dir)
    if interpreter is None:
        install_status, install_reason = install_cpython(tag, timeout)
        interpreter = find_interpreter(tag, scanner.python_tag_to_executable(tag), data_dir)
        if interpreter is None:
            return install_status, install_reason, None
    env_dir = global_tool_env_dir(data_dir, tool)
    create_status, create_reason = create_venv(interpreter, env_dir, timeout)
    if create_status != "ok":
        return create_status, create_reason, None
    package = global_tool_package(tool)
    status, reason = install_global_tool_package(env_dir, tool, package, timeout)
    executable = find_global_tool(tool, data_dir)
    if status == "ok" and executable:
        return "ok", reason, executable
    if status == "ok":
        return "installer_unavailable", f"installed {package}, but {tool} executable was not found", None
    return status, reason, executable


def install_global_tool_package(env_dir: Path, tool: str, package: str, timeout: int) -> tuple[str, str]:
    command = global_tool_install_command(env_dir, tool, package)
    if command:
        return run_shell_installer(command, env_dir, timeout)
    return install_env_package(env_dir, tool, package, timeout)


def has_global_tool_install_command(tool: str) -> bool:
    env_name = GLOBAL_TOOL_INSTALL_CMD_ENVS.get(tool)
    return bool(env_name and os.environ.get(env_name))


def global_tool_install_command(env_dir: Path, tool: str, package: str) -> str:
    env_name = GLOBAL_TOOL_INSTALL_CMD_ENVS.get(tool)
    template = os.environ.get(env_name, "") if env_name else ""
    if not template:
        return ""
    python = env_dir / "bin" / "python"
    pip = env_dir / "bin" / "pip"
    return template.format(
        python=shlex.quote(str(python)),
        pip=shlex.quote(str(pip)),
        env_dir=shlex.quote(str(env_dir)),
        package=shlex.quote(package),
    )


def run_shell_installer(command: str, env_dir: Path, timeout: int) -> tuple[str, str]:
    env = os.environ.copy()
    env["PATH"] = str(env_dir / "bin") + os.pathsep + env.get("PATH", "")
    try:
        completed = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
            text=True,
            errors="replace",
            env=env,
        )
    except subprocess.TimeoutExpired:
        return "timeout", f"timeout_after_{timeout}s"
    except OSError as exc:
        return "error", f"{type(exc).__name__}:{exc}"
    if completed.returncode == 0:
        return "ok", compact_reason(completed.stdout)
    return f"exit_{completed.returncode}", compact_reason(completed.stderr) or compact_reason(completed.stdout)


def command_version(command: Sequence[str]) -> str:
    try:
        completed = subprocess.run(
            list(command),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=20,
            check=False,
            text=True,
            errors="replace",
        )
    except (subprocess.TimeoutExpired, OSError) as exc:
        return f"error:{type(exc).__name__}:{exc}"
    text = compact_reason(completed.stdout) or compact_reason(completed.stderr)
    return text or f"exit_{completed.returncode}"


def install_cpython(tag: str, timeout: int) -> tuple[str, str]:
    version = cpython_tag_version(tag)
    if not version:
        return "unsupported_tag", tag
    uv_status, uv_reason = ensure_uv(timeout)
    uv = find_uv()
    if uv:
        status, reason = run_installer([uv, "python", "install", version], timeout)
        if status == "ok":
            return status, reason
        uv_status, uv_reason = status, reason
    apt = shutil.which("apt-get")
    if apt:
        status, reason = apt_install_cpython(apt, version, timeout)
        if status == "ok":
            return status, reason
    pyenv = shutil.which("pyenv")
    if pyenv:
        install_version = pyenv_install_version(pyenv, version, timeout)
        if install_version:
            return run_installer([pyenv, "install", "-s", install_version], timeout)
        return "installer_failed", f"pyenv has no installable version for {version}"
    return "installer_unavailable", f"uv:{uv_status}:{uv_reason}; install {scanner.python_tag_to_executable(tag)} or install apt/pyenv"


def ensure_uv(timeout: int) -> tuple[str, str]:
    uv = find_uv()
    if uv:
        return "ok", uv
    commands = [
        [sys.executable, "-m", "pip", "install", "--user", "uv"],
        [sys.executable, "-m", "pip", "install", "uv"],
    ]
    last_status = "installer_unavailable"
    last_reason = "uv not found"
    for command in commands:
        status, reason = run_installer(command, timeout)
        if status != "ok":
            last_status, last_reason = status, reason
            continue
        uv = find_uv()
        if uv:
            return "ok", f"installed uv at {uv}"
        last_status, last_reason = "installer_unavailable", "pip installed uv but executable was not found"
    return last_status, last_reason


def find_uv() -> str | None:
    candidates = [
        shutil.which("uv"),
        Path(sys.executable).resolve().parent / "uv",
        Path(sys.prefix) / "bin" / "uv",
        Path("/usr/local/bin/uv"),
        Path("/usr/bin/uv"),
        Path.home() / ".local" / "bin" / "uv",
        Path("/root/.local/bin/uv"),
    ]
    for candidate in candidates:
        if not candidate:
            continue
        path = Path(candidate)
        if path.exists():
            return str(path)
        if isinstance(candidate, str):
            return candidate
    return None


def apt_install_cpython(apt: str, version: str, timeout: int) -> tuple[str, str]:
    prefix = [apt] if os.geteuid() == 0 else sudo_prefix()
    if not prefix:
        return "installer_unavailable", "apt-get requires root or passwordless sudo"
    update_status, update_reason = run_installer([*prefix, "update"], timeout)
    if update_status != "ok":
        return update_status, update_reason
    packages = [f"python{version}", f"python{version}-venv"]
    install_status, install_reason = run_installer([*prefix, "install", "-y", *packages], timeout)
    if install_status == "ok":
        return "ok", "installed " + " ".join(packages)
    return install_status, install_reason


def sudo_prefix() -> list[str]:
    sudo = shutil.which("sudo")
    if not sudo:
        return []
    return [sudo, "-n", "apt-get"]


def run_installer(command: Sequence[str], timeout: int) -> tuple[str, str]:
    try:
        completed = subprocess.run(
            list(command),
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
        return "ok", compact_reason(completed.stdout)
    return f"exit_{completed.returncode}", compact_reason(completed.stderr) or compact_reason(completed.stdout)


def pyenv_install_version(pyenv: str, version: str, timeout: int) -> str:
    try:
        completed = subprocess.run(
            [pyenv, "install", "--list"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
            text=True,
            errors="replace",
        )
    except (subprocess.TimeoutExpired, OSError):
        return ""
    if completed.returncode != 0:
        return ""
    prefix = version + "."
    matches = [
        item.strip()
        for item in completed.stdout.splitlines()
        if item.strip() == version or item.strip().startswith(prefix)
    ]
    return matches[-1] if matches else ""


def create_venv(interpreter: str, env_dir: Path, timeout: int) -> tuple[str, str]:
    if (env_dir / "bin" / "python").exists():
        return "ok", "exists"
    try:
        completed = subprocess.run(
            [interpreter, "-m", "venv", str(env_dir)],
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


def install_env_tool(env_dir: Path, tool: str, timeout: int) -> tuple[str, str]:
    return install_env_package(env_dir, tool, tool, timeout)


def install_env_package(env_dir: Path, tool: str, package: str, timeout: int) -> tuple[str, str]:
    executable = env_dir / "bin" / tool
    if executable.exists():
        return "ok", "exists"
    pip = env_dir / "bin" / "pip"
    try:
        completed = subprocess.run(
            [str(pip), "install", package],
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


def artifact_error_result(artifact: Path, reason: str) -> ToolAnalysisResult:
    return ToolAnalysisResult(
        artifact=str(artifact),
        artifact_type=scanner.input_type(artifact),
        pyc_path="",
        python_tag="",
        magic_number="",
        magic_matches_runtime=False,
        source_present=False,
        stdlib_marshal="error",
        stdlib_marshal_reason=reason,
        stdlib_marshal_level=0,
        stdlib_dis="error",
        stdlib_dis_reason=reason,
        stdlib_dis_level=0,
        error=reason,
    )


def analyze_artifact(
    artifact: Path,
    selected_tools: dict[str, str | None],
    interpreters: dict[str, str | None],
    tool_envs: dict[str, dict[str, str | None]],
    external_timeout: int,
    magic_tags: dict[str, str] | None = None,
    progress_label: str = "",
) -> list[ToolAnalysisResult]:
    try:
        entries = list(scanner.iter_entries(artifact))
    except Exception as exc:
        return [artifact_error_result(artifact, f"open_failed:{type(exc).__name__}:{exc}")]

    py_paths = {scanner.normalize_path(entry.path) for entry in entries if not entry.is_dir and entry.path.endswith(".py")}
    magic_tags = magic_tags or {}
    pyc_entries = []
    for entry in entries:
        entry_path = scanner.normalize_path(entry.path)
        if entry.is_dir or not entry_path.endswith(".pyc"):
            continue
        tag = pyc_analysis_tag(entry_path, entry.data or b"", magic_tags)
        if rq2_in_scope_tag(tag, interpreters):
            pyc_entries.append((entry, tag))
    if progress_label:
        print(f"[tool-analysis-active {progress_label}] pyc_files={len(pyc_entries)} artifact={artifact}", flush=True)

    results = []
    for pyc_index, (entry, tag) in enumerate(pyc_entries, start=1):
        entry_path = scanner.normalize_path(entry.path)
        if progress_label and (pyc_index == 1 or pyc_index == len(pyc_entries) or pyc_index % 25 == 0):
            print(
                f"[tool-analysis-active {progress_label}] pyc {pyc_index}/{len(pyc_entries)} artifact={artifact}",
                flush=True,
            )
        result = analyze_pyc_entry(
            artifact,
            scanner.input_type(artifact),
            entry_path,
            entry.data or b"",
            py_paths,
            selected_tools,
            interpreters,
            tool_envs,
            external_timeout,
            tag,
        )
        results.append(result)
    return results


def analyze_pyc_entry(
    artifact: Path,
    artifact_type: str,
    pyc_path: str,
    data: bytes,
    py_paths: set[str],
    selected_tools: dict[str, str | None],
    interpreters: dict[str, str | None],
    tool_envs: dict[str, dict[str, str | None]],
    external_timeout: int,
    tag: str | None = None,
) -> ToolAnalysisResult:
    magic_number = scanner.pyc_magic(data) or ""
    source_present = any(candidate in py_paths for candidate in scanner.module_source_candidates(pyc_path))
    tag = tag or python_tag(pyc_path)

    result = ToolAnalysisResult(
        artifact=str(artifact),
        artifact_type=artifact_type,
        pyc_path=pyc_path,
        python_tag=tag,
        magic_number=magic_number,
        magic_matches_runtime=data[:4] == importlib.util.MAGIC_NUMBER if len(data) >= 4 else False,
        source_present=source_present,
        stdlib_marshal="not_run",
        stdlib_marshal_reason="",
        stdlib_marshal_level=0,
        stdlib_dis="not_run",
        stdlib_dis_reason="",
        stdlib_dis_level=0,
    )

    with tempfile.TemporaryDirectory(prefix="pybcsec-rq2-") as tmpdir:
        tmp_pyc = Path(tmpdir) / "sample.pyc"
        tmp_pyc.write_bytes(data)
        marshal_status, marshal_reason, dis_status, dis_reason = run_stdlib_analysis(
            tmp_pyc,
            data,
            tag,
            interpreters,
            external_timeout,
        )
        result.stdlib_marshal = marshal_status
        result.stdlib_marshal_reason = marshal_reason
        result.stdlib_marshal_level = 1 if marshal_status == "ok" else 0
        result.stdlib_dis = dis_status
        result.stdlib_dis_reason = dis_reason
        result.stdlib_dis_level = 2 if dis_status == "ok" else 0
        result.error = "|".join(item for item in (marshal_reason, dis_reason) if item)

        entry_tools = tools_for_tag(tag, selected_tools, tool_envs)
        if any(entry_tools.values()):
            for tool, executable in entry_tools.items():
                status, reason = run_optional_tool(tool, executable, tmp_pyc, external_timeout)
                setattr(result, tool, status)
                setattr(result, f"{tool}_reason", reason)
                setattr(result, f"{tool}_level", 3 if status == "ok" else 0)

    result.overall_level, result.overall_label = classify_overall_level(result, tools_for_tag(tag, selected_tools, tool_envs))

    return result


def run_stdlib_analysis(
    pyc_path: Path,
    data: bytes,
    tag: str,
    interpreters: dict[str, str | None],
    timeout: int,
) -> tuple[str, str, str, str]:
    if tag.startswith("cpython-"):
        if tag in interpreters and interpreters[tag] is None:
            return "unavailable_interpreter", f"missing interpreter for {tag}", "unavailable_interpreter", f"missing interpreter for {tag}"
        executable = interpreters.get(tag)
        if executable:
            return run_stdlib_interpreter(executable, pyc_path, timeout)
    code, marshal_status, marshal_error = load_code_object(data)
    if code is None:
        return marshal_status, marshal_error, "not_run", ""
    dis_status, dis_error = disassemble_code_object(code)
    return marshal_status, marshal_error, dis_status, dis_error


def run_stdlib_interpreter(executable: str, pyc_path: Path, timeout: int) -> tuple[str, str, str, str]:
    script = (
        "import dis,json,marshal,sys\n"
        "data=open(sys.argv[1],'rb').read()\n"
        "errors=[]; code=None\n"
        "for offset in (16,12,8):\n"
        "    if len(data) <= offset: continue\n"
        "    try: obj=marshal.loads(data[offset:])\n"
        "    except Exception as exc: errors.append(f'offset{offset}:{type(exc).__name__}:{exc}'); continue\n"
        "    if hasattr(obj, 'co_code'): code=obj; break\n"
        "    errors.append(f'offset{offset}:not_code')\n"
        "if code is None:\n"
        "    print(json.dumps({'marshal':'error','marshal_reason':'marshal_failed:' + ','.join(errors),'dis':'not_run','dis_reason':''}))\n"
        "else:\n"
        "    try:\n"
        "        list(dis.Bytecode(code)); print(json.dumps({'marshal':'ok','marshal_reason':'','dis':'ok','dis_reason':''}))\n"
        "    except Exception as exc:\n"
        "        print(json.dumps({'marshal':'ok','marshal_reason':'','dis':'error','dis_reason':f'dis_failed:{type(exc).__name__}:{exc}'}))\n"
    )
    try:
        completed = subprocess.run(
            [executable, "-c", script, str(pyc_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
            text=True,
            errors="replace",
        )
    except subprocess.TimeoutExpired:
        reason = f"timeout_after_{timeout}s"
        return "timeout", reason, "timeout", reason
    except OSError as exc:
        reason = f"{type(exc).__name__}:{exc}"
        return "error", reason, "error", reason
    if completed.returncode != 0:
        reason = compact_reason(completed.stderr) or compact_reason(completed.stdout)
        return f"exit_{completed.returncode}", reason, "not_run", ""
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        reason = f"json_decode_failed:{exc}:{compact_reason(completed.stdout)}"
        return "error", reason, "not_run", ""
    return (
        payload.get("marshal", "error"),
        payload.get("marshal_reason", ""),
        payload.get("dis", "not_run"),
        payload.get("dis_reason", ""),
    )


def load_code_object(data: bytes) -> tuple[CodeType | None, str, str]:
    errors = []
    for offset in (16, 12, 8):
        if len(data) <= offset:
            continue
        try:
            obj = marshal.loads(data[offset:])
        except Exception as exc:
            errors.append(f"offset{offset}:{type(exc).__name__}")
            continue
        if isinstance(obj, CodeType):
            return obj, "ok", ""
        errors.append(f"offset{offset}:not_code")
    return None, "error", "marshal_failed:" + ",".join(errors)


def disassemble_code_object(code: CodeType) -> tuple[str, str]:
    try:
        for _ in dis.Bytecode(code):
            pass
        return "ok", ""
    except Exception as exc:
        return "error", f"dis_failed:{type(exc).__name__}:{exc}"


def load_magic_tag_map(interpreters: dict[str, str | None], timeout: int) -> dict[str, str]:
    magic_tags: dict[str, str] = {}
    for tag, executable in sorted(interpreters.items()):
        if not executable or not rq2_supported_cpython_tag(tag):
            continue
        magic = interpreter_magic_number(executable, max(1, min(timeout, 10)))
        if magic:
            magic_tags[magic] = tag
    if magic_tags:
        print(
            "RQ2 magic map: "
            + ", ".join(f"{magic}->{tag}" for magic, tag in sorted(magic_tags.items(), key=lambda item: item[1]))
        )
    return magic_tags


def interpreter_magic_number(executable: str, timeout: int) -> str:
    script = "import importlib.util,struct; print(struct.unpack('<H', importlib.util.MAGIC_NUMBER[:2])[0])"
    try:
        completed = subprocess.run(
            [executable, "-c", script],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
            text=True,
            errors="replace",
        )
    except (OSError, subprocess.TimeoutExpired):
        return ""
    if completed.returncode != 0:
        return ""
    return completed.stdout.strip()


def pyc_analysis_tag(pyc_path: str, data: bytes, magic_tags: dict[str, str]) -> str:
    return scanner.resolve_pyc_tag(pyc_path, data, magic_tags)


def python_tag(pyc_path: str) -> str:
    name = Path(pyc_path).name
    parts = name.split(".")
    for part in parts:
        tag = scanner.canonical_pyc_tag(part)
        if tag:
            return tag
    return ""


def canonical_analysis_tag(value: str) -> str:
    return scanner.canonical_pyc_tag(value)


def tag_from_interpreter(interpreter: str) -> str:
    name = Path(interpreter).name
    if not name.startswith("python3."):
        return ""
    minor = name.removeprefix("python3.")
    if not minor.isdigit():
        return ""
    return f"cpython-3{minor}"


def supported_cpython_analysis_tag(tag: str) -> bool:
    version = cpython_tag_version(tag)
    if not version:
        return False
    major, _, minor = version.partition(".")
    if major != "3" or not minor.isdigit():
        return False
    return True


def rq2_supported_cpython_tag(tag: str) -> bool:
    version = cpython_tag_version(tag)
    if not version:
        return False
    major, _, minor = version.partition(".")
    if major != "3" or not minor.isdigit():
        return False
    minor_int = int(minor)
    return RQ2_MIN_CPYTHON_MINOR <= minor_int <= RQ2_MAX_CPYTHON_MINOR


def rq2_in_scope_tag(tag: str, interpreters: dict[str, str | None]) -> bool:
    if not rq2_supported_cpython_tag(tag):
        return False
    return bool(interpreters.get(tag))


def run_optional_tool(tool: str, executable: str | None, pyc_path: Path, timeout: int) -> tuple[str, str]:
    if executable is None:
        return "unavailable", "not installed on PATH"
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
    if completed.returncode == 0:
        return "ok", ""
    reason = compact_reason(completed.stderr) or compact_reason(completed.stdout)
    return f"exit_{completed.returncode}", reason


def compact_reason(text: str, limit: int = 240) -> str:
    reason = " ".join(text.strip().split())
    if len(reason) > limit:
        return reason[: limit - 3] + "..."
    return reason


def classify_overall_level(
    result: ToolAnalysisResult,
    selected_tools: dict[str, str | None],
) -> tuple[int, str]:
    if result.stdlib_marshal != "ok":
        successful_decompilers = successful_available_decompilers(result, selected_tools)
        if successful_decompilers:
            return decompiler_level(successful_decompilers, selected_tools)
        return 0, "not_analyzable"
    if result.stdlib_dis != "ok":
        successful_decompilers = successful_available_decompilers(result, selected_tools)
        if successful_decompilers:
            return decompiler_level(successful_decompilers, selected_tools)
        return 1, "loadable_only"

    successful_decompilers = successful_available_decompilers(result, selected_tools)
    if successful_decompilers:
        return decompiler_level(successful_decompilers, selected_tools)
    return 2, "disassemblable"


def successful_available_decompilers(
    result: ToolAnalysisResult,
    selected_tools: dict[str, str | None],
) -> list[str]:
    return [
        tool
        for tool in DECOMPILER_TOOLS
        if selected_tools.get(tool) and getattr(result, tool) == "ok"
    ]


def decompiler_level(
    successful_decompilers: Sequence[str],
    selected_tools: dict[str, str | None],
) -> tuple[int, str]:
    if successful_decompilers:
        return 4, "fully_decompilable"
    return 3, "partially_decompilable"


SOURCE_LESS_TOOLS = ("stdlib_marshal", "stdlib_dis", "uncompyle6", "decompyle3", "pylingual")


def write_source_less_reports(
    out_dir: Path,
    results: Sequence[ToolAnalysisResult],
    scan_csv: Path | None = None,
) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    source_less = [item for item in results if not item.source_present]
    scan_rows = read_scan_rows(scan_csv) if scan_csv else {}
    paths = [
        out_dir / "source_less_summary.csv",
        out_dir / "source_less_by_version.csv",
        out_dir / "source_less_by_artifact_type.csv",
        out_dir / "source_less_by_level.csv",
        out_dir / "source_less_tool_outcomes.csv",
        out_dir / "source_less_top_artifacts.csv",
        out_dir / "source_less_top_packages.csv",
        out_dir / "source_less_artifact_properties.csv",
        out_dir / "source_less_keyword_categories.csv",
    ]
    write_source_less_summary(paths[0], results, source_less, scan_rows)
    write_source_less_group_csv(paths[1], source_less, "python_tag")
    write_source_less_group_csv(paths[2], source_less, "artifact_type")
    write_source_less_level_csv(paths[3], source_less)
    write_source_less_tool_outcomes_csv(paths[4], source_less)
    write_source_less_top_artifacts_csv(paths[5], source_less)
    write_source_less_top_packages_csv(paths[6], results, source_less, scan_rows)
    write_source_less_artifact_properties_csv(paths[7], results, source_less, scan_rows)
    write_source_less_keyword_categories_csv(paths[8], source_less)
    return paths


def write_source_less_summary(
    path: Path,
    results: Sequence[ToolAnalysisResult],
    source_less: Sequence[ToolAnalysisResult],
    scan_rows: dict[str, dict[str, str]],
) -> None:
    total = len(results)
    subset = len(source_less)
    source_less_artifacts = {item.artifact for item in source_less}
    rows = [
        ("pyc_files", subset),
        ("share_of_rq2_pyc", percent_value(subset, total)),
        ("artifacts", len(source_less_artifacts)),
        ("artifacts_with_dynamic_loading_indicators", count_dynamic_artifacts(source_less_artifacts, scan_rows)),
        ("artifacts_with_security_keywords", count_keyword_artifacts(source_less)),
        ("runtime_magic", sum(1 for item in source_less if item.magic_matches_runtime)),
        ("marshal_ok", sum(1 for item in source_less if item.stdlib_marshal == "ok")),
        ("dis_ok", sum(1 for item in source_less if item.stdlib_dis == "ok")),
        ("uncompyle6_ok", sum(1 for item in source_less if item.uncompyle6 == "ok")),
        ("decompyle3_ok", sum(1 for item in source_less if item.decompyle3 == "ok")),
        ("pylingual_ok", sum(1 for item in source_less if item.pylingual == "ok")),
        ("source_recoverable", sum(1 for item in source_less if item.overall_level == 4)),
        ("not_source_recoverable", sum(1 for item in source_less if item.overall_level != 4)),
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["metric", "value"])
        writer.writeheader()
        for metric, value in rows:
            writer.writerow({"metric": metric, "value": value})


def write_source_less_group_csv(path: Path, source_less: Sequence[ToolAnalysisResult], field: str) -> None:
    groups: dict[str, list[ToolAnalysisResult]] = {}
    for item in source_less:
        key = str(getattr(item, field) or "unknown")
        groups.setdefault(key, []).append(item)
    rows = []
    total = len(source_less)
    for key, items in sorted(groups.items(), key=lambda entry: (-len(entry[1]), entry[0])):
        rows.append(
            {
                field: key,
                "pyc_files": len(items),
                "pct_source_less_pyc": percent_value(len(items), total),
                "artifacts": len({item.artifact for item in items}),
                "source_recoverable": sum(1 for item in items if item.overall_level == 4),
                "source_recoverable_pct": percent_value(sum(1 for item in items if item.overall_level == 4), len(items)),
                "marshal_ok": sum(1 for item in items if item.stdlib_marshal == "ok"),
                "dis_ok": sum(1 for item in items if item.stdlib_dis == "ok"),
                "pylingual_ok": sum(1 for item in items if item.pylingual == "ok"),
            }
        )
    fieldnames = [field, "pyc_files", "pct_source_less_pyc", "artifacts", "source_recoverable", "source_recoverable_pct", "marshal_ok", "dis_ok", "pylingual_ok"]
    write_dict_rows(path, fieldnames, rows)


def write_source_less_level_csv(path: Path, source_less: Sequence[ToolAnalysisResult]) -> None:
    counts = Counter(item.overall_label for item in source_less)
    total = len(source_less)
    rows = [
        {"level": label, "pyc_files": count, "pct_source_less_pyc": percent_value(count, total)}
        for label, count in sorted(counts.items())
    ]
    write_dict_rows(path, ["level", "pyc_files", "pct_source_less_pyc"], rows)


def write_source_less_tool_outcomes_csv(path: Path, source_less: Sequence[ToolAnalysisResult]) -> None:
    rows = []
    total = len(source_less)
    for tool in SOURCE_LESS_TOOLS:
        counts = Counter(str(getattr(item, tool)) for item in source_less)
        reason_field = f"{tool}_reason"
        reason_counts = Counter(
            str(getattr(item, reason_field, ""))
            for item in source_less
            if str(getattr(item, tool)) != "ok"
        )
        common_reason = reason_counts.most_common(1)[0][0] if reason_counts else ""
        for status, count in sorted(counts.items(), key=lambda entry: (-entry[1], entry[0])):
            rows.append(
                {
                    "tool": tool,
                    "status": status,
                    "pyc_files": count,
                    "pct_source_less_pyc": percent_value(count, total),
                    "top_non_ok_reason": common_reason if status != "ok" else "",
                }
            )
    write_dict_rows(path, ["tool", "status", "pyc_files", "pct_source_less_pyc", "top_non_ok_reason"], rows)


def write_source_less_top_artifacts_csv(path: Path, source_less: Sequence[ToolAnalysisResult], limit: int = 50) -> None:
    groups: dict[str, list[ToolAnalysisResult]] = {}
    for item in source_less:
        groups.setdefault(item.artifact, []).append(item)
    rows = []
    for artifact, items in sorted(groups.items(), key=lambda entry: (-len(entry[1]), entry[0]))[:limit]:
        rows.append(
            {
                "artifact": artifact_name_from_path(artifact),
                "package": package_name_from_artifact(artifact),
                "version": package_version_from_artifact(artifact)[1],
                "artifact_type": items[0].artifact_type if items else "",
                "source_less_pyc": len(items),
                "python_tags": ";".join(sorted({item.python_tag for item in items if item.python_tag})),
                "levels": ";".join(f"{level}:{sum(1 for item in items if item.overall_label == level)}" for level in sorted({item.overall_label for item in items})),
                "pylingual_ok": sum(1 for item in items if item.pylingual == "ok"),
            }
        )
    write_dict_rows(path, ["artifact", "package", "version", "artifact_type", "source_less_pyc", "python_tags", "levels", "pylingual_ok"], rows)




def write_source_less_top_packages_csv(
    path: Path,
    results: Sequence[ToolAnalysisResult],
    source_less: Sequence[ToolAnalysisResult],
    scan_rows: dict[str, dict[str, str]],
    limit: int = 50,
) -> None:
    all_by_package: dict[tuple[str, str], list[ToolAnalysisResult]] = {}
    source_less_by_package: dict[tuple[str, str], list[ToolAnalysisResult]] = {}
    for item in results:
        key = package_version_from_artifact(item.artifact)
        all_by_package.setdefault(key, []).append(item)
    for item in source_less:
        key = package_version_from_artifact(item.artifact)
        source_less_by_package.setdefault(key, []).append(item)

    rows = []
    for (package, version), items in sorted(source_less_by_package.items(), key=lambda entry: (-len(entry[1]), entry[0]))[:limit]:
        all_items = all_by_package.get((package, version), [])
        artifacts = {item.artifact for item in items}
        categories = keyword_categories_for_items(items)
        source_recoverable = sum(1 for item in items if item.overall_level == 4)
        rows.append(
            {
                "package": package,
                "version": version,
                "artifacts": len(artifacts),
                "artifact_types": ";".join(sorted({item.artifact_type for item in items if item.artifact_type})),
                "source_less_pyc": len(items),
                "total_pyc_in_package_version": len(all_items),
                "source_less_pyc_pct_in_package_version": percent_value(len(items), len(all_items)),
                "python_tags": ";".join(sorted({item.python_tag for item in items if item.python_tag})),
                "source_recoverable_pyc": source_recoverable,
                "source_recoverable_pct": percent_value(source_recoverable, len(items)),
                "artifacts_with_dynamic_loading_indicators": count_dynamic_artifacts(artifacts, scan_rows),
                "keyword_categories": ";".join(categories),
                "security_keyword_indicator": "yes" if "security" in categories else "no",
            }
        )
    write_dict_rows(
        path,
        [
            "package",
            "version",
            "artifacts",
            "artifact_types",
            "source_less_pyc",
            "total_pyc_in_package_version",
            "source_less_pyc_pct_in_package_version",
            "python_tags",
            "source_recoverable_pyc",
            "source_recoverable_pct",
            "artifacts_with_dynamic_loading_indicators",
            "keyword_categories",
            "security_keyword_indicator",
        ],
        rows,
    )


def write_source_less_artifact_properties_csv(
    path: Path,
    results: Sequence[ToolAnalysisResult],
    source_less: Sequence[ToolAnalysisResult],
    scan_rows: dict[str, dict[str, str]],
) -> None:
    all_by_artifact: dict[str, list[ToolAnalysisResult]] = {}
    source_less_by_artifact: dict[str, list[ToolAnalysisResult]] = {}
    for item in results:
        all_by_artifact.setdefault(item.artifact, []).append(item)
    for item in source_less:
        source_less_by_artifact.setdefault(item.artifact, []).append(item)

    rows = []
    for artifact, items in sorted(source_less_by_artifact.items(), key=lambda entry: (-len(entry[1]), entry[0])):
        all_items = all_by_artifact.get(artifact, [])
        scan_row = scan_rows.get(artifact, {})
        categories = keyword_categories_for_items(items)
        source_recoverable = sum(1 for item in items if item.overall_level == 4)
        rows.append(
            {
                "artifact": artifact_name_from_path(artifact),
                "package": package_name_from_artifact(artifact),
                "version": package_version_from_artifact(artifact)[1],
                "artifact_type": items[0].artifact_type if items else "",
                "source_less_pyc": len(items),
                "total_pyc_in_artifact": len(all_items),
                "source_less_pyc_pct_in_artifact": percent_value(len(items), len(all_items)),
                "python_tags": ";".join(sorted({item.python_tag for item in items if item.python_tag})),
                "top_level_paths": ";".join(top_level_paths(items)),
                "source_recoverable_pyc": source_recoverable,
                "source_recoverable_pct": percent_value(source_recoverable, len(items)),
                "dynamic_loading_indicator": scan_row.get("has_dynamic_loading", ""),
                "dynamic_load_hits": scan_row.get("dynamic_load_hits", ""),
                "keyword_categories": ";".join(categories),
                "security_keyword_indicator": "yes" if "security" in categories else "no",
            }
        )
    write_dict_rows(
        path,
        [
            "artifact",
            "package",
            "version",
            "artifact_type",
            "source_less_pyc",
            "total_pyc_in_artifact",
            "source_less_pyc_pct_in_artifact",
            "python_tags",
            "top_level_paths",
            "source_recoverable_pyc",
            "source_recoverable_pct",
            "dynamic_loading_indicator",
            "dynamic_load_hits",
            "keyword_categories",
            "security_keyword_indicator",
        ],
        rows,
    )


def write_source_less_keyword_categories_csv(path: Path, source_less: Sequence[ToolAnalysisResult]) -> None:
    pyc_counts: Counter[str] = Counter()
    artifact_groups: dict[str, set[str]] = {}
    for item in source_less:
        categories = keyword_categories_for_items([item])
        if not categories:
            categories = ["uncategorized"]
        for category in categories:
            pyc_counts[category] += 1
            artifact_groups.setdefault(category, set()).add(item.artifact)
    total = len(source_less)
    rows = [
        {
            "keyword_category": category,
            "pyc_files": count,
            "pct_source_less_pyc": percent_value(count, total),
            "artifacts": len(artifact_groups.get(category, set())),
        }
        for category, count in sorted(pyc_counts.items(), key=lambda entry: (-entry[1], entry[0]))
    ]
    write_dict_rows(path, ["keyword_category", "pyc_files", "pct_source_less_pyc", "artifacts"], rows)


def read_scan_rows(scan_csv: Path | None) -> dict[str, dict[str, str]]:
    if not scan_csv or not scan_csv.exists():
        return {}
    with scan_csv.open(newline="", encoding="utf-8") as handle:
        return {row.get("input", ""): row for row in csv.DictReader(handle) if row.get("input")}


def count_dynamic_artifacts(artifacts: set[str], scan_rows: dict[str, dict[str, str]]) -> int:
    return sum(
        1
        for artifact in artifacts
        if scan_rows.get(artifact, {}).get("has_dynamic_loading") == "True"
        or int(scan_rows.get(artifact, {}).get("dynamic_load_hits") or 0) > 0
    )


def count_keyword_artifacts(source_less: Sequence[ToolAnalysisResult]) -> int:
    return len(
        {
            item.artifact
            for item in source_less
            if "security" in keyword_categories_for_items([item])
        }
    )


KEYWORD_CATEGORIES: dict[str, tuple[str, ...]] = {
    "security": (
        "auth",
        "crypto",
        "crypt",
        "encrypt",
        "decrypt",
        "jwt",
        "oauth",
        "password",
        "secret",
        "secure",
        "security",
        "token",
        "tls",
        "ssl",
    ),
    "network": ("api", "client", "http", "https", "net", "proxy", "request", "rpc", "server", "socket", "url", "web"),
    "data": ("csv", "data", "database", "db", "etl", "json", "sql", "table", "xml", "yaml"),
    "ml": ("ai", "learn", "ml", "model", "numpy", "pandas", "torch", "tensorflow"),
    "testing": ("test", "pytest", "unittest"),
    "build": ("build", "compile", "dist", "pack", "setup", "wheel"),
    "plugin": ("addon", "extension", "plugin"),
    "cli": ("cli", "cmd", "command", "console"),
}


def keyword_categories_for_items(items: Sequence[ToolAnalysisResult]) -> list[str]:
    text = " ".join(
        " ".join([package_name_from_artifact(item.artifact), item.pyc_path])
        for item in items
    ).lower()
    tokens = {token for token in re.split(r"[^a-z0-9]+", text) if token}
    categories = [
        category
        for category, keywords in KEYWORD_CATEGORIES.items()
        if any(keyword in tokens for keyword in keywords)
    ]
    return sorted(categories)


def artifact_name_from_path(artifact: str) -> str:
    return Path(artifact).name


def package_version_from_artifact(artifact: str) -> tuple[str, str]:
    parts = Path(artifact).parts
    if "pypi" in parts:
        index = parts.index("pypi")
        package = parts[index + 1] if index + 1 < len(parts) else "unknown"
        version = parts[index + 2] if index + 2 < len(parts) else "unknown"
        return package, version
    return package_name_from_artifact(artifact), "unknown"


def package_name_from_artifact(artifact: str) -> str:
    parts = Path(artifact).parts
    if "pypi" in parts:
        index = parts.index("pypi")
        if index + 1 < len(parts):
            return parts[index + 1]
    if len(parts) >= 3:
        return parts[-3]
    return Path(artifact).stem


def top_level_paths(items: Sequence[ToolAnalysisResult], limit: int = 5) -> list[str]:
    counts = Counter(top_level_path(item.pyc_path) for item in items)
    return [path for path, _ in counts.most_common(limit) if path]


def top_level_path(path: str) -> str:
    parts = [part for part in scanner.normalize_path(path).split("/") if part]
    if not parts:
        return ""
    if parts[0].endswith(".dist-info") or parts[0].endswith(".egg-info"):
        return parts[0]
    if len(parts) >= 2 and parts[1] == "__pycache__":
        return parts[0]
    return parts[0]

def write_dict_rows(path: Path, fieldnames: Sequence[str], rows: Sequence[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def percent_value(numerator: int, denominator: int) -> str:
    if not denominator:
        return "0.00"
    return f"{(numerator / denominator) * 100:.2f}"


def write_csv(path: Path, results: Sequence[ToolAnalysisResult]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=TOOL_ANALYSIS_FIELDNAMES)
        writer.writeheader()
        writer.writerows(asdict(result) for result in results)


def write_summary_csv(path: Path, results: Sequence[ToolAnalysisResult]) -> None:
    summary = summarize(results)
    rows = [
        ("pyc_files", summary["pyc_files"]),
        ("source_present", summary["source_present"]),
        ("source_less", summary["source_less"]),
        ("runtime_magic", summary["runtime_magic"]),
        ("marshal_ok", summary["marshal_ok"]),
        ("dis_ok", summary["dis_ok"]),
        ("uncompyle6_ok", summary["uncompyle6_ok"]),
        ("decompyle3_ok", summary["decompyle3_ok"]),
        ("pylingual_ok", summary["pylingual_ok"]),
        ("level_0", summary["level_0"]),
        ("level_1", summary["level_1"]),
        ("level_2", summary["level_2"]),
        ("level_3", summary["level_3"]),
        ("level_4", summary["level_4"]),
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["metric", "value"])
        writer.writeheader()
        for metric, value in rows:
            writer.writerow({"metric": metric, "value": value})


def summarize(results: Sequence[ToolAnalysisResult]) -> dict[str, int]:
    return {
        "pyc_files": len(results),
        "source_present": sum(1 for item in results if item.source_present),
        "source_less": sum(1 for item in results if not item.source_present),
        "runtime_magic": sum(1 for item in results if item.magic_matches_runtime),
        "marshal_ok": sum(1 for item in results if item.stdlib_marshal == "ok"),
        "dis_ok": sum(1 for item in results if item.stdlib_dis == "ok"),
        "uncompyle6_ok": sum(1 for item in results if item.uncompyle6 == "ok"),
        "decompyle3_ok": sum(1 for item in results if item.decompyle3 == "ok"),
        "pylingual_ok": sum(1 for item in results if item.pylingual == "ok"),
        "level_0": sum(1 for item in results if item.overall_level == 0),
        "level_1": sum(1 for item in results if item.overall_level == 1),
        "level_2": sum(1 for item in results if item.overall_level == 2),
        "level_3": sum(1 for item in results if item.overall_level == 3),
        "level_4": sum(1 for item in results if item.overall_level == 4),
    }
