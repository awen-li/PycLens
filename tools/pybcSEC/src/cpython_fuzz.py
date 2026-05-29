"""RQ3 CPython bytecode fuzzing support."""

from __future__ import annotations

import csv
import hashlib
import shutil
import subprocess
import tarfile
import textwrap
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import scanner
import seed_extract
import tool_analysis


SEED_FIELDNAMES = [
    "seed",
    "artifact",
    "artifact_type",
    "pyc_path",
    "python_tag",
    "magic_number",
    "bytes",
]
RUN_FIELDNAMES = [
    "python_tag",
    "interpreter",
    "honggfuzz",
    "input_dir",
    "corpus_dir",
    "findings_dir",
    "report",
    "log",
    "duration",
    "workers",
    "status",
    "reason",
    "crashes",
    "timeouts",
]
SUMMARY_FIELDNAMES = ["metric", "value"]


@dataclass(frozen=True)
class FuzzSeed:
    seed: str
    artifact: str
    artifact_type: str
    pyc_path: str
    python_tag: str
    magic_number: str
    bytes: int


@dataclass(frozen=True)
class FuzzRun:
    python_tag: str
    interpreter: str
    honggfuzz: str
    input_dir: str
    corpus_dir: str
    findings_dir: str
    report: str
    log: str
    duration: int
    workers: int
    status: str
    reason: str
    crashes: int
    timeouts: int


def extract_seed_corpus(
    artifacts: Sequence[Path],
    out_dir: Path,
    limit: int | None = None,
) -> list[FuzzSeed]:
    seeds: list[FuzzSeed] = []
    out_dir.mkdir(parents=True, exist_ok=True)
    for artifact in artifacts:
        try:
            entries = list(scanner.iter_entries(artifact))
        except Exception as exc:
            print(f"[rq3-seed-error] {artifact} open_failed:{type(exc).__name__}:{exc}")
            continue
        for entry in entries:
            entry_path = scanner.normalize_path(entry.path)
            if entry.is_dir or not entry_path.endswith(".pyc") or not entry.data:
                continue
            digest = hashlib.sha256(
                str(artifact).encode("utf-8") + b"\0" + entry_path.encode("utf-8") + b"\0" + entry.data
            ).hexdigest()[:16]
            tag = scanner.pyc_python_tag(entry_path)
            seed_dir = out_dir / tag
            seed_dir.mkdir(parents=True, exist_ok=True)
            seed_name = f"{Path(entry_path).stem}_{digest}.pyc"
            seed_path = seed_dir / seed_name
            if not seed_path.exists():
                seed_path.write_bytes(entry.data)
            seeds.append(
                FuzzSeed(
                    seed=str(seed_path),
                    artifact=str(artifact),
                    artifact_type=scanner.input_type(artifact),
                    pyc_path=entry_path,
                    python_tag=tag,
                    magic_number=scanner.pyc_magic(entry.data) or "",
                    bytes=len(entry.data),
                )
            )
            if limit and len(seeds) >= limit:
                return seeds
    return seeds


def generate_seed_corpus(
    tags: Sequence[str],
    interpreters: dict[str, str | None],
    out_dir: Path,
    timeout: int,
) -> list[FuzzSeed]:
    seeds: list[FuzzSeed] = []
    out_dir.mkdir(parents=True, exist_ok=True)
    for tag in sorted(set(tags)):
        interpreter = interpreters.get(tag)
        if not interpreter:
            print(f"[rq3-seed] {tag}: missing interpreter; skipping generated seeds")
            continue
        tag_dir = out_dir / tag
        tag_dir.mkdir(parents=True, exist_ok=True)
        status, reason = run_seed_generator(interpreter, tag_dir, timeout)
        if status != "ok":
            print(f"[rq3-seed] {tag}: {status} {reason}")
            continue
        tag_seeds = []
        for seed_path in sorted(tag_dir.glob("*.pyc")):
            data = seed_path.read_bytes()
            tag_seeds.append(
                FuzzSeed(
                    seed=str(seed_path),
                    artifact="generated",
                    artifact_type="generated",
                    pyc_path=seed_path.name,
                    python_tag=tag,
                    magic_number=scanner.pyc_magic(data) or "",
                    bytes=len(data),
                )
            )
        seeds.extend(tag_seeds)
        print(f"[rq3-seed] {tag}: generated {len(tag_seeds)} seeds")
    return seeds


