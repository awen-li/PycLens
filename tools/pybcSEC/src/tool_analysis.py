"""Evaluate practical analyzability of packaged Python bytecode artifacts."""

from __future__ import annotations

import csv
import dis
import importlib.util
import json
import marshal
import os
import shutil
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
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
    "pycdc",
    "pycdc_reason",
    "pycdc_level",
    "pylingual",
    "pylingual_reason",
    "pylingual_level",
    "overall_level",
    "overall_label",
    "error",
]
OPTIONAL_TOOLS = ("uncompyle6", "decompyle3", "pycdc", "pylingual")
DECOMPILER_TOOLS = OPTIONAL_TOOLS
PER_INTERPRETER_TOOLS = ("uncompyle6", "decompyle3")
GLOBAL_TOOLS = ("pycdc", "pylingual")


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
    pycdc: str = "unavailable"
    pycdc_reason: str = ""
    pycdc_level: int = 0
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


def analyze_artifacts(
    artifacts: Sequence[Path],
    workers: int,
    external_timeout: int,
    interpreters: dict[str, str | None],
    tool_envs: dict[str, dict[str, str | None]],
) -> list[ToolAnalysisResult]:
    selected_tools = available_tools()
    print(
        "tool analysis inputs: artifacts={artifacts}, workers={workers}, optional_tools={tools}".format(
            artifacts=len(artifacts),
            workers=max(1, workers),
            tools=",".join(f"{tool}:{'yes' if selected_tools[tool] else 'no'}" for tool in OPTIONAL_TOOLS),
        )
    )
    if not artifacts:
        return []

    if workers <= 1:
        results: list[ToolAnalysisResult] = []
        for index, artifact in enumerate(artifacts, start=1):
            artifact_results = analyze_artifact(artifact, selected_tools, interpreters, tool_envs, external_timeout)
            results.extend(artifact_results)
            print_progress(index, len(artifacts), artifact, artifact_results)
        return results

    results = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(analyze_artifact, artifact, selected_tools, interpreters, tool_envs, external_timeout): (index, artifact)
            for index, artifact in enumerate(artifacts, start=1)
        }
        completed = 0
        for future in as_completed(futures):
            index, artifact = futures[future]
            artifact_results = future.result()
            results.extend(artifact_results)
            completed += 1
            print_progress(completed, len(artifacts), artifact, artifact_results)
    return results


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
        f"[tool-analysis {completed}/{total}] pyc={pyc_count} marshal_ok={marshal_ok} "
        f"dis_ok={dis_ok} pylingual_ok={pylingual_ok} failed={failed} {levels} latest={artifact}"
    )


def available_tools() -> dict[str, str | None]:
    return {tool: shutil.which(tool) for tool in OPTIONAL_TOOLS}


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
            tag = tag_from_interpreter(interpreter) or canonical_analysis_tag(row.get("python_tag", ""))
            if not tag or tag == "unknown" or not supported_cpython_analysis_tag(tag):
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
    for candidate in candidates:
        if candidate is None:
            continue
        path = Path(candidate)
        if path.exists():
            return str(path)
        if isinstance(candidate, str):
            return candidate
    return None


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


