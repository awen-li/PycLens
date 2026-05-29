#!/usr/bin/env python3
"""pybcSEC study helper for collecting and scanning Python package artifacts.

Components:
  1. collect-pypi: download package distribution files from PyPI.
  2. scan: scan local artifacts for bytecode evidence.

The tool intentionally uses only the Python standard library so it can run in a
fresh research VM before the rest of the experimental infrastructure exists.
"""

from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
import json
import random
import sys
import urllib.request
from dataclasses import asdict
from pathlib import Path
from typing import Sequence

from collectors import (
    CollectionConfig,
    GitHubReleaseCollector,
    LocalArtifactCollector,
    PYPI_DISTRIBUTIONS,
    PyPICollector,
    SuspiciousPyPICollector,
)
import scanner as bytecode_scan


DEFAULT_DATA_DIR = Path("data")
DEFAULT_INPUT_DIR = DEFAULT_DATA_DIR / "inputs"
DEFAULT_PYPI_PACKAGES = DEFAULT_INPUT_DIR / "pypi_packages.txt"
DEFAULT_SUSPICIOUS_PYPI_PACKAGES = DEFAULT_INPUT_DIR / "suspicious_pypi_packages.txt"
DEFAULT_LOCAL_ARTIFACTS = DEFAULT_INPUT_DIR / "local_artifacts.txt"
DEFAULT_GITHUB_REPOSITORIES = DEFAULT_INPUT_DIR / "github_repositories.txt"
PYPI_SIMPLE_URL = "https://pypi.org/simple/"


class SimpleIndexParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.names: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        for key, value in attrs:
            if key == "href" and value:
                name = value.rstrip("/").rsplit("/", 1)[-1]
                if name:
                    self.names.append(name)


def read_package_names(path: Path) -> list[str]:
    names: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        names.append(line)
    return names


def read_optional_lines(path: Path) -> list[str]:
    if not path.exists():
        return []
    return read_package_names(path)


def input_list_ready(path: Path) -> bool:
    return bool(read_optional_lines(path))