def build_seed_corpus(
    tags: Sequence[str],
    interpreters: dict[str, str | None],
    out_dir: Path,
    timeout: int,
    raw_seed_root: Path,
    cpython_source_root: Path,
) -> list[FuzzSeed]:
    seeds: list[FuzzSeed] = []
    fallback_tags: list[str] = []
    for tag in sorted(set(tags)):
        interpreter = interpreters.get(tag)
        if not interpreter:
            print(f"[rq3-seed] {tag}: missing interpreter; skipping seeds")
            continue
        tag_out = out_dir / tag
        existing_seeds = seeds_from_dir(
            tag_out,
            tag,
            artifact=f"cpython_unittest:{tag_out}",
            artifact_type="cpython_unittest_seed",
        )
        if existing_seeds:
            seeds.extend(existing_seeds)
            print(f"[rq3-seed] {tag}: reused {len(existing_seeds)} compiled CPython unittest seeds from {tag_out}")
            continue
        raw_dir = find_unittest_seed_dir(tag, raw_seed_root)
        if raw_dir is None:
            source_dir = find_cpython_source_dir(tag, cpython_source_root)
            if source_dir is None:
                status, reason, source_dir = prepare_cpython_source(tag, interpreter, cpython_source_root, timeout)
                if status == "ok":
                    print(f"[rq3-source] {tag}: prepared CPython source at {source_dir}")
                else:
                    print(f"[rq3-source] {tag}: source preparation {status} {reason}")
            if source_dir:
                raw_dir = raw_seed_root / tag / "raw"
                try:
                    extracted = seed_extract.extract_cpython_test_seeds(source_dir, raw_dir)
                    print(f"[rq3-seed] {tag}: extracted {extracted.cases} CPython unittest seeds from {source_dir}")
                except Exception as exc:
                    print(f"[rq3-seed] {tag}: unittest extraction failed {type(exc).__name__}:{exc}")
        if raw_dir:
            status, reason = compile_source_seed_corpus(interpreter, raw_dir, tag_out, max(300, timeout))
            tag_seeds = seeds_from_dir(
                tag_out,
                tag,
                artifact=f"cpython_unittest:{raw_dir}",
                artifact_type="cpython_unittest_seed",
            )
            if status == "ok":
                seeds.extend(tag_seeds)
                print(f"[rq3-seed] {tag}: compiled {len(tag_seeds)} CPython unittest seeds from {raw_dir}")
                continue
            if tag_seeds:
                seeds.extend(tag_seeds)
                print(f"[rq3-seed] {tag}: using {len(tag_seeds)} partially compiled CPython unittest seeds ({status} {reason})")
                continue
            print(f"[rq3-seed] {tag}: CPython unittest seed compile {status} {reason}")
        fallback_tags.append(tag)
    if fallback_tags:
        print(f"[rq3-seed] generated fallback seeds for: {', '.join(fallback_tags)}")
        seeds.extend(generate_seed_corpus(fallback_tags, interpreters, out_dir / "generated", timeout))
    return seeds


def prepare_cpython_source(
    tag: str,
    interpreter: str,
    source_root: Path,
    timeout: int,
) -> tuple[str, str, Path | None]:
    exact_version = interpreter_version(interpreter, timeout)
    if not exact_version:
        exact_version = tool_analysis.cpython_tag_version(tag)
    if not exact_version:
        return "unsupported_tag", tag, None

    source_dir = source_root / f"cpython-{exact_version}"
    if (source_dir / "Lib" / "test").is_dir():
        return "ok", "exists", source_dir

    source_root.mkdir(parents=True, exist_ok=True)
    archive = source_root / f"Python-{exact_version}.tgz"
    url = f"https://www.python.org/ftp/python/{exact_version}/Python-{exact_version}.tgz"
    try:
        if not archive.exists():
            print(f"[rq3-source] {tag}: downloading {url}")
            request = urllib.request.Request(url, headers={"User-Agent": "pybcSEC-study-tool/0.1"})
            with urllib.request.urlopen(request, timeout=max(30, timeout)) as response:
                with archive.open("wb") as handle:
                    shutil.copyfileobj(response, handle)
        extract_root = source_root / f"Python-{exact_version}"
        if not (extract_root / "Lib" / "test").is_dir():
            with tarfile.open(archive) as tf:
                safe_extractall(tf, source_root)
        if extract_root.exists() and not source_dir.exists():
            extract_root.rename(source_dir)
    except Exception as exc:
        return "error", f"{type(exc).__name__}:{exc}", None

    if (source_dir / "Lib" / "test").is_dir():
        return "ok", url, source_dir
    return "error", f"missing Lib/test after extracting {archive}", None


