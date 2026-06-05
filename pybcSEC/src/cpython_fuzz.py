"""RQ3 CPython bytecode fuzzing support."""

from __future__ import annotations

import csv
import hashlib
import os
import pty
import re
import select
import shutil
import subprocess
import sys
import tarfile
import textwrap
import time
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
    "coverage_stats",
    "crash_dir",
    "timeout_dir",
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
    coverage_stats: str
    crash_dir: str
    timeout_dir: str
    report: str
    log: str
    duration: int
    workers: int
    status: str
    reason: str
    crashes: int
    timeouts: int


def version_dir_name(tag: str) -> str:
    version = tool_analysis.cpython_tag_version(tag)
    if version:
        parts = version.split(".")
        if len(parts) >= 2:
            return f"cpython-{parts[0]}.{parts[1]}"
    return tag


def rq3_root(path: Path) -> Path:
    if path.name in {"seeds", "unittest_seeds", "cpython_sources", "instrumented", "fuzz"}:
        return path.parent
    return path


def version_dir(root: Path, tag: str) -> Path:
    return rq3_root(root) / version_dir_name(tag)


def version_seed_dir(root: Path, tag: str) -> Path:
    return version_dir(root, tag) / "seeds"


def version_raw_seed_dir(root: Path, tag: str) -> Path:
    return version_dir(root, tag) / "unittest_seeds" / "raw"


def version_source_root(root: Path, tag: str) -> Path:
    return version_dir(root, tag) / "source"


def version_build_dir(root: Path, tag: str) -> Path:
    return version_dir(root, tag) / "instrumented"


def version_fuzz_dir(root: Path, tag: str) -> Path:
    return version_dir(root, tag) / "fuzz"


def legacy_seed_dir(out_dir: Path, tag: str) -> Path:
    root = rq3_root(out_dir)
    if out_dir.name == "seeds":
        return out_dir / tag
    return root / "seeds" / tag


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
        if out_dir.name == "seeds" and out_dir.parent.name.startswith("cpython-"):
            tag_dir = out_dir
        else:
            tag_dir = version_seed_dir(out_dir, tag)
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
        tag_out = version_seed_dir(out_dir, tag)
        existing_seeds = seeds_from_dir(
            tag_out,
            tag,
            artifact=f"cpython_unittest:{tag_out}",
            artifact_type="cpython_unittest_seed",
        )
        if not existing_seeds:
            old_tag_out = legacy_seed_dir(out_dir, tag)
            existing_seeds = seeds_from_dir(
                old_tag_out,
                tag,
                artifact=f"cpython_unittest:{old_tag_out}",
                artifact_type="cpython_unittest_seed",
            )
        if existing_seeds:
            seeds.extend(existing_seeds)
            print(f"[rq3-seed] {tag}: reused {len(existing_seeds)} compiled CPython unittest seeds")
            continue
        raw_dir = find_unittest_seed_dir(tag, raw_seed_root)
        if raw_dir is None:
            source_dir = find_cpython_source_dir(tag, cpython_source_root)
            if source_dir is None:
                status, reason, source_dir = prepare_cpython_source(
                    tag,
                    interpreter,
                    version_source_root(cpython_source_root, tag),
                    timeout,
                )
                if status == "ok":
                    print(f"[rq3-source] {tag}: prepared CPython source at {source_dir}")
                else:
                    print(f"[rq3-source] {tag}: source preparation {status} {reason}")
            if source_dir:
                raw_dir = version_raw_seed_dir(raw_seed_root, tag)
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
        for tag in fallback_tags:
            seeds.extend(generate_seed_corpus([tag], interpreters, version_seed_dir(out_dir, tag), timeout))
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
    if source_dir.exists():
        shutil.rmtree(source_dir, ignore_errors=True)

    source_root.mkdir(parents=True, exist_ok=True)
    archive = source_root / f"Python-{exact_version}.tgz"
    url = f"https://www.python.org/ftp/python/{exact_version}/Python-{exact_version}.tgz"
    try:
        extract_root = source_root / f"Python-{exact_version}"
        for attempt in range(2):
            if not archive.exists():
                download_cpython_archive(url, archive, timeout)
            if (extract_root / "Lib" / "test").is_dir():
                break
            try:
                with tarfile.open(archive) as tf:
                    safe_extractall(tf, source_root)
                break
            except (EOFError, tarfile.TarError, OSError):
                if attempt:
                    raise
                archive.unlink(missing_ok=True)
                shutil.rmtree(extract_root, ignore_errors=True)
        if extract_root.exists() and not source_dir.exists():
            extract_root.rename(source_dir)
    except Exception as exc:
        return "error", f"{type(exc).__name__}:{exc}", None

    if (source_dir / "Lib" / "test").is_dir():
        return "ok", url, source_dir
    return "error", f"missing Lib/test after extracting {archive}", None