def write_lines(path: Path, values: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text("\n".join(values) + ("\n" if values else ""), encoding="utf-8")
    tmp.replace(path)


def fetch_pypi_names(timeout: int) -> list[str]:
    request = urllib.request.Request(PYPI_SIMPLE_URL, headers={"User-Agent": "pybcSEC-study-tool/0.1"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        text = response.read().decode("utf-8", errors="replace")
    parser = SimpleIndexParser()
    parser.feed(text)
    return sorted(set(parser.names))


def select_pypi_input_names(names: Sequence[str], size: str, seed: int) -> list[str]:
    if size == "all":
        return list(names)
    try:
        count = int(size)
    except ValueError as exc:
        raise SystemExit("--pypi-size must be an integer or 'all'") from exc
    if count < 1:
        raise SystemExit("--pypi-size must be positive or 'all'")
    if count > len(names):
        raise SystemExit(f"requested {count} PyPI packages, but only found {len(names)} names")
    rng = random.Random(seed)
    return sorted(rng.sample(list(names), count))


def prepare_inputs(args: argparse.Namespace) -> int:
    normalize_input_paths(args)
    print("[phase 1/3] preparing dataset input lists")
    force = bool(getattr(args, "force_inputs", False) or getattr(args, "force_prepare", False))
    if input_list_ready(args.pypi_package_file) and not force:
        packages = read_package_names(args.pypi_package_file)
        print(f"using existing PyPI input list: {args.pypi_package_file} ({len(packages)} packages)")
        ensure_curated_input_templates(args)
        return 0

    print(f"fetching PyPI package index from {PYPI_SIMPLE_URL}")
    names = fetch_pypi_names(args.timeout)
    packages = select_pypi_input_names(names, args.pypi_size, args.seed)
    write_lines(args.pypi_package_file, packages)
    ensure_curated_input_templates(args)

    print(f"wrote {len(packages)} PyPI package names to {args.pypi_package_file}")
    return 0


def ensure_curated_input_templates(args: argparse.Namespace) -> None:
    template_paths = [
        args.suspicious_pypi_package_file,
        args.local_artifact_file,
        args.github_repo_file,
    ]
    for path in template_paths:
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# Add one entry per line.\n", encoding="utf-8")

    print("created empty curated input templates when missing:")
    for path in template_paths:
        print(f"  {path}")


def normalize_input_paths(args: argparse.Namespace) -> None:
    input_dir = args.data_dir / "inputs"
    if args.pypi_package_file is None:
        args.pypi_package_file = input_dir / "pypi_packages.txt"
    if args.suspicious_pypi_package_file is None:
        args.suspicious_pypi_package_file = input_dir / "suspicious_pypi_packages.txt"
    if args.local_artifact_file is None:
        args.local_artifact_file = input_dir / "local_artifacts.txt"
    if args.github_repo_file is None:
        args.github_repo_file = input_dir / "github_repositories.txt"


def resolve_packages(args: argparse.Namespace) -> list[str]:
    packages = list(args.package or [])
    if args.package_file:
        packages.extend(read_package_names(args.package_file))
    return list(dict.fromkeys(packages))


def collect_pypi(args: argparse.Namespace) -> int:
    packages = resolve_packages(args)

    if not packages:
        raise SystemExit("collect-pypi requires --package or --package-file")

    collector = PyPICollector(
        CollectionConfig(
            data_dir=args.data_dir,
            out_dir=args.out_dir,
            csv_out=args.csv_out,
            json_out=args.json_out,
            include=tuple(args.include or PYPI_DISTRIBUTIONS),
            max_files_per_kind=args.max_files_per_kind,
            timeout=args.timeout,
            delay=args.delay,
            force=args.force,
            quiet=args.quiet,
            max_age_years=normalize_max_age_years(args.max_age_years),
            workers=args.workers,
        )
    )
    records = collector.collect(packages)
    csv_out = collector.write_outputs(records)
    print(f"wrote {len(records)} collection records to {csv_out}")
    return 0


def collect_all(args: argparse.Namespace) -> int:
    normalize_input_paths(args)
    print("[phase 2/3] collecting dataset artifacts")
    pypi_packages = read_optional_lines(args.pypi_package_file)
    suspicious_packages = read_optional_lines(args.suspicious_pypi_package_file)
    local_artifacts = read_optional_lines(args.local_artifact_file)
    github_repos = read_optional_lines(args.github_repo_file)

    if not any((pypi_packages, suspicious_packages, local_artifacts, github_repos)):
        raise SystemExit(
            "no real dataset inputs found. Create one or more files under data/inputs/:\n"
            f"  {args.pypi_package_file}              ordinary PyPI package names\n"
            f"  {args.suspicious_pypi_package_file}   suspicious/malicious PyPI package names\n"
            f"  {args.local_artifact_file}            local bundle/archive/directory paths\n"
            f"  {args.github_repo_file}               GitHub repositories as owner/name"
        )

    total_records = 0
    manifests: list[Path] = []

    if pypi_packages:
        print(f"source pypi: {len(pypi_packages)} packages")
        collector = PyPICollector(collection_config(args, PYPI_DISTRIBUTIONS))
        records = collector.collect(pypi_packages)
        manifests.append(collector.write_outputs(records))
        total_records += len(records)

    if suspicious_packages:
        print(f"source suspicious_pypi: {len(suspicious_packages)} packages")
        collector = SuspiciousPyPICollector(collection_config(args, PYPI_DISTRIBUTIONS))
        records = collector.collect(suspicious_packages)
        manifests.append(collector.write_outputs(records))
        total_records += len(records)

    if local_artifacts:
        print(f"source local: {len(local_artifacts)} paths")
        collector = LocalArtifactCollector(collection_config(args, ()))
        records = collector.collect(local_artifacts)
        manifests.append(collector.write_outputs(records))
        total_records += len(records)

    if github_repos:
        print(f"source github_releases: {len(github_repos)} repositories")
        collector = GitHubReleaseCollector(collection_config(args, ("wheel", "zip", "archive")))
        records = collector.collect(github_repos)
        manifests.append(collector.write_outputs(records))
        total_records += len(records)

    print(f"wrote {total_records} collection records across {len(manifests)} manifests")
    for manifest in manifests:
        print(f"  {manifest}")
    return 0


def run_pipeline(args: argparse.Namespace) -> int:
    normalize_input_paths(args)
    prepare_inputs(args)
    collect_all(args)

    scan_args = argparse.Namespace(
        data_dir=args.data_dir,
        inputs=[],
        recursive=True,
        csv_out=None,
        json_out=None,
        progress_every=50,
        workers=args.workers,
    )
    return scan(scan_args)


def collect_suspicious_pypi(args: argparse.Namespace) -> int:
    packages = resolve_packages(args)

    if not packages:
        raise SystemExit("collect-suspicious-pypi requires --package or --package-file")

    collector = SuspiciousPyPICollector(collection_config(args, PYPI_DISTRIBUTIONS))
    records = collector.collect(packages)
    csv_out = collector.write_outputs(records)
    print(f"wrote {len(records)} collection records to {csv_out}")
    return 0


def collect_local(args: argparse.Namespace) -> int:
    if not args.input:
        raise SystemExit("collect-local requires at least one input path")

    collector = LocalArtifactCollector(collection_config(args, ()))
    records = collector.collect([str(item) for item in args.input])
    csv_out = collector.write_outputs(records)
    print(f"wrote {len(records)} collection records to {csv_out}")
    return 0


def collect_github_release(args: argparse.Namespace) -> int:
    repos = list(args.repo or [])
    if args.repo_file:
        repos.extend(read_package_names(args.repo_file))
    repos = list(dict.fromkeys(repos))

    if not repos:
        raise SystemExit("collect-github-release requires --repo or --repo-file")

    collector = GitHubReleaseCollector(collection_config(args, ("wheel", "zip", "archive")))
    records = collector.collect(repos)
    csv_out = collector.write_outputs(records)
    print(f"wrote {len(records)} collection records to {csv_out}")
    return 0


def collection_config(args: argparse.Namespace, default_include: Sequence[str]) -> CollectionConfig:
    return CollectionConfig(
        data_dir=args.data_dir,
        out_dir=args.out_dir,
        csv_out=args.csv_out,
        json_out=args.json_out,
        include=tuple(args.include or default_include),
        max_files_per_kind=args.max_files_per_kind,
        timeout=args.timeout,
        delay=args.delay,
        force=args.force,
        quiet=args.quiet,
        max_age_years=normalize_max_age_years(args.max_age_years),
        workers=args.workers,
    )


def normalize_max_age_years(value: int | None) -> int | None:
    if value is None or value <= 0:
        return None
    return value


def scan(args: argparse.Namespace) -> int:
    print("[phase 3/3] scanning unified artifact directory")
    default_input = args.data_dir / "artifacts"
    if args.inputs:
        inputs = [str(item) for item in args.inputs]
        paths = bytecode_scan.expand_inputs(inputs, args.recursive)
    elif default_input.exists():
        inputs = [str(default_input)]
        paths = bytecode_scan.expand_inputs(inputs, True)
    else:
        inputs = [str(default_input)]
        paths = []
    print(f"scan inputs: {len(paths)} artifact entries from {', '.join(inputs)}")
    results = []
    progress_every = max(1, int(getattr(args, "progress_every", 50)))
    scan_workers = max(1, int(getattr(args, "workers", 8)))
    print(f"scan workers: {scan_workers}")
    if scan_workers == 1:
        for index, path in enumerate(paths, start=1):
            result = scan_one(path, index, len(paths), progress_every)
            results.append(result)
    else:
        with ThreadPoolExecutor(max_workers=scan_workers) as executor:
            futures = {
                executor.submit(bytecode_scan.scan_path, path): (index, path)
                for index, path in enumerate(paths, start=1)
            }
            completed = 0
            for future in as_completed(futures):
                index, path = futures[future]
                result = future.result()
                results.append(result)
                completed += 1
                if completed == 1 or completed == len(paths) or completed % progress_every == 0:
                    print(f"[scan {completed}/{len(paths)}] latest={path}")
                print_scan_event(path, result)
    csv_out: Path = args.csv_out or args.data_dir / "scan" / "bytecode_scan.csv"
    csv_out.parent.mkdir(parents=True, exist_ok=True)
    bytecode_scan.write_csv(csv_out, results)
    aggregate = bytecode_scan.aggregate(results)
    print_scan_summary(results, aggregate)

    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "component": "bytecode_scan",
            "aggregate": aggregate,
            "results": [
                {
                    **asdict(result),
                    "has_bytecode": result.has_bytecode,
                    "has_dynamic_loading": result.has_dynamic_loading,
                }
                for result in results
            ],
        }
        args.json_out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(
        "wrote {rows} scan rows to {path}; inputs_with_bytecode={with_bc}/{total}; pyc_files={pyc}".format(
            rows=len(results),
            path=csv_out,
            with_bc=aggregate["inputs_with_bytecode"],
            total=aggregate["inputs"],
            pyc=aggregate["pyc_files"],
        )
    )
    return 0


def print_scan_summary(results: Sequence[bytecode_scan.ScanResult], aggregate: dict[str, object]) -> None:
    by_type = Counter(result.input_type for result in results)
    print("scan summary:")
    print(
        "  artifacts={inputs}, with_bytecode={with_bc}, py_files={py}, pyc_files={pyc}, source_less_pyc={src_less}, dynamic_hits={dyn}".format(
            inputs=aggregate["inputs"],
            with_bc=aggregate["inputs_with_bytecode"],
            py=aggregate["py_files"],
            pyc=aggregate["pyc_files"],
            src_less=aggregate["source_less_pyc"],
            dyn=aggregate["dynamic_load_hits"],
        )
    )
    if by_type:
        print("  by_type: " + ", ".join(f"{kind}={count}" for kind, count in sorted(by_type.items())))


def scan_one(path: Path, index: int, total: int, progress_every: int) -> bytecode_scan.ScanResult:
    if index == 1 or index == total or index % progress_every == 0:
        print(f"[scan {index}/{total}] {path}")
    result = bytecode_scan.scan_path(path)
    print_scan_event(path, result)
    return result


def print_scan_event(path: Path, result: bytecode_scan.ScanResult) -> None:
    if result.has_bytecode:
        print(
            f"[bytecode] {path} pyc={result.pyc_files} pycache={result.pycache_dirs} source_less={result.source_less_pyc}"
        )
    if result.errors:
        print(f"[scan-error] {path} {'|'.join(result.errors)}")


def add_collection_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--package", action="append", help="Package name; may be repeated")
    parser.add_argument("--package-file", type=Path, help="Text file containing one package per line")
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR, help="Root directory for collected data")
    parser.add_argument("--out-dir", type=Path, help="Artifact output directory; defaults to data/artifacts/pypi")
    parser.add_argument("--csv-out", type=Path, help="CSV manifest path; defaults to data/sources/pypi/manifest.csv")
    parser.add_argument("--json-out", type=Path, help="Optional detailed JSON manifest")
    parser.add_argument(
        "--include",
        choices=(*PYPI_DISTRIBUTIONS, "other"),
        action="append",
        default=None,
        help="Distribution kind to collect; may be repeated. Defaults to wheel and sdist.",
    )
    parser.add_argument("--max-files-per-kind", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--delay", type=float, default=0.2)
    parser.add_argument("--max-age-years", type=int, default=5, help="Only collect artifacts uploaded within this many years; use 0 for no age filter")
    parser.add_argument("--workers", type=int, default=8, help="Parallel package download workers")
    parser.add_argument("--force", action="store_true", help="Redownload files that already exist")
    parser.add_argument("--quiet", action="store_true", help="Only print the final summary")
    parser.set_defaults(func=collect_pypi)


def add_common_collector_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR, help="Root directory for collected data")
    parser.add_argument("--out-dir", type=Path, help="Artifact output directory; defaults to data/artifacts/<source>")
    parser.add_argument("--csv-out", type=Path, help="CSV manifest path; defaults to data/sources/<source>/manifest.csv")
    parser.add_argument("--json-out", type=Path, help="Optional detailed JSON manifest")
    parser.add_argument(
        "--include",
        action="append",
        default=None,
        help="Collector-specific artifact kind filter; may be repeated",
    )
    parser.add_argument("--max-files-per-kind", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--delay", type=float, default=0.2)
    parser.add_argument("--max-age-years", type=int, default=5, help="Only collect source artifacts uploaded within this many years where supported; use 0 for no age filter")
    parser.add_argument("--workers", type=int, default=8, help="Parallel package download workers where supported")
    parser.add_argument("--force", action="store_true", help="Redownload or recopy files that already exist")
    parser.add_argument("--quiet", action="store_true", help="Only print the final summary")


def add_prepare_inputs_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "prepare-inputs",
        help="Generate real dataset input lists under data/inputs.",
    )
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR, help="Root directory for dataset inputs")
    parser.add_argument("--pypi-package-file", type=Path)
    parser.add_argument("--suspicious-pypi-package-file", type=Path)
    parser.add_argument("--local-artifact-file", type=Path)
    parser.add_argument("--github-repo-file", type=Path)
    parser.add_argument("--pypi-size", default="all", help="Number of PyPI package names to use, or 'all'")
    parser.add_argument("--pypi-random-size", dest="pypi_size", help=argparse.SUPPRESS)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("--force", dest="force_prepare", action="store_true", help="Overwrite generated input lists")
    parser.set_defaults(func=prepare_inputs)


