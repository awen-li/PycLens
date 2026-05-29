#!/usr/bin/env python3
"""Scan Python package artifacts for bytecode evidence.

The scanner accepts extracted package directories and common package archives
(.whl/.zip/.tar/.tar.gz/.tgz).  It reports whether each input contains Python
bytecode artifacts, source files, source-less bytecode candidates, and static
patterns commonly used to load bytecode or marshalled code objects.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import struct
import tarfile
import zipfile
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterator, Sequence


DYNAMIC_LOAD_PATTERNS: Sequence[tuple[str, re.Pattern[str]]] = (
    ("marshal", re.compile(r"\bmarshal\s*\.")),
    ("marshal.loads", re.compile(r"\bmarshal\s*\.\s*loads\s*\(")),
    ("importlib", re.compile(r"\bimportlib\b")),
    ("SourcelessFileLoader", re.compile(r"\bSourcelessFileLoader\b")),
    ("exec", re.compile(r"\bexec\s*\(")),
    ("eval", re.compile(r"\beval\s*\(")),
    ("types.CodeType", re.compile(r"\btypes\s*\.\s*CodeType\b|\bCodeType\s*\(")),
)


@dataclass
class DynamicHit:
    path: str
    pattern: str


@dataclass
class ScanResult:
    input: str
    input_type: str
    files_total: int = 0
    py_files: int = 0
    pyc_files: int = 0
    pycache_dirs: int = 0
    source_less_pyc: int = 0
    magic_numbers: dict[str, int] = field(default_factory=dict)
    dynamic_load_hits: list[DynamicHit] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    @property
    def has_bytecode(self) -> bool:
        return self.pyc_files > 0 or self.pycache_dirs > 0

    @property
    def has_dynamic_loading(self) -> bool:
        return bool(self.dynamic_load_hits)

    def to_summary_row(self) -> dict[str, object]:
        return {
            "input": self.input,
            "input_type": self.input_type,
            "files_total": self.files_total,
            "py_files": self.py_files,
            "pyc_files": self.pyc_files,
            "pycache_dirs": self.pycache_dirs,
            "source_less_pyc": self.source_less_pyc,
            "has_bytecode": self.has_bytecode,
            "has_dynamic_loading": self.has_dynamic_loading,
            "dynamic_load_hits": len(self.dynamic_load_hits),
            "magic_numbers": ";".join(
                f"{magic}:{count}" for magic, count in sorted(self.magic_numbers.items())
            ),
            "errors": "|".join(self.errors),
        }


@dataclass(frozen=True)
class FileEntry:
    path: str
    is_dir: bool
    data: bytes | None = None


def normalize_path(path: str) -> str:
    return path.replace("\\", "/").lstrip("./")


def is_archive(path: Path) -> bool:
    suffixes = "".join(path.suffixes).lower()
    return (
        suffixes.endswith(".whl")
        or suffixes.endswith(".zip")
        or suffixes.endswith(".tar")
        or suffixes.endswith(".tar.gz")
        or suffixes.endswith(".tgz")
        or suffixes.endswith(".tar.bz2")
        or suffixes.endswith(".tbz2")
        or suffixes.endswith(".tar.xz")
        or suffixes.endswith(".txz")
    )


def input_type(path: Path) -> str:
    if path.is_dir():
        return "directory"
    suffixes = "".join(path.suffixes).lower()
    if suffixes.endswith(".whl"):
        return "wheel"
    if suffixes.endswith(".zip"):
        return "zip"
    if ".tar" in suffixes or suffixes.endswith(".tgz") or suffixes.endswith(".tbz2") or suffixes.endswith(".txz"):
        return "tar"
    return "file"


def iter_directory(root: Path) -> Iterator[FileEntry]:
    for current, dirs, files in os.walk(root):
        dirs.sort()
        files.sort()
        current_path = Path(current)
        for dirname in dirs:
            path = current_path / dirname
            yield FileEntry(normalize_path(str(path.relative_to(root))), is_dir=True)
        for filename in files:
            path = current_path / filename
            rel = normalize_path(str(path.relative_to(root)))
            data = None
            if filename.endswith((".py", ".pyc")):
                try:
                    data = path.read_bytes()
                except OSError:
                    data = None
            yield FileEntry(rel, is_dir=False, data=data)


def iter_zip(path: Path) -> Iterator[FileEntry]:
    with zipfile.ZipFile(path) as zf:
        for info in sorted(zf.infolist(), key=lambda item: item.filename):
            name = normalize_path(info.filename)
            if not name:
                continue
            if info.is_dir():
                yield FileEntry(name.rstrip("/"), is_dir=True)
                continue
            data = None
            if name.endswith((".py", ".pyc")):
                try:
                    data = zf.read(info)
                except (OSError, RuntimeError, zipfile.BadZipFile):
                    data = None
            yield FileEntry(name, is_dir=False, data=data)


def iter_tar(path: Path) -> Iterator[FileEntry]:
    with tarfile.open(path) as tf:
        members = sorted(tf.getmembers(), key=lambda item: item.name)
        for member in members:
            name = normalize_path(member.name)
            if not name:
                continue
            if member.isdir():
                yield FileEntry(name.rstrip("/"), is_dir=True)
                continue
            data = None
            if member.isfile() and name.endswith((".py", ".pyc")):
                extracted = tf.extractfile(member)
                if extracted is not None:
                    try:
                        data = extracted.read()
                    except OSError:
                        data = None
            yield FileEntry(name, is_dir=False, data=data)


def iter_single_file(path: Path) -> Iterator[FileEntry]:
    data = None
    if path.name.endswith((".py", ".pyc")):
        try:
            data = path.read_bytes()
        except OSError:
            data = None
    yield FileEntry(path.name, is_dir=False, data=data)


def iter_entries(path: Path) -> Iterator[FileEntry]:
    if path.is_dir():
        yield from iter_directory(path)
    elif zipfile.is_zipfile(path):
        yield from iter_zip(path)
    elif tarfile.is_tarfile(path):
        yield from iter_tar(path)
    else:
        yield from iter_single_file(path)


def module_source_candidates(pyc_path: str) -> set[str]:
    path = normalize_path(pyc_path)
    candidates = set()
    if path.endswith(".pyc"):
        candidates.add(path[:-1])

    parts = path.split("/")
    if "__pycache__" in parts:
        idx = parts.index("__pycache__")
        filename = parts[-1]
        stem = filename[:-4] if filename.endswith(".pyc") else filename
        module = stem.split(".cpython-")[0].split(".pypy-")[0]
        if module:
            candidates.add("/".join(parts[:idx] + [module + ".py"]))
    return {normalize_path(item) for item in candidates}


def pyc_magic(data: bytes | None) -> str | None:
    if data is None or len(data) < 4:
        return None
    magic = struct.unpack("<H", data[:2])[0]
    return str(magic)


def scan_dynamic_patterns(path: str, data: bytes | None) -> list[DynamicHit]:
    if data is None:
        return []
    try:
        text = data.decode("utf-8", errors="ignore")
    except Exception:
        return []
    hits = []
    for name, pattern in DYNAMIC_LOAD_PATTERNS:
        if pattern.search(text):
            hits.append(DynamicHit(path=path, pattern=name))
    return hits


def scan_path(path: Path) -> ScanResult:
    result = ScanResult(input=str(path), input_type=input_type(path))
    py_paths: set[str] = set()
    pyc_paths: set[str] = set()

    try:
        entries = list(iter_entries(path))
    except Exception as exc:
        result.errors.append(f"open_failed:{type(exc).__name__}:{exc}")
        return result

    for entry in entries:
        entry_path = normalize_path(entry.path)
        if not entry_path:
            continue
        result.files_total += 1

        parts = entry_path.split("/")
        if entry.is_dir:
            if parts[-1] == "__pycache__":
                result.pycache_dirs += 1
            continue

        if "__pycache__" in parts[:-1]:
            # Some archives omit explicit directory entries.
            pass

        if entry_path.endswith(".py"):
            result.py_files += 1
            py_paths.add(entry_path)
            result.dynamic_load_hits.extend(scan_dynamic_patterns(entry_path, entry.data))
        elif entry_path.endswith(".pyc"):
            result.pyc_files += 1
            pyc_paths.add(entry_path)
            magic = pyc_magic(entry.data)
            if magic is not None:
                result.magic_numbers[magic] = result.magic_numbers.get(magic, 0) + 1

    explicit_pycache_dirs = {
        "/".join(parts[: idx + 1])
        for pyc in pyc_paths
        for parts in [pyc.split("/")]
        for idx, part in enumerate(parts)
        if part == "__pycache__"
    }
    result.pycache_dirs = max(result.pycache_dirs, len(explicit_pycache_dirs))

    for pyc in pyc_paths:
        candidates = module_source_candidates(pyc)
        if candidates and not any(candidate in py_paths for candidate in candidates):
            result.source_less_pyc += 1

    return result


def aggregate(results: Sequence[ScanResult]) -> dict[str, object]:
    return {
        "inputs": len(results),
        "inputs_with_bytecode": sum(1 for item in results if item.has_bytecode),
        "inputs_with_pyc": sum(1 for item in results if item.pyc_files > 0),
        "inputs_with_pycache": sum(1 for item in results if item.pycache_dirs > 0),
        "inputs_with_source_less_pyc": sum(1 for item in results if item.source_less_pyc > 0),
        "inputs_with_dynamic_loading": sum(1 for item in results if item.has_dynamic_loading),
        "py_files": sum(item.py_files for item in results),
        "pyc_files": sum(item.pyc_files for item in results),
        "source_less_pyc": sum(item.source_less_pyc for item in results),
        "dynamic_load_hits": sum(len(item.dynamic_load_hits) for item in results),
    }


def expand_inputs(inputs: Sequence[str], recursive: bool) -> list[Path]:
    paths: list[Path] = []
    for raw in inputs:
        path = Path(raw)
        if recursive and path.is_dir():
            selected_dirs: list[Path] = []
            for child in sorted(path.rglob("*")):
                if child.is_file() and is_archive(child):
                    paths.append(child)
                elif child.is_dir() and child.name != "__pycache__" and contains_python_artifacts(child):
                    if not any(is_relative_to(child, selected) for selected in selected_dirs):
                        paths.append(child)
                        selected_dirs.append(child)
        else:
            paths.append(path)
    return paths


def contains_python_artifacts(path: Path) -> bool:
    try:
        for child in path.rglob("*"):
            if child.is_file() and child.name.endswith((".py", ".pyc")):
                return True
    except OSError:
        return False
    return False


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def write_csv(path: Path, results: Sequence[ScanResult]) -> None:
    rows = [item.to_summary_row() for item in results]
    fieldnames = list(rows[0].keys()) if rows else list(ScanResult("", "").to_summary_row().keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Scan Python package artifacts for bytecode evidence."
    )
    parser.add_argument("inputs", nargs="+", help="Package directories or package archives to scan")
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="When an input is a directory, scan package archives below it as separate inputs.",
    )
    parser.add_argument("--csv-out", type=Path, default=Path("data/bytecode_scan.csv"), help="Write per-input CSV summary to this path")
    parser.add_argument("--json-out", type=Path, help="Optionally write detailed JSON results to this path")
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print optional JSON written to --json-out.",
    )
    args = parser.parse_args(argv)

    paths = expand_inputs(args.inputs, args.recursive)
    results = [scan_path(path) for path in paths]
    payload = {
        "aggregate": aggregate(results),
        "results": [
            {
                **asdict(result),
                "has_bytecode": result.has_bytecode,
                "has_dynamic_loading": result.has_dynamic_loading,
            }
            for result in results
        ],
    }

    args.csv_out.parent.mkdir(parents=True, exist_ok=True)
    write_csv(args.csv_out, results)
    aggregate_row = aggregate(results)
    print(
        "wrote {rows} scan rows to {path}; inputs_with_bytecode={with_bc}/{total}; pyc_files={pyc}".format(
            rows=len(results),
            path=args.csv_out,
            with_bc=aggregate_row["inputs_with_bytecode"],
            total=aggregate_row["inputs"],
            pyc=aggregate_row["pyc_files"],
        )
    )

    json_text = json.dumps(payload, indent=2 if args.pretty else None, sort_keys=True)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json_text + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