def download_cpython_archive(url: str, archive: Path, timeout: int) -> None:
    part = archive.with_suffix(archive.suffix + ".part")
    part.unlink(missing_ok=True)
    print(f"[rq3-source] downloading {url}", flush=True)
    request = urllib.request.Request(url, headers={"User-Agent": "pybcSEC-study-tool/0.1"})
    with urllib.request.urlopen(request, timeout=max(30, timeout)) as response:
        with part.open("wb") as handle:
            shutil.copyfileobj(response, handle)
    part.replace(archive)


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
    root = rq3_root(raw_seed_root)
    candidates = [
        version_raw_seed_dir(root, tag),
        version_dir(root, tag) / "unittest_seeds",
        raw_seed_root / tag / "raw",
        raw_seed_root / tag,
        root / "unittest_seeds" / tag / "raw",
        root / "unittest_seeds" / tag,
    ]
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
    root = rq3_root(source_root)
    if not version:
        return None
    matches = [
        version_source_root(root, tag),
        version_source_root(root, tag) / f"cpython-{version}",
        source_root / tag,
        source_root / f"cpython-{version}",
        root / "cpython_sources" / tag,
        root / "cpython_sources" / f"cpython-{version}",
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
    root = rq3_root(raw_seed_root)
    if root.exists():
        for candidate in sorted(root.glob("cpython-*")):
            if not candidate.is_dir():
                continue
            tag = directory_name_to_tag(candidate.name)
            if not tag:
                continue
            source_has_tests = any((candidate / "source").glob("cpython-*/Lib/test/test_*.py"))
            if any((candidate / "seeds").glob("*.pyc")) or any((candidate / "unittest_seeds" / "raw").glob("*.py")) or source_has_tests:
                tags.append(tag)
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


def write_version_reports(data_dir: Path, seeds: Sequence[FuzzSeed], runs: Sequence[FuzzRun]) -> list[Path]:
    tags = sorted({seed.python_tag for seed in seeds} | {run.python_tag for run in runs})
    written: list[Path] = []
    for tag in tags:
        root = version_dir(data_dir / "rq3", tag)
        tag_seeds = [seed for seed in seeds if seed.python_tag == tag]
        tag_runs = [run for run in runs if run.python_tag == tag]
        seed_csv = root / "bytecode_seeds.csv"
        run_csv = root / "fuzz_runs.csv"
        summary_csv = root / "rq3_summary.csv"
        write_seed_csv(seed_csv, tag_seeds)
        write_run_csv(run_csv, tag_runs)
        write_summary_csv(summary_csv, tag_seeds, tag_runs)
        written.extend([seed_csv, run_csv, summary_csv])
    return written


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
                namespace = {"__name__": "pybcsec_rq3_seed"}
                exec(code, namespace, namespace)
                target = namespace.get("__pybcsec_seed__")
                if callable(target):
                    result = target()
                    close = getattr(result, "close", None)
                    if hasattr(result, "__await__") and callable(close):
                        close()
            """
        ),
        encoding="utf-8",
    )


def find_honggfuzz(explicit: Path | None = None) -> str | None:
    if explicit:
        return str(explicit) if explicit.exists() else None
    tool_root = Path(__file__).resolve().parents[1]
    env_root = Path(os.environ["PYBCSEC_HONGGFUZZ_HOME"]) if os.environ.get("PYBCSEC_HONGGFUZZ_HOME") else None
    if env_root:
        candidate = env_root / "honggfuzz"
        return str(candidate) if candidate.is_file() else None
    compiler = find_hfuzz_compiler()
    compiler_root = Path(compiler).resolve().parents[1] if compiler else None
    candidates = [
        env_root / "honggfuzz" if env_root else None,
        compiler_root / "honggfuzz" if compiler_root else None,
        tool_root / "honggfuzz",
        tool_root / "tools" / "honggfuzz",
        shutil.which("honggfuzz"),
    ]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return str(candidate)
    return None


def find_hfuzz_compiler() -> str | None:
    tool_root = Path(__file__).resolve().parents[1]
    env_root = Path(os.environ["PYBCSEC_HONGGFUZZ_HOME"]) if os.environ.get("PYBCSEC_HONGGFUZZ_HOME") else None
    if env_root:
        for candidate in (
            env_root / "hfuzz_cc" / "hfuzz-clang",
            env_root / "hfuzz-clang",
            env_root / "hfuzz_cc" / "hfuzz-gcc",
            env_root / "hfuzz-gcc",
        ):
            if candidate.is_file():
                return str(candidate)
        return None
    candidates = [
        tool_root / "hfuzz_cc" / "hfuzz-clang",
        tool_root / "tools" / "hfuzz_cc" / "hfuzz-clang",
        tool_root / "hfuzz-clang",
        tool_root / "tools" / "hfuzz-clang",
        shutil.which("hfuzz-clang"),
        shutil.which("hfuzz-gcc"),
    ]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return str(candidate)
    return None


def prepare_instrumented_interpreters(
    tags: Sequence[str],
    interpreters: dict[str, str | None],
    data_dir: Path,
    timeout: int,
) -> dict[str, str | None]:
    prepared: dict[str, str | None] = {}
    root = data_dir / "rq3"
    compiler = find_hfuzz_compiler()
    if not compiler:
        raise SystemExit(
            "hfuzz-clang/hfuzz-gcc not found. Build or copy honggfuzz compiler "
            "wrappers before running full RQ3 fuzzing; use smoke-rq3 for an "
            "uninstrumented workflow check."
        )

    for tag in sorted(set(tags)):
        base_interpreter = interpreters.get(tag)
        if not base_interpreter:
            prepared[tag] = None
            print(
                f"[rq3-build] {tag}: missing base interpreter; run pybcSEC prepare-analysis-env first",
                flush=True,
            )
            continue
        status, reason, source_dir = prepare_cpython_source(
            tag,
            base_interpreter,
            version_source_root(root, tag),
            timeout,
        )
        if status != "ok" or source_dir is None:
            prepared[tag] = None
            print(f"[rq3-build] {tag}: source preparation {status} {reason}", flush=True)
            continue
        interpreter = build_instrumented_cpython(tag, source_dir, version_build_dir(root, tag), compiler, timeout)
        prepared[tag] = interpreter
    return prepared


def build_instrumented_cpython(
    tag: str,
    source_dir: Path,
    build_dir: Path,
    compiler: str,
    timeout: int,
) -> str | None:
    source_dir = source_dir.resolve()
    build_dir = build_dir.resolve()
    python_bin = build_dir / "python"
    if python_bin.exists():
        if validate_instrumented_cpython(python_bin, timeout):
            print(f"[rq3-build] {tag}: using existing instrumented CPython {python_bin}", flush=True)
            return str(python_bin)
        print(f"[rq3-build] {tag}: existing instrumented CPython is incomplete; rebuilding", flush=True)
        shutil.rmtree(build_dir, ignore_errors=True)

    build_dir.mkdir(parents=True, exist_ok=True)
    configure = source_dir / "configure"
    if not configure.exists():
        print(f"[rq3-build] {tag}: missing configure script in {source_dir}", flush=True)
        return None

    print(f"[rq3-build] {tag}: configuring instrumented CPython with {compiler}", flush=True)
    env = os.environ.copy()
    env.update(
        {
            "CC": compiler,
            "CXX": compiler,
            "CFLAGS": "-O1 -g",
            "LDFLAGS": env.get("LDFLAGS", ""),
        }
    )
    configure_cmd = [
        str(configure),
        "--without-pymalloc",
        "--disable-shared",
        "--without-ensurepip",
    ]
    status, reason = run_build_step(configure_cmd, build_dir, env, max(timeout, 600))
    if status != "ok":
        print(f"[rq3-build] {tag}: configure {status} {reason}", flush=True)
        return None

    jobs = str(max(1, os.cpu_count() or 1))
    print(f"[rq3-build] {tag}: building instrumented CPython", flush=True)
    status, reason = run_build_step(["make", "-j", jobs], build_dir, env, max(timeout, 3600))
    if status != "ok":
        print(f"[rq3-build] {tag}: make {status} {reason}", flush=True)
        return None

    if python_bin.exists() and validate_instrumented_cpython(python_bin, timeout):
        print(f"[rq3-build] {tag}: built {python_bin}", flush=True)
        return str(python_bin)
    print(f"[rq3-build] {tag}: build completed but python binary is missing or incomplete", flush=True)
    return None


def validate_instrumented_cpython(python_bin: Path, timeout: int) -> bool:
    script = (
        "import hashlib, importlib.util, marshal, py_compile, tempfile; "
        "hashlib.md5(b'pybcsec').hexdigest(); "
        "compile('x = 1\\n', '<pybcsec-build-check>', 'exec')"
    )
    try:
        completed = subprocess.run(
            [str(python_bin), "-c", script],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=max(10, timeout),
            check=False,
            text=True,
            errors="replace",
        )
    except (subprocess.TimeoutExpired, OSError):
        return False
    return completed.returncode == 0


def run_build_step(
    command: Sequence[str],
    cwd: Path,
    env: dict[str, str],
    timeout: int,
) -> tuple[str, str]:
    log = cwd / "build.log"
    try:
        with log.open("a", encoding="utf-8", errors="replace") as handle:
            handle.write("$ " + " ".join(command) + "\n")
            completed = subprocess.run(
                command,
                cwd=cwd,
                env=env,
                stdout=handle,
                stderr=subprocess.STDOUT,
                timeout=timeout,
                check=False,
            )
    except subprocess.TimeoutExpired:
        return "timeout", f"timeout_after_{timeout}s log={log}"
    except OSError as exc:
        return "error", f"{type(exc).__name__}:{exc} log={log}"
    if completed.returncode == 0:
        return "ok", str(log)
    return f"exit_{completed.returncode}", str(log)


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

    hfuzz_options = honggfuzz_options(hfuzz)
    harness = data_dir / "rq3" / "harness.py"
    write_harness(harness)
    if interpreters is None:
        interpreters = tool_analysis.load_interpreter_environment(versions_csv, data_dir=data_dir)
    runs: list[FuzzRun] = []
    tags = sorted({seed.python_tag for seed in seeds if seed.python_tag != "unknown"})
    for tag in tags:
        input_dir = version_seed_dir(data_dir / "rq3", tag)
        if not input_dir.exists():
            input_dir = data_dir / "rq3" / "seeds" / tag
        interpreter = interpreters.get(tag)
        out_dir = version_fuzz_dir(data_dir / "rq3", tag)
        corpus_dir = out_dir / "corpus"
        coverage_stats = out_dir / "coverage_stats.csv"
        crash_dir = out_dir / "crashes"
        timeout_dir = out_dir / "timeouts"
        report = out_dir / "HONGGFUZZ.REPORT.TXT"
        log = out_dir / "honggfuzz.log"
        corpus_dir.mkdir(parents=True, exist_ok=True)
        crash_dir.mkdir(parents=True, exist_ok=True)
        timeout_dir.mkdir(parents=True, exist_ok=True)

        if not interpreter:
            run = FuzzRun(
                python_tag=tag,
                interpreter="",
                honggfuzz=hfuzz,
                input_dir=str(input_dir),
                corpus_dir=str(corpus_dir),
                coverage_stats=str(coverage_stats),
                crash_dir=str(crash_dir),
                timeout_dir=str(timeout_dir),
                report=str(report),
                log=str(log),
                duration=duration,
                workers=workers,
                status="unavailable_interpreter",
                reason=f"missing interpreter for {tag}",
                crashes=count_findings(crash_dir),
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
            str(crash_dir),
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
        if "--timeoutdir" in hfuzz_options:
            command[command.index("--extension"):command.index("--extension")] = ["--timeoutdir", str(timeout_dir)]
        if "--statsfile" in hfuzz_options:
            command[command.index("--"):command.index("--")] = ["--statsfile", str(coverage_stats)]
        if "--report" in hfuzz_options:
            command[command.index("--"):command.index("--")] = ["--report", str(report)]
        print(f"[rq3-fuzz] {tag}: seeds={len(list(input_dir.glob('*.pyc')))} duration={duration}s workers={workers} persistent=disabled")
        returncode: int | None = None
        coverage_lines: list[str] = []
        env = os.environ.copy()
        env["HFUZZ_DISABLE_PERSISTENT_AUTODETECT"] = "1"
        try:
            returncode, coverage_lines = run_honggfuzz_live(
                command,
                env=env,
                timeout=duration + timeout + 60,
            )
        except subprocess.TimeoutExpired:
            status = "timeout"
            reason = f"timeout_after_{duration + timeout + 60}s"
        except OSError as exc:
            status = "error"
            reason = f"{type(exc).__name__}:{exc}"
        crashes = count_findings(crash_dir)
        timeouts = count_findings(timeout_dir)
        if returncode is not None:
            status = classify_honggfuzz_status(returncode, crashes)
            reason = "" if status == "ok" else f"exit_{returncode}"
        write_compact_fuzz_log(
            log,
            tag=tag,
            command=command,
            input_dir=input_dir,
            corpus_dir=corpus_dir,
            coverage_stats=coverage_stats,
            crash_dir=crash_dir,
            timeout_dir=timeout_dir,
            report=report,
            duration=duration,
            workers=max(1, workers),
            status=status,
            reason=reason,
            crashes=crashes,
            timeouts=timeouts,
            returncode=returncode,
            coverage_lines=coverage_lines,
        )
        runs.append(
            FuzzRun(
                python_tag=tag,
                interpreter=interpreter,
                honggfuzz=hfuzz,
                input_dir=str(input_dir),
                corpus_dir=str(corpus_dir),
                coverage_stats=str(coverage_stats),
                crash_dir=str(crash_dir),
                timeout_dir=str(timeout_dir),
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


def honggfuzz_options(hfuzz: str) -> set[str]:
    try:
        completed = subprocess.run(
            [hfuzz, "--help"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=10,
            check=False,
            text=True,
            errors="replace",
        )
    except (subprocess.TimeoutExpired, OSError):
        return set()
    options: set[str] = set()
    for word in completed.stdout.split():
        if not word.startswith("--"):
            continue
        options.add(word.strip())
        options.add(word.split("|", 1)[0].strip())
    return options


def run_honggfuzz_live(
    command: Sequence[str],
    env: dict[str, str],
    timeout: int,
    sample_seconds: int = 60,
) -> tuple[int, list[str]]:
    master_fd, slave_fd = pty.openpty()
    coverage_lines: list[str] = []
    buffer = ""
    started = time.monotonic()
    process: subprocess.Popen[bytes] | None = None
    try:
        process = subprocess.Popen(
            list(command),
            env=env,
            stdout=slave_fd,
            stderr=slave_fd,
            stdin=subprocess.DEVNULL,
            close_fds=True,
        )
        os.close(slave_fd)
        slave_fd = -1
        while True:
            elapsed = time.monotonic() - started
            if process.poll() is not None:
                drain_pty(master_fd, coverage_lines, buffer, started, sample_seconds)
                break
            if elapsed > timeout:
                process.kill()
                raise subprocess.TimeoutExpired(command, timeout)
            ready, _, _ = select.select([master_fd], [], [], 0.2)
            if not ready:
                continue
            try:
                chunk = os.read(master_fd, 8192)
            except OSError:
                break
            if not chunk:
                continue
            os.write(sys.stdout.fileno(), chunk)
            buffer = capture_coverage_lines(buffer, chunk, coverage_lines, started, sample_seconds)
        return process.wait(), coverage_lines
    finally:
        if slave_fd != -1:
            os.close(slave_fd)
        os.close(master_fd)
        if process is not None and process.poll() is None:
            process.kill()


def drain_pty(
    master_fd: int,
    coverage_lines: list[str],
    buffer: str,
    started: float,
    sample_seconds: int,
) -> str:
    while True:
        ready, _, _ = select.select([master_fd], [], [], 0)
        if not ready:
            return buffer
        try:
            chunk = os.read(master_fd, 8192)
        except OSError:
            return buffer
        if not chunk:
            return buffer
        os.write(sys.stdout.fileno(), chunk)
        buffer = capture_coverage_lines(buffer, chunk, coverage_lines, started, sample_seconds)


def capture_coverage_lines(
    buffer: str,
    chunk: bytes,
    coverage_lines: list[str],
    started: float,
    sample_seconds: int,
) -> str:
    text = chunk.decode("utf-8", errors="replace")
    buffer += text.replace("\r", "\n")
    parts = buffer.split("\n")
    buffer = parts.pop() if parts else ""
    for raw in parts:
        line = strip_ansi(raw).strip()
        if "Sz:" in line and "Tm:" in line and "New:" in line and "Cur:" in line:
            elapsed = max(0, int(time.monotonic() - started))
            bucket = elapsed // max(1, sample_seconds)
            sampled = f"elapsed_minute={bucket} elapsed_seconds={elapsed} {line}"
            if coverage_lines and coverage_lines[-1].startswith(f"elapsed_minute={bucket} "):
                coverage_lines[-1] = sampled
            else:
                coverage_lines.append(sampled)
    return buffer[-4096:]


def strip_ansi(text: str) -> str:
    return re.sub(r"\x1b\[[0-?]*[ -/]*[@-~]", "", text)


def write_compact_fuzz_log(
    path: Path,
    tag: str,
    command: Sequence[str],
    input_dir: Path,
    corpus_dir: Path,
    coverage_stats: Path,
    crash_dir: Path,
    timeout_dir: Path,
    report: Path,
    duration: int,
    workers: int,
    status: str,
    reason: str,
    crashes: int,
    timeouts: int,
    returncode: int | None,
    coverage_lines: Sequence[str],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"python_tag={tag}",
        f"status={status}",
        f"reason={reason}",
        f"returncode={'' if returncode is None else returncode}",
        f"duration={duration}",
        f"workers={workers}",
        "persistent=disabled",
        f"input_dir={input_dir}",
        f"corpus_dir={corpus_dir}",
        f"coverage_stats={coverage_stats}",
        f"crash_dir={crash_dir}",
        f"timeout_dir={timeout_dir}",
        f"report={report}",
        f"crashes={crashes}",
        f"timeouts={timeouts}",
        "command=" + " ".join(str(item) for item in command),
    ]
    tail = report_tail(report)
    if tail:
        lines.append("")
        lines.append("[report_tail]")
        lines.extend(tail)
    if coverage_lines:
        lines.append("")
        lines.append("[coverage_by_minute]")
        lines.extend(coverage_lines)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def report_tail(path: Path, max_lines: int = 40) -> list[str]:
    if not path.exists():
        return []
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return []
    return lines[-max_lines:]


def classify_honggfuzz_status(returncode: int, crashes: int) -> str:
    if returncode == 0:
        return "ok"
    if returncode == 1 and crashes:
        return "ok"
    return f"exit_{returncode}"


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