def add_run_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "run",
        help="Run prepare, collect, and scan in sequence.",
    )
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR, help="Root directory for study data")
    parser.add_argument("--pypi-package-file", type=Path, help=argparse.SUPPRESS)
    parser.add_argument("--suspicious-pypi-package-file", type=Path, help=argparse.SUPPRESS)
    parser.add_argument("--local-artifact-file", type=Path, help=argparse.SUPPRESS)
    parser.add_argument("--github-repo-file", type=Path, help=argparse.SUPPRESS)
    parser.add_argument("--pypi-size", default="all", help=argparse.SUPPRESS)
    parser.add_argument("--seed", type=int, default=0, help=argparse.SUPPRESS)
    parser.add_argument(
        "--include",
        choices=(*PYPI_DISTRIBUTIONS, "other", "zip", "archive"),
        action="append",
        default=None,
        help=argparse.SUPPRESS,
    )
    parser.add_argument("--max-files-per-kind", type=int, default=1, help=argparse.SUPPRESS)
    parser.add_argument("--timeout", type=int, default=60, help=argparse.SUPPRESS)
    parser.add_argument("--delay", type=float, default=0.2, help=argparse.SUPPRESS)
    parser.add_argument("--max-age-years", type=int, default=5, help=argparse.SUPPRESS)
    parser.add_argument("--workers", type=int, default=8, help="Parallel workers for download and scan")
    parser.add_argument("--force", action="store_true", help="Redownload or recopy collected artifacts")
    parser.add_argument("--force-inputs", action="store_true", help="Regenerate dataset input lists")
    parser.add_argument("--prepare", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--quiet", action="store_true", help="Reduce collector progress output")
    parser.set_defaults(func=run_pipeline, out_dir=None, csv_out=None, json_out=None)


def add_collect_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "collect",
        help="Collect all configured real dataset sources from data/inputs.",
    )
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR, help="Root directory for collected data")
    parser.add_argument("--pypi-package-file", type=Path)
    parser.add_argument("--suspicious-pypi-package-file", type=Path)
    parser.add_argument("--local-artifact-file", type=Path)
    parser.add_argument("--github-repo-file", type=Path)
    parser.add_argument(
        "--include",
        choices=(*PYPI_DISTRIBUTIONS, "other", "zip", "archive"),
        action="append",
        default=None,
        help="Artifact kind to collect where supported; defaults are source-specific",
    )
    parser.add_argument("--max-files-per-kind", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--delay", type=float, default=0.2)
    parser.add_argument("--max-age-years", type=int, default=5, help="Only collect source artifacts uploaded within this many years where supported; use 0 for no age filter")
    parser.add_argument("--workers", type=int, default=8, help="Parallel package download workers where supported")
    parser.add_argument("--force", action="store_true", help="Redownload or recopy files that already exist")
    parser.add_argument("--quiet", action="store_true", help="Only print final summaries")
    parser.set_defaults(func=collect_all, out_dir=None, csv_out=None, json_out=None)


def add_collect_pypi_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "collect-pypi",
        help="Collect PyPI release metadata and distribution artifacts.",
    )
    add_collection_arguments(parser)