def interpreter_version(interpreter: str, timeout: int) -> str:
    try:
        completed = subprocess.run(
            [interpreter, "-c", "import sys; print('.'.join(map(str, sys.version_info[:3])))"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=max(10, timeout),
            check=False,
            text=True,
            errors="replace",
        )
    except (subprocess.TimeoutExpired, OSError):
        return ""
    if completed.returncode != 0:
        return ""
    return completed.stdout.strip()


def safe_extractall(archive: tarfile.TarFile, destination: Path) -> None:
    root = destination.resolve()
    for member in archive.getmembers():
        target = (destination / member.name).resolve()
        if not str(target).startswith(str(root) + "/") and target != root:
            raise RuntimeError(f"unsafe archive member: {member.name}")
    archive.extractall(destination)


def find_unittest_seed_dir(tag: str, raw_seed_root: Path) -> Path | None:
    candidates = [raw_seed_root / tag / "raw", raw_seed_root / tag]
    version = tool_analysis.cpython_tag_version(tag)
    if version:
        candidates.extend(sorted(raw_seed_root.glob(f"cpython-{version}*/raw")))
        candidates.extend(sorted(raw_seed_root.glob(f"cpython-{version}*")))
    for candidate in candidates:
        if candidate.is_dir() and any(candidate.glob("*.py")):
            return candidate
    return None


def find_cpython_source_dir(tag: str, source_root: Path) -> Path | None:
    version = tool_analysis.cpython_tag_version(tag)
    if not version or not source_root.exists():
        return None
    matches = [
        source_root / tag,
        source_root / f"cpython-{version}",
        *sorted(source_root.glob(f"cpython-{version}*")),
    ]
    for match in matches:
        candidates = [match, match / "targets" / "src", match / "src"]
        for candidate in candidates:
            if (candidate / "Lib" / "test").is_dir():
                return candidate
    return None


def discover_unittest_seed_tags(raw_seed_root: Path, compiled_seed_root: Path, cpython_source_root: Path) -> list[str]:
    tags = []
    for root, pattern, file_pattern in (
        (raw_seed_root, "cpython-*", "*.py"),
        (compiled_seed_root, "cpython-*", "*.pyc"),
        (cpython_source_root, "cpython-*", "Lib/test/test_*.py"),
    ):
        if not root.exists():
            continue
        for seed_dir in sorted(root.glob(pattern)):
            if not seed_dir.is_dir() or not any(seed_dir.glob(file_pattern)):
                continue
            tag = directory_name_to_tag(seed_dir.name)
            if tag:
                tags.append(tag)
    return sorted(set(tags))


def discover_cpython_source_dirs(source_root: Path) -> dict[str, Path]:
    source_dirs: dict[str, Path] = {}
    if not source_root.exists():
        return source_dirs
    for path in sorted(source_root.glob("cpython-*")):
        tag = directory_name_to_tag(path.name)
        if not tag:
            continue
        source_dir = find_cpython_source_dir(tag, source_root)
        if source_dir:
            source_dirs[tag] = source_dir
    return source_dirs


def extract_unittest_seed_sources(source_root: Path, raw_seed_root: Path) -> dict[str, seed_extract.ExtractSeedResult]:
    results = {}
    for tag, source_dir in discover_cpython_source_dirs(source_root).items():
        out_dir = raw_seed_root / tag / "raw"
        result = seed_extract.extract_cpython_test_seeds(source_dir, out_dir)
        results[tag] = result
    return results


def directory_name_to_tag(name: str) -> str:
    raw = name.removeprefix("cpython-")
    parts = raw.split(".")
    if len(parts) >= 2 and parts[0].isdigit() and parts[1].isdigit():
        return f"cpython-{parts[0]}{parts[1]}"
    if raw.isdigit():
        return f"cpython-{raw}"
    return ""


def version_to_tag(version: str) -> str:
    value = version.strip().lower().removeprefix("python").removeprefix("cpython-")
    if "." in value:
        parts = value.split(".")
        if len(parts) >= 2 and parts[0].isdigit() and parts[1].isdigit():
            return f"cpython-{parts[0]}{parts[1]}"
    if value.isdigit():
        return f"cpython-{value}"
    return version


def compile_source_seed_corpus(
    interpreter: str,
    raw_dir: Path,
    out_dir: Path,
    timeout: int,
) -> tuple[str, str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    script = textwrap.dedent(
        """\
        import hashlib
        import importlib.util
        import marshal
        import os
        import struct
        import sys
        from pathlib import Path

        raw_dir = Path(sys.argv[1])
        out_dir = Path(sys.argv[2])
        compiled = 0
        failed = 0

        def executable_seed_source(text):
            target = "__pybcsec_seed__"
            if f"seed-target: {target}" in text:
                return text.rstrip() + f"\\n\\nif __name__ == '__main__':\\n    {target}()\\n"
            return text

        def write_pyc(code, out):
            with out.open("wb") as handle:
                handle.write(importlib.util.MAGIC_NUMBER)
                handle.write(struct.pack("<I", 0))
                handle.write(struct.pack("<I", 0))
                handle.write(struct.pack("<I", 0))
                marshal.dump(code, handle)

        for path in sorted(raw_dir.glob("*.py")):
            digest = hashlib.sha256(str(path).encode("utf-8")).hexdigest()[:16]
            out = out_dir / f"{path.stem}_{digest}.pyc"
            if out.exists():
                compiled += 1
                continue
            try:
                source = executable_seed_source(path.read_text(encoding="utf-8"))
                code = compile(source, str(path), "exec")
                write_pyc(code, out)
                compiled += 1
            except Exception:
                failed += 1
        print(f"compiled={compiled} failed={failed}")
        if compiled == 0:
            raise SystemExit("no bytecode seeds were compiled")
        """
    )
    try:
        completed = subprocess.run(
            [interpreter, "-c", script, str(raw_dir), str(out_dir)],
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


def seeds_from_dir(seed_dir: Path, tag: str, artifact: str, artifact_type: str) -> list[FuzzSeed]:
    seeds = []
    for seed_path in sorted(seed_dir.glob("*.pyc")):
        data = seed_path.read_bytes()
        seeds.append(
            FuzzSeed(
                seed=str(seed_path),
                artifact=artifact,
                artifact_type=artifact_type,
                pyc_path=seed_path.name,
                python_tag=tag,
                magic_number=scanner.pyc_magic(data) or "",
                bytes=len(data),
            )
        )
    return seeds


def run_seed_generator(interpreter: str, out_dir: Path, timeout: int) -> tuple[str, str]:
    script = textwrap.dedent(
        """\
        import hashlib
        import importlib.util
        import marshal
        import struct
        import sys
        from pathlib import Path

        out_dir = Path(sys.argv[1])
        snippets = {
            "straightline": "x = 1\\ny = x + 2\\nz = y * 3\\n",
            "branches": "def f(x):\\n    if x % 2:\\n        return x + 1\\n    return x - 1\\n",
            "loop": "def f(n):\\n    total = 0\\n    for i in range(n):\\n        total += i\\n    return total\\n",
            "exceptions": "def f(x):\\n    try:\\n        return 10 // x\\n    except ZeroDivisionError:\\n        return None\\n",
            "classes": "class C:\\n    def __init__(self, x):\\n        self.x = x\\n    def value(self):\\n        return self.x\\n",
            "comprehensions": "xs = [i * i for i in range(20) if i % 3]\\nys = {str(i): i for i in xs}\\n",
            "closures": "def outer(x):\\n    def inner(y):\\n        return x + y\\n    return inner\\n",
            "async_defs": "async def f(x):\\n    return x\\n",
            "pattern": "def f(x):\\n    match x:\\n        case 0:\\n            return 'zero'\\n        case _:\\n            return 'other'\\n",
        }

        def write_pyc(name, code):
            digest = hashlib.sha256(name.encode()).hexdigest()[:12]
            path = out_dir / f"{name}_{digest}.pyc"
            with path.open("wb") as handle:
                handle.write(importlib.util.MAGIC_NUMBER)
                handle.write(struct.pack("<I", 0))
                handle.write(struct.pack("<I", 0))
                handle.write(struct.pack("<I", 0))
                marshal.dump(code, handle)

        written = 0
        for name, source in snippets.items():
            try:
                code = compile(source, f"<pybcsec-rq3-{name}>", "exec")
            except SyntaxError:
                continue
            write_pyc(name, code)
            written += 1
        print(written)
        """
    )
    try:
        completed = subprocess.run(
            [interpreter, "-c", script, str(out_dir)],
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
        return "ok", completed.stdout.strip()
    return f"exit_{completed.returncode}", compact_reason(completed.stderr) or compact_reason(completed.stdout)


def write_seed_csv(path: Path, seeds: Sequence[FuzzSeed]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=SEED_FIELDNAMES)
        writer.writeheader()
        writer.writerows(seed.__dict__ for seed in seeds)


def write_run_csv(path: Path, runs: Sequence[FuzzRun]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=RUN_FIELDNAMES)
        writer.writeheader()
        writer.writerows(run.__dict__ for run in runs)


def write_summary_csv(path: Path, seeds: Sequence[FuzzSeed], runs: Sequence[FuzzRun]) -> None:
    by_tag: dict[str, int] = {}
    for seed in seeds:
        by_tag[seed.python_tag] = by_tag.get(seed.python_tag, 0) + 1
    rows = [
        {"metric": "seeds", "value": str(len(seeds))},
        {"metric": "tags", "value": str(len(by_tag))},
        {"metric": "runs", "value": str(len(runs))},
        {"metric": "completed_runs", "value": str(sum(1 for run in runs if run.status == "ok"))},
        {"metric": "crashes", "value": str(sum(run.crashes for run in runs))},
        {"metric": "timeouts", "value": str(sum(run.timeouts for run in runs))},
    ]
    rows.extend({"metric": f"seeds_{tag}", "value": str(count)} for tag, count in sorted(by_tag.items()))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=SUMMARY_FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def read_version_tags(path: Path) -> list[str]:
    if not path.exists():
        return []
    tags: list[str] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            tag = row.get("python_tag", "")
            if tag.startswith("cpython-"):
                tags.append(tag)
    return sorted(set(tags))


def write_harness(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        textwrap.dedent(
            """\
            import dis
            import importlib.machinery
            import marshal
            import sys

            path = sys.argv[1]
            data = open(path, "rb").read()

            code = None
            try:
                code = importlib.machinery.SourcelessFileLoader("pybcsec_rq3_seed", path).get_code("pybcsec_rq3_seed")
            except BaseException:
                for offset in (16, 12, 8):
                    try:
                        obj = marshal.loads(data[offset:])
                    except BaseException:
                        continue
                    if hasattr(obj, "co_code"):
                        code = obj
                        break

            if code is not None:
                list(dis.Bytecode(code))
                marshal.dumps(code)
            """
        ),
        encoding="utf-8",
    )


def find_honggfuzz(explicit: Path | None = None) -> str | None:
    if explicit:
        return str(explicit) if explicit.exists() else None
    tool_root = Path(__file__).resolve().parents[1]
    candidates = [
        tool_root / "honggfuzz",
        tool_root / "tools" / "honggfuzz",
        shutil.which("honggfuzz"),
    ]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return str(candidate)
    return None


def run_fuzz_campaigns(
    seeds: Sequence[FuzzSeed],
    data_dir: Path,
    versions_csv: Path,
    workers: int,
    duration: int,
    timeout: int,
    honggfuzz_path: Path | None = None,
    interpreters: dict[str, str | None] | None = None,
) -> list[FuzzRun]:
    hfuzz = find_honggfuzz(honggfuzz_path)
    if not hfuzz:
        print("[rq3] honggfuzz not found; seed corpus was prepared but fuzzing was not run")
        return []

    harness = data_dir / "rq3" / "harness.py"
    write_harness(harness)
    if interpreters is None:
        interpreters = tool_analysis.load_interpreter_environment(versions_csv, data_dir=data_dir)
    runs: list[FuzzRun] = []
    tags = sorted({seed.python_tag for seed in seeds if seed.python_tag != "unknown"})
    for tag in tags:
        input_dir = data_dir / "rq3" / "seeds" / tag
        interpreter = interpreters.get(tag)
        out_dir = data_dir / "rq3" / "fuzz" / tag
        corpus_dir = out_dir / "corpus"
        findings_dir = out_dir / "findings"
        report = out_dir / "HONGGFUZZ.REPORT.TXT"
        log = out_dir / "honggfuzz.log"
        corpus_dir.mkdir(parents=True, exist_ok=True)
        findings_dir.mkdir(parents=True, exist_ok=True)

        if not interpreter:
            run = FuzzRun(
                python_tag=tag,
                interpreter="",
                honggfuzz=hfuzz,
                input_dir=str(input_dir),
                corpus_dir=str(corpus_dir),
                findings_dir=str(findings_dir),
                report=str(report),
                log=str(log),
                duration=duration,
                workers=workers,
                status="unavailable_interpreter",
                reason=f"missing interpreter for {tag}",
                crashes=count_findings(findings_dir),
                timeouts=0,
            )
            runs.append(run)
            print(f"[rq3-fuzz] {tag}: unavailable_interpreter")
            continue

        command = [
            hfuzz,
            "-i",
            str(input_dir),
            "-o",
            str(corpus_dir),
            "--crashdir",
            str(findings_dir),
            "--extension",
            "pyc",
            "--run_time",
            str(duration),
            "--timeout",
            str(timeout),
            "-n",
            str(max(1, workers)),
            "--",
            interpreter,
            str(harness),
            "___FILE___",
        ]
        print(f"[rq3-fuzz] {tag}: seeds={len(list(input_dir.glob('*.pyc')))} duration={duration}s workers={workers}")
        try:
            with log.open("w", encoding="utf-8", errors="replace") as log_handle:
                completed = subprocess.run(
                    command,
                    stdout=log_handle,
                    stderr=subprocess.STDOUT,
                    timeout=duration + timeout + 60,
                    check=False,
                    text=True,
                    errors="replace",
                )
            status = "ok" if completed.returncode in (0, 1) else f"exit_{completed.returncode}"
            reason = ""
        except subprocess.TimeoutExpired:
            status = "timeout"
            reason = f"timeout_after_{duration + timeout + 60}s"
        except OSError as exc:
            status = "error"
            reason = f"{type(exc).__name__}:{exc}"
        crashes = count_findings(findings_dir)
        timeouts = count_timeout_findings(findings_dir)
        runs.append(
            FuzzRun(
                python_tag=tag,
                interpreter=interpreter,
                honggfuzz=hfuzz,
                input_dir=str(input_dir),
                corpus_dir=str(corpus_dir),
                findings_dir=str(findings_dir),
                report=str(report),
                log=str(log),
                duration=duration,
                workers=workers,
                status=status,
                reason=reason,
                crashes=crashes,
                timeouts=timeouts,
            )
        )
        print(f"[rq3-fuzz] {tag}: status={status} crashes={crashes} timeouts={timeouts}")
    return runs


def count_findings(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for item in path.iterdir() if item.is_file())


def count_timeout_findings(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for item in path.iterdir() if item.is_file() and "timeout" in item.name.lower())


def compact_reason(text: str, limit: int = 240) -> str:
    compact = " ".join((text or "").split())
    if len(compact) > limit:
        return compact[: limit - 3] + "..."
    return compact