def prepare_analysis_environment(
    data_dir: Path,
    versions_csv: Path,
    timeout: int,
) -> Path:
    interpreters = load_interpreter_environment(versions_csv, data_dir=data_dir)
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
        executable = shutil.which(tool)
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
    if tool == "pycdc":
        return command_version([executable])
    if tool == "pylingual":
        help_text = command_version([executable, "--help"])
        if help_text.startswith("Usage: pylingual"):
            return "installed (version unavailable)"
        return help_text
    return command_version([executable, "--version"])


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
    apt = shutil.which("apt-get")
    if apt:
        status, reason = apt_install_cpython(apt, version, timeout)
        if status == "ok":
            return status, reason
    uv = shutil.which("uv")
    if uv:
        status, reason = run_installer([uv, "python", "install", version], timeout)
        if status == "ok":
            return status, reason
    pyenv = shutil.which("pyenv")
    if pyenv:
        install_version = pyenv_install_version(pyenv, version, timeout)
        if install_version:
            return run_installer([pyenv, "install", "-s", install_version], timeout)
        return "installer_failed", f"pyenv has no installable version for {version}"
    return "installer_unavailable", f"install {scanner.python_tag_to_executable(tag)} or install apt/uv/pyenv"


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
    executable = env_dir / "bin" / tool
    if executable.exists():
        return "ok", "exists"
    pip = env_dir / "bin" / "pip"
    try:
        completed = subprocess.run(
            [str(pip), "install", tool],
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


def analyze_artifact(
    artifact: Path,
    selected_tools: dict[str, str | None],
    interpreters: dict[str, str | None],
    tool_envs: dict[str, dict[str, str | None]],
    external_timeout: int,
) -> list[ToolAnalysisResult]:
    try:
        entries = list(scanner.iter_entries(artifact))
    except Exception as exc:
        return [
            ToolAnalysisResult(
                artifact=str(artifact),
                artifact_type=scanner.input_type(artifact),
                pyc_path="",
                python_tag="",
                magic_number="",
                magic_matches_runtime=False,
                source_present=False,
                stdlib_marshal="error",
                stdlib_marshal_reason=f"open_failed:{type(exc).__name__}:{exc}",
                stdlib_marshal_level=0,
                stdlib_dis="error",
                stdlib_dis_reason=f"open_failed:{type(exc).__name__}:{exc}",
                stdlib_dis_level=0,
                error=f"open_failed:{type(exc).__name__}:{exc}",
            )
        ]

    py_paths = {scanner.normalize_path(entry.path) for entry in entries if not entry.is_dir and entry.path.endswith(".py")}
    results = []
    for entry in entries:
        entry_path = scanner.normalize_path(entry.path)
        if entry.is_dir or not entry_path.endswith(".pyc"):
            continue
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
) -> ToolAnalysisResult:
    magic_number = scanner.pyc_magic(data) or ""
    source_present = any(candidate in py_paths for candidate in scanner.module_source_candidates(pyc_path))
    tag = python_tag(pyc_path)

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


def python_tag(pyc_path: str) -> str:
    name = Path(pyc_path).name
    parts = name.split(".")
    for part in parts:
        tag = canonical_analysis_tag(part)
        if tag:
            return tag
    return ""


def canonical_analysis_tag(value: str) -> str:
    if value.startswith("cpython-"):
        raw = value.removeprefix("cpython-")
        digits = []
        for char in raw:
            if not char.isdigit():
                break
            digits.append(char)
        if len(digits) in (2, 3):
            return "cpython-" + "".join(digits)
    if value.startswith("pypy-"):
        raw = value.removeprefix("pypy-")
        digits = []
        for char in raw:
            if not char.isdigit():
                break
            digits.append(char)
        if len(digits) in (2, 3):
            return "pypy-" + "".join(digits)
    return ""


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
    return int(minor) >= 6


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
    available_decompilers = [tool for tool, executable in selected_tools.items() if executable]
    if len(successful_decompilers) == len(available_decompilers):
        return 4, "fully_decompilable"
    return 3, "partially_decompilable"


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
        ("pycdc_ok", summary["pycdc_ok"]),
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
        "pycdc_ok": sum(1 for item in results if item.pycdc == "ok"),
        "pylingual_ok": sum(1 for item in results if item.pylingual == "ok"),
        "level_0": sum(1 for item in results if item.overall_level == 0),
        "level_1": sum(1 for item in results if item.overall_level == 1),
        "level_2": sum(1 for item in results if item.overall_level == 2),
        "level_3": sum(1 for item in results if item.overall_level == 3),
        "level_4": sum(1 for item in results if item.overall_level == 4),
    }