def add_collect_suspicious_pypi_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "collect-suspicious-pypi",
        help="Collect suspicious or malicious PyPI package artifacts.",
    )
    add_collection_arguments(parser)
    parser.set_defaults(func=collect_suspicious_pypi)


def add_collect_local_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "collect-local",
        help="Collect local bundles, archives, directories, or runtime corpus files.",
    )
    parser.add_argument("input", nargs="+", type=Path, help="Local artifact path; may be repeated")
    add_common_collector_arguments(parser)
    parser.set_defaults(func=collect_local)


def add_collect_github_release_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "collect-github-release",
        help="Collect downloadable assets from the latest GitHub release.",
    )
    parser.add_argument("--repo", action="append", help="GitHub repository as owner/name; may be repeated")
    parser.add_argument("--repo-file", type=Path, help="Text file containing one owner/name repository per line")
    add_common_collector_arguments(parser)
    parser.set_defaults(func=collect_github_release)


def add_scan_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "scan",
        help="Scan local package artifacts for bytecode evidence.",
    )
    parser.add_argument(
        "inputs",
        nargs="*",
        type=Path,
        help="Package directories or package archives to scan; defaults to data/artifacts",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Treat package archives below input directories as separate inputs.",
    )
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR, help="Root directory for scan outputs")
    parser.add_argument("--csv-out", type=Path, help="CSV report path; defaults to data/scan/bytecode_scan.csv")
    parser.add_argument("--json-out", type=Path, help="Optional detailed JSON results")
    parser.add_argument("--progress-every", type=int, default=50, help="Print scan progress every N artifacts")
    parser.add_argument("--workers", type=int, default=8, help="Parallel scan workers")
    parser.set_defaults(func=scan)


def main(argv: Sequence[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    if not argv:
        argv = ["run"]

    parser = argparse.ArgumentParser(
        description="pybcSEC study tool for data collection and bytecode scanning."
    )
    subparsers = parser.add_subparsers(dest="component", required=True)
    add_run_parser(subparsers)
    add_prepare_inputs_parser(subparsers)
    add_collect_parser(subparsers)
    add_collect_pypi_parser(subparsers)
    add_collect_suspicious_pypi_parser(subparsers)
    add_collect_local_parser(subparsers)
    add_collect_github_release_parser(subparsers)
    add_scan_parser(subparsers)
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
