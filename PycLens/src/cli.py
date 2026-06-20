#!/usr/bin/env python3
"""PycLens study helper for collecting and scanning Python package artifacts.

Components:
  1. collect-pypi: download package distribution files from PyPI.
  2. scan: scan local artifacts for bytecode evidence.

The tool intentionally uses only the Python standard library so it can run in a
fresh research VM before the rest of the experimental infrastructure exists.
"""

from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
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
    PYPI_DISTRIBUTIONS,
    PyPICollector,
)
import scanner as bytecode_scan
import cpython_fuzz
import crash_analysis
from rq1_analysis import RQ1Analyzer
import source_repro
import tool_analysis


DEFAULT_DATA_DIR = Path("data")
DEFAULT_SMOKE_DATA_DIR = DEFAULT_DATA_DIR / "smoke"
DEFAULT_INPUT_DIR = DEFAULT_DATA_DIR / "inputs"
DEFAULT_PYPI_PACKAGES = DEFAULT_INPUT_DIR / "pypi_packages.txt"
PYPI_SIMPLE_URL = "https://pypi.org/simple/"
DEFAULT_SMOKE_ITEMS_PER_SOURCE = 1000


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
    request = urllib.request.Request(PYPI_SIMPLE_URL, headers={"User-Agent": "PycLens-study-tool/0.1"})
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


def first_n_or_exit(values: Sequence[str], count: int, path: Path) -> list[str]:
    if len(values) < count:
        raise SystemExit(
            f"requested {count} PyPI items, but {path} has {len(values)}. "
            f"Add more entries to that input file or run with a smaller --items-per-source."
        )
    return list(values[:count])


def limit_source_items(
    values: Sequence[str],
    count: int | None,
    path: Path,
) -> list[str]:
    if count is None:
        return list(values)
    if count < 1:
        raise SystemExit("--items-per-source must be positive")
    return first_n_or_exit(values, count, path)


def prepare_inputs(args: argparse.Namespace) -> int:
    normalize_input_paths(args)
    print("[phase 1/3] preparing dataset input lists")
    force = bool(getattr(args, "force_inputs", False) or getattr(args, "force_prepare", False))
    if input_list_ready(args.pypi_package_file) and not force:
        packages = read_package_names(args.pypi_package_file)
        print(f"using existing PyPI input list: {args.pypi_package_file} ({len(packages)} packages)")
        return 0

    print(f"fetching PyPI package index from {PYPI_SIMPLE_URL}")
    names = fetch_pypi_names(args.timeout)
    packages = select_pypi_input_names(names, args.pypi_size, args.seed)
    write_lines(args.pypi_package_file, packages)

    print(f"wrote {len(packages)} PyPI package names to {args.pypi_package_file}")
    return 0


def normalize_input_paths(args: argparse.Namespace) -> None:
    input_dir = args.data_dir / "inputs"
    if args.pypi_package_file is None:
        args.pypi_package_file = input_dir / "pypi_packages.txt"


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
    count = getattr(args, "items_per_source", None)
    pypi_packages = limit_source_items(
        read_optional_lines(args.pypi_package_file),
        count,
        args.pypi_package_file,
    )

    if not pypi_packages:
        raise SystemExit(
            "no PyPI dataset inputs found. Run prepare-inputs or create:\n"
            f"  {args.pypi_package_file}              ordinary PyPI package names"
        )

    total_records = 0
    manifests: list[Path] = []

    print(f"source pypi: {len(pypi_packages)} packages")
    collector = PyPICollector(collection_config(args, PYPI_DISTRIBUTIONS))
    records = collector.collect(pypi_packages)
    manifests.append(collector.write_outputs(records))
    total_records += len(records)

    print(f"wrote {total_records} collection records across {len(manifests)} manifests")
    for manifest in manifests:
        print(f"  {manifest}")
    return 0


def run_pipeline(args: argparse.Namespace) -> int:
    normalize_input_paths(args)
    if args.items_per_source is not None and args.pypi_size == "all":
        args.pypi_size = str(args.items_per_source)
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


def smoke_test(args: argparse.Namespace) -> int:
    count = args.items_per_source
    if count < 1:
        raise SystemExit("--items-per-source must be positive")

    print(f"[smoke] preparing {count} PyPI items")
    pypi_package_file = args.data_dir / "inputs" / "pypi_packages.txt"
    if input_list_ready(pypi_package_file) and not args.force_inputs:
        pypi_packages = read_package_names(pypi_package_file)
        print(f"[smoke] using existing PyPI smoke list: {pypi_package_file} ({len(pypi_packages)} packages)")
    else:
        print(f"[smoke] fetching PyPI package index from {PYPI_SIMPLE_URL}")
        names = fetch_pypi_names(args.timeout)
        pypi_packages = select_pypi_input_names(names, str(count), args.seed)
        write_lines(pypi_package_file, pypi_packages)
        print(f"[smoke] wrote {len(pypi_packages)} PyPI package names to {pypi_package_file}")

    pypi_packages = first_n_or_exit(pypi_packages, count, pypi_package_file)

    print("[smoke] collecting source pypi")
    pypi_collector = PyPICollector(collection_config(args, PYPI_DISTRIBUTIONS))
    pypi_manifest = pypi_collector.write_outputs(pypi_collector.collect(pypi_packages))
    print(f"[smoke] wrote PyPI manifest: {pypi_manifest}")

    return scan(
        argparse.Namespace(
            data_dir=args.data_dir,
            inputs=[],
            recursive=True,
            csv_out=None,
            json_out=None,
            progress_every=50,
            workers=args.workers,
        )
    )


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
    default_input = args.data_dir / "artifacts" / "pypi"
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
            pending = {
                executor.submit(bytecode_scan.scan_path, path): (index, path)
                for index, path in enumerate(paths, start=1)
            }
            completed = 0
            while pending:
                done, _ = wait(pending, timeout=30, return_when=FIRST_COMPLETED)
                if not done:
                    pending_items = list(pending.values())[: min(10, len(pending))]
                    print(f"[scan wait] completed={completed}/{len(paths)} pending={len(pending)}")
                    for pending_index, pending_path in pending_items:
                        print(f"  pending [{pending_index}/{len(paths)}] {pending_path}")
                    continue
                for future in done:
                    index, path = pending.pop(future)
                    result = future.result()
                    results.append(result)
                    completed += 1
                    if completed == 1 or completed == len(paths) or completed % progress_every == 0:
                        print(f"[scan {completed}/{len(paths)}] latest={path}")
                    print_scan_event(path, result)
    csv_out: Path = args.csv_out or args.data_dir / "scan" / "bytecode_scan.csv"
    csv_out.parent.mkdir(parents=True, exist_ok=True)
    bytecode_scan.write_csv(csv_out, results)
    versions_out = args.data_dir / "scan" / "cpython_versions.csv"
    bytecode_scan.write_python_versions_csv(versions_out, results)
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
    print(f"wrote CPython bytecode version summary to {versions_out}")
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


def summarize_rq1(args: argparse.Namespace) -> int:
    analyzer = RQ1Analyzer(
        data_dir=args.data_dir,
        scan_csv=args.scan_csv,
        versions_csv=args.versions_csv,
    )
    analyzer.analyze()
    return 0


def analyze_tools(args: argparse.Namespace) -> int:
    print("[RQ2] analyzing practical bytecode analyzability")
    scan_csv = args.scan_csv or args.data_dir / "scan" / "bytecode_scan.csv"
    csv_out = args.csv_out or args.data_dir / "rq2" / "tool_analysis.csv"
    versions_csv = args.data_dir / "rq1" / "rq1_versions.csv"
    interpreters = tool_analysis.load_interpreter_environment(
        versions_csv,
        data_dir=args.data_dir,
    )
    tool_envs = tool_analysis.load_tool_environment(args.data_dir, interpreters)
    tool_analysis.print_interpreter_environment(interpreters)
    magic_tags = tool_analysis.load_magic_tag_map(interpreters, args.timeout)
    artifacts = tool_analysis.read_bytecode_artifacts(scan_csv)
    if args.limit:
        artifacts = artifacts[: args.limit]
        print(f"limited analysis to first {len(artifacts)} bytecode-containing artifacts")
    results = tool_analysis.analyze_artifacts(
        artifacts,
        workers=args.workers,
        external_timeout=args.timeout,
        interpreters=interpreters,
        tool_envs=tool_envs,
        data_dir=args.data_dir,
        magic_tags=magic_tags,
        run_tools=not args.count_only,
    )
    if args.count_only:
        denominator_summary = args.data_dir / "rq2" / "rq2_denominator_summary.csv"
        denominator_artifacts = args.data_dir / "rq2" / "rq2_denominator_artifacts.csv"
        tool_analysis.write_count_only_reports(denominator_summary, denominator_artifacts, results, artifacts, scan_csv)
        print(f"wrote RQ2 denominator audit to {denominator_summary}")
        print(f"wrote RQ2 denominator artifact audit to {denominator_artifacts}")
        print("count-only mode: skipped marshal/dis/decompiler tool analysis")
        return 0
    tool_analysis.write_csv(csv_out, results)
    summary_csv = args.data_dir / "rq2" / "rq2_summary.csv"
    tool_analysis.write_summary_csv(summary_csv, results)
    completeness_csv = args.data_dir / "rq2" / "rq2_analysis_completeness.csv"
    expected_pyc = tool_analysis.read_count_only_expected(args.data_dir / "rq2" / "rq2_denominator_summary.csv")
    completeness = tool_analysis.write_analysis_completeness_report(completeness_csv, results, expected_pyc)
    source_less_reports = tool_analysis.write_source_less_reports(args.data_dir / "rq2", results, scan_csv)
    failure_reports = tool_analysis.write_failure_reports(args.data_dir / "rq2", results)
    summary = tool_analysis.summarize(results)
    print(
        "tool analysis summary: pyc_files={pyc}, source_present={src}, source_less={src_less}, "
        "runtime_magic={magic}, marshal_ok={marshal_ok}, dis_ok={dis_ok}, "
        "decompyle3_ok={decompyle3}, pylingual_ok={pylingual}".format(
            pyc=summary["pyc_files"],
            src=summary["source_present"],
            src_less=summary["source_less"],
            magic=summary["runtime_magic"],
            marshal_ok=summary["marshal_ok"],
            dis_ok=summary["dis_ok"],
            decompyle3=summary["decompyle3_ok"],
            pylingual=summary["pylingual_ok"],
        )
    )
    print(
        "analysis levels: L0_not_analyzable={l0}, L1_loadable_only={l1}, "
        "L2_disassemblable={l2}, L3_partial_decompile={l3}, L4_full_decompile={l4}".format(
            l0=summary["level_0"],
            l1=summary["level_1"],
            l2=summary["level_2"],
            l3=summary["level_3"],
            l4=summary["level_4"],
        )
    )
    print(f"wrote {len(results)} tool-analysis rows to {csv_out}")
    print(f"wrote RQ2 summary to {summary_csv}")
    print(f"wrote RQ2 analysis completeness report to {completeness_csv}")
    if completeness.get("complete") == "False":
        print(
            "WARNING: RQ2 tool analysis is incomplete: expected_pyc={expected}, analyzed_rows={actual}, missing_rows={missing}".format(
                expected=completeness.get("expected_pyc"),
                actual=completeness.get("analyzed_rows"),
                missing=completeness.get("missing_rows"),
            )
        )
    print("wrote RQ2 source-less subset reports:")
    for path in source_less_reports:
        print(f"  {path}")
    print("wrote RQ2 failed-PYC analysis reports:")
    for path in failure_reports:
        print(f"  {path}")
    print(f"wrote RQ2 failed-case replay corpus to {args.data_dir / 'rq2' / 'failed_cases'}")
    return 0


def collect_failed_cases(args: argparse.Namespace) -> int:
    print("[RQ2] collecting failed .pyc cases from existing tool-analysis results")
    csv_path = args.csv_in or args.data_dir / "rq2" / "tool_analysis.csv"
    reports = tool_analysis.collect_failed_cases_from_csv(csv_path, args.data_dir / "rq2")
    manifest = args.data_dir / "rq2" / "failed_cases" / "manifest.csv"
    print(f"read RQ2 tool-analysis rows from {csv_path}")
    print(f"wrote RQ2 failed-case replay corpus to {args.data_dir / 'rq2' / 'failed_cases'}")
    print(f"wrote RQ2 failed-case manifest to {manifest}")
    print("wrote RQ2 failed-PYC reports:")
    for path in reports:
        print(f"  {path}")
    return 0



def prepare_analysis_env(args: argparse.Namespace) -> int:
    print("[RQ2] preparing CPython-specific analysis environments")
    versions_csv = args.data_dir / "rq1" / "rq1_versions.csv"
    out_csv = tool_analysis.prepare_analysis_environment(
        args.data_dir,
        versions_csv,
        args.timeout,
    )
    print(f"wrote analysis environment report to {out_csv}")
    print(f"wrote tool version report to {args.data_dir / 'rq2' / 'tool_versions.csv'}")
    return 0


def fuzz_cpython(args: argparse.Namespace) -> int:
    print("[RQ3] fuzzing CPython bytecode processing with honggfuzz", flush=True)
    versions_csv = args.data_dir / "scan" / "cpython_versions.csv"
    interpreters = tool_analysis.load_interpreter_environment(versions_csv, data_dir=args.data_dir)
    rq3_root = args.data_dir / "rq3"
    seed_dir = rq3_root
    raw_seed_root = rq3_root
    cpython_source_root = rq3_root
    if args.versions:
        tags = sorted({cpython_fuzz.version_to_tag(version) for version in args.versions})
    else:
        tags = sorted(
            set(cpython_fuzz.read_version_tags(versions_csv))
            | set(cpython_fuzz.discover_unittest_seed_tags(raw_seed_root, seed_dir, cpython_source_root))
        )
    if not tags:
        raise SystemExit("no RQ3 CPython versions found. Run pyclens scan first or add CPython unittest seeds under data/rq3/unittest_seeds/.")
    for tag in tags:
        if tag not in interpreters:
            interpreters[tag] = tool_analysis.find_interpreter(tag, bytecode_scan.python_tag_to_executable(tag), args.data_dir)
    print("RQ3 CPython versions: " + ", ".join(tags), flush=True)
    if args.instrument:
        interpreters = cpython_fuzz.prepare_instrumented_interpreters(
            tags,
            interpreters,
            args.data_dir,
            args.timeout,
        )
    seeds = cpython_fuzz.build_seed_corpus(
        tags,
        interpreters,
        seed_dir,
        args.timeout,
        raw_seed_root=raw_seed_root,
        cpython_source_root=cpython_source_root,
    )
    seed_csv = args.data_dir / "rq3" / "bytecode_seeds.csv"
    cpython_fuzz.write_seed_csv(seed_csv, seeds)
    print(f"RQ3 seed corpus: seeds={len(seeds)} tags={len({seed.python_tag for seed in seeds})} output={rq3_root}/cpython-<version>/seeds")
    for tag in sorted({seed.python_tag for seed in seeds}):
        print(f"  {tag}: {sum(1 for seed in seeds if seed.python_tag == tag)} seeds")
    if not seeds:
        raise SystemExit("RQ3 seed corpus is empty; stop before fuzzing")

    runs = cpython_fuzz.run_fuzz_campaigns(
        seeds,
        data_dir=args.data_dir,
        versions_csv=versions_csv,
        workers=args.workers,
        duration=args.duration,
        timeout=args.timeout,
        honggfuzz_path=args.honggfuzz,
        interpreters=interpreters,
    )
    run_csv = args.data_dir / "rq3" / "fuzz_runs.csv"
    summary_csv = args.data_dir / "rq3" / "rq3_summary.csv"
    cpython_fuzz.write_run_csv(run_csv, runs)
    cpython_fuzz.write_summary_csv(summary_csv, seeds, runs)
    version_reports = cpython_fuzz.write_version_reports(args.data_dir, seeds, runs)
    print(
        "RQ3 fuzz summary: runs={runs}, crashes={crashes}, timeouts={timeouts}".format(
            runs=len(runs),
            crashes=sum(run.crashes for run in runs),
            timeouts=sum(run.timeouts for run in runs),
        )
    )
    print("wrote per-version RQ3 reports:")
    for path in version_reports:
        print(f"  {path}")
    print("wrote aggregate RQ3 reports:")
    print(f"  {seed_csv}")
    print(f"  {run_csv}")
    print(f"  {summary_csv}")
    return 0


def smoke_rq3(args: argparse.Namespace) -> int:
    if not args.version:
        raise SystemExit("smoke-rq3 requires one CPython version, such as 3.10 or cpython-310")
    return fuzz_cpython(
        argparse.Namespace(
            data_dir=args.data_dir,
            versions=[args.version],
            workers=args.workers,
            duration=args.duration,
            timeout=args.timeout,
            honggfuzz=args.honggfuzz,
            instrument=False,
        )
    )


def reproduce_source(args: argparse.Namespace) -> int:
    print("[RQ4] checking source-level reproducibility of bytecode findings")
    versions_csv = args.data_dir / "scan" / "cpython_versions.csv"
    if args.versions:
        tags = sorted({cpython_fuzz.version_to_tag(version) for version in args.versions})
    else:
        tags = sorted(
            set(cpython_fuzz.read_version_tags(versions_csv))
            | {
                cpython_fuzz.directory_name_to_tag(path.name)
                for path in (args.data_dir / "rq3").glob("cpython-*")
                if path.is_dir()
            }
        )
        tags = sorted(tag for tag in tags if tag)
    if not tags:
        raise SystemExit("no RQ4 CPython versions found. Run pyclens fuzz-cpython first.")
    print("RQ4 CPython versions: " + ", ".join(tags))
    rows = source_repro.analyze_reproducibility(
        tags,
        data_dir=args.data_dir,
        timeout=args.timeout,
        workers=args.workers,
    )
    csv_out = args.data_dir / "rq4" / "source_reproduction.csv"
    finding_csv = args.data_dir / "rq4" / "source_reproduction_findings.csv"
    failure_csv = args.data_dir / "rq4" / "source_reproduction_tool_failures.csv"
    summary_csv = args.data_dir / "rq4" / "rq4_summary.csv"
    source_repro.write_csv(csv_out, rows)
    source_repro.write_finding_report_csv(finding_csv, rows)
    source_repro.write_tool_failure_csv(failure_csv, rows)
    source_repro.write_summary_csv(summary_csv, rows)
    findings = {row.finding for row in rows}
    reproduced = {row.finding for row in rows if row.reproduced}
    print(
        "RQ4 summary: findings={findings}, tool_reproduced={reproduced}, not_reproduced_by_selected_tools={not_reproduced}".format(
            findings=len(findings),
            reproduced=len(reproduced),
            not_reproduced=len(findings - reproduced),
        )
    )
    print(f"wrote RQ4 source reproduction report to {csv_out}")
    print(f"wrote RQ4 finding report to {finding_csv}")
    print(f"wrote RQ4 tool-failure report to {failure_csv}")
    print(f"wrote RQ4 summary to {summary_csv}")
    return 0


def analyze_crashes(args: argparse.Namespace) -> int:
    print("[RQ3] analyzing and deduplicating fuzzing crash findings")
    findings, unique_bugs = crash_analysis.analyze_crashes(
        data_dir=args.data_dir,
        tags=args.versions,
        timeout=args.timeout,
        include_timeouts=args.include_timeouts,
    )
    finding_csv = args.data_dir / "rq3" / "crash_findings.csv"
    unique_csv = args.data_dir / "rq3" / "unique_bugs.csv"
    summary_csv = args.data_dir / "rq3" / "crash_summary.csv"
    bug_type_csv = args.data_dir / "rq3" / "bug_type_summary.csv"
    bug_context_csv = args.data_dir / "rq3" / "bug_context_summary.csv"
    bug_type_by_version_csv = args.data_dir / "rq3" / "bug_type_by_version.csv"
    bug_context_by_version_csv = args.data_dir / "rq3" / "bug_context_by_version.csv"
    report_md = args.data_dir / "rq3" / "unique_bug_report.md"
    crash_analysis.write_finding_csv(finding_csv, findings)
    crash_analysis.write_unique_csv(unique_csv, unique_bugs)
    benchmark_unique_csvs = crash_analysis.write_benchmark_unique_csvs(args.data_dir / "rq3", unique_bugs)
    crash_analysis.write_summary_csv(summary_csv, findings, unique_bugs)
    crash_analysis.write_bug_type_summary_csv(bug_type_csv, unique_bugs)
    crash_analysis.write_bug_context_summary_csv(bug_context_csv, unique_bugs)
    crash_analysis.write_bug_type_by_version_csv(bug_type_by_version_csv, unique_bugs)
    crash_analysis.write_bug_context_by_version_csv(bug_context_by_version_csv, unique_bugs)
    crash_analysis.write_unique_report(report_md, findings, unique_bugs)
    benchmark_reports = crash_analysis.write_benchmark_unique_reports(args.data_dir / "rq3", findings, unique_bugs)
    print(
        "RQ3 crash analysis summary: findings={findings}, unique_bugs={unique}".format(
            findings=len(findings),
            unique=len(unique_bugs),
        )
    )
    print(f"wrote RQ3 crash findings to {finding_csv}")
    print(f"wrote RQ3 unique bugs to {unique_csv}")
    print(f"wrote benchmark-level unique bug CSVs: {len(benchmark_unique_csvs)}")
    for path in benchmark_unique_csvs:
        print(f"  {path}")
    print(f"wrote RQ3 crash summary to {summary_csv}")
    print(f"wrote RQ3 bug type summary to {bug_type_csv}")
    print(f"wrote RQ3 bug context summary to {bug_context_csv}")
    print(f"wrote RQ3 bug type by-version summary to {bug_type_by_version_csv}")
    print(f"wrote RQ3 bug context by-version summary to {bug_context_by_version_csv}")
    print(f"wrote RQ3 unique bug report to {report_md}")
    print(f"wrote benchmark-level unique bug reports: {len(benchmark_reports)}")
    for path in benchmark_reports:
        print(f"  {path}")
    print(f"wrote representative unique-bug pyc files under {args.data_dir / 'rq3'}/<cpython-version>/unique_bug_pyc")
    return 0


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


def add_prepare_inputs_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "prepare-inputs",
        help="Generate real dataset input lists under data/inputs.",
    )
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR, help="Root directory for dataset inputs")
    parser.add_argument("--pypi-package-file", type=Path)
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
    parser.add_argument("--pypi-size", default="all", help=argparse.SUPPRESS)
    parser.add_argument("--seed", type=int, default=0, help=argparse.SUPPRESS)
    parser.add_argument(
        "--include",
        choices=(*PYPI_DISTRIBUTIONS, "other"),
        action="append",
        default=None,
        help=argparse.SUPPRESS,
    )
    parser.add_argument("--max-files-per-kind", type=int, default=1, help=argparse.SUPPRESS)
    parser.add_argument("--timeout", type=int, default=60, help=argparse.SUPPRESS)
    parser.add_argument("--delay", type=float, default=0.2, help=argparse.SUPPRESS)
    parser.add_argument("--max-age-years", type=int, default=5, help=argparse.SUPPRESS)
    parser.add_argument("--items-per-source", type=int, help="Collect first N PyPI packages")
    parser.add_argument("--workers", type=int, default=8, help="Parallel workers for download and scan")
    parser.add_argument("--force", action="store_true", help="Redownload or recopy collected artifacts")
    parser.add_argument("--force-inputs", action="store_true", help="Regenerate dataset input lists")
    parser.add_argument("--prepare", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--quiet", action="store_true", help="Reduce collector progress output")
    parser.set_defaults(func=run_pipeline, out_dir=None, csv_out=None, json_out=None)


def add_smoke_test_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "smoke-test",
        help="Collect and scan a 1k-item PyPI sample.",
    )
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_SMOKE_DATA_DIR, help="Root directory for smoke-test data")
    parser.add_argument("--items-per-source", type=int, default=DEFAULT_SMOKE_ITEMS_PER_SOURCE, help="PyPI packages to collect")
    parser.add_argument("--workers", type=int, default=8, help="Parallel workers for download and scan")
    parser.add_argument("--force", action="store_true", help="Redownload collected artifacts")
    parser.add_argument("--force-inputs", action="store_true", help="Regenerate the PyPI smoke package list")
    parser.add_argument("--quiet", action="store_true", help="Reduce collector progress output")
    parser.add_argument("--seed", type=int, default=0, help=argparse.SUPPRESS)
    parser.add_argument("--timeout", type=int, default=60, help=argparse.SUPPRESS)
    parser.add_argument("--delay", type=float, default=0.2, help=argparse.SUPPRESS)
    parser.add_argument("--max-age-years", type=int, default=5, help=argparse.SUPPRESS)
    parser.set_defaults(
        func=smoke_test,
        out_dir=None,
        csv_out=None,
        json_out=None,
        include=None,
        max_files_per_kind=1,
    )


def add_collect_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "collect",
        help="Collect configured PyPI packages from data/inputs.",
    )
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR, help="Root directory for collected data")
    parser.add_argument("--pypi-package-file", type=Path)
    parser.add_argument(
        "--include",
        choices=(*PYPI_DISTRIBUTIONS, "other"),
        action="append",
        default=None,
        help="Artifact kind to collect; defaults to wheel and sdist",
    )
    parser.add_argument("--max-files-per-kind", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--delay", type=float, default=0.2)
    parser.add_argument("--max-age-years", type=int, default=5, help="Only collect artifacts uploaded within this many years; use 0 for no age filter")
    parser.add_argument("--items-per-source", type=int, help="Collect first N PyPI packages")
    parser.add_argument("--workers", type=int, default=8, help="Parallel package download workers")
    parser.add_argument("--force", action="store_true", help="Redownload or recopy files that already exist")
    parser.add_argument("--quiet", action="store_true", help="Only print final summaries")
    parser.set_defaults(func=collect_all, out_dir=None, csv_out=None, json_out=None)


def add_collect_pypi_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "collect-pypi",
        help="Collect PyPI release metadata and distribution artifacts.",
    )
    add_collection_arguments(parser)


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


def add_analyze_tools_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "analyze-tools",
        help="RQ2: evaluate practical analyzability of discovered bytecode artifacts.",
    )
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR, help="Root directory for study data")
    parser.add_argument("--scan-csv", type=Path, help="Bytecode scan CSV; defaults to data/scan/bytecode_scan.csv")
    parser.add_argument("--csv-out", type=Path, help="Tool-analysis CSV; defaults to data/rq2/tool_analysis.csv")
    parser.add_argument("--workers", type=int, default=8, help="Parallel artifact analysis workers")
    parser.add_argument("--limit", type=int, help="Analyze only the first N bytecode-containing artifacts")
    parser.add_argument("--timeout", type=int, default=600, help="Per-.pyc timeout in seconds for each external analysis tool")
    parser.add_argument("--count-only", action="store_true", help="Only count RQ2 in-scope .pyc files and write denominator audit reports")
    parser.set_defaults(func=analyze_tools)


def add_collect_failed_cases_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "collect-failed-cases",
        help="RQ2: rebuild failed .pyc replay corpus from an existing tool_analysis.csv without rerunning analysis.",
    )
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR, help="Root directory for study data")
    parser.add_argument("--csv-in", type=Path, help="Existing RQ2 tool-analysis CSV; defaults to data/rq2/tool_analysis.csv")
    parser.set_defaults(func=collect_failed_cases)



def add_summarize_rq1_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "summarize-rq1",
        help="RQ1: summarize bytecode exposure and packaging from scan outputs.",
    )
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR, help="Root directory for study data")
    parser.add_argument("--scan-csv", type=Path, help="Bytecode scan CSV; defaults to data/scan/bytecode_scan.csv")
    parser.add_argument("--versions-csv", type=Path, help="CPython version CSV; defaults to data/scan/cpython_versions.csv")
    parser.set_defaults(func=summarize_rq1)


def add_prepare_analysis_env_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "prepare-analysis-env",
        help="Prepare CPython-version-specific RQ2 tool environments.",
    )
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR, help="Root directory for study data")
    parser.add_argument("--timeout", type=int, default=300, help="Timeout for venv creation and tool installation")
    parser.set_defaults(func=prepare_analysis_env)


def add_fuzz_cpython_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "fuzz-cpython",
        help="RQ3: extract unittest seeds, compile .pyc seeds, and fuzz CPython bytecode processing.",
    )
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR, help="Root directory for study data")
    parser.add_argument("--workers", type=int, default=1, help="Honggfuzz worker count per CPython version")
    parser.add_argument("--duration", type=int, default=60, help="Honggfuzz runtime in seconds per CPython version")
    parser.add_argument("--timeout", type=int, default=10, help="Per-input timeout in seconds")
    parser.add_argument("--honggfuzz", type=Path, help="Path to honggfuzz binary; auto-detected by default")
    parser.add_argument("--no-instrument", dest="instrument", action="store_false", help=argparse.SUPPRESS)
    parser.add_argument("versions", nargs="*", help="Optional CPython versions to fuzz, such as 3.10 or cpython-310")
    parser.set_defaults(func=fuzz_cpython, instrument=True)


def add_smoke_rq3_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "smoke-rq3",
        help="Smoke test RQ3 for one CPython version using the real fuzz-cpython workflow.",
    )
    parser.add_argument("version", help="CPython version to test, such as 3.10 or cpython-310")
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_SMOKE_DATA_DIR, help="Root directory for smoke-test data")
    parser.add_argument("--workers", type=int, default=1, help="Honggfuzz worker count")
    parser.add_argument("--duration", type=int, default=5, help="Honggfuzz runtime in seconds")
    parser.add_argument("--timeout", type=int, default=5, help="Per-input timeout in seconds")
    parser.add_argument("--honggfuzz", type=Path, help="Path to honggfuzz binary; auto-detected by default")
    parser.set_defaults(func=smoke_rq3)


def add_reproduce_source_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "reproduce-source",
        help="RQ4: check whether RQ3 bytecode findings are reproducible from ordinary source.",
    )
    parser.add_argument("versions", nargs="*", help="Optional CPython versions to analyze, such as 3.10 or cpython-310")
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR, help="Root directory for study data")
    parser.add_argument("--timeout", type=int, default=600, help="Per-finding timeout in seconds")
    parser.add_argument("--workers", type=int, default=1, help="Number of findings to analyze concurrently")
    parser.set_defaults(func=reproduce_source)


def replay_crashes(args: argparse.Namespace) -> int:
    print("[RQ3] replaying unique crash representatives")
    rows = crash_analysis.replay_unique_bugs_with_valgrind(
        data_dir=args.data_dir,
        tags=args.versions,
        timeout=args.timeout,
    )
    report_csv = args.data_dir / "rq3" / "valgrind_report.csv"
    summary_csv = args.data_dir / "rq3" / "valgrind_summary.csv"
    crash_analysis.write_valgrind_csv(report_csv, rows)
    benchmark_csvs = crash_analysis.write_benchmark_valgrind_csvs(args.data_dir / "rq3", rows)
    crash_analysis.write_valgrind_summary_csv(summary_csv, rows)
    print(f"RQ3 replay summary: unique_bugs={len(rows)}")
    print(f"wrote RQ3 Valgrind replay report to {report_csv}")
    print(f"wrote benchmark-level Valgrind replay CSVs: {len(benchmark_csvs)}")
    for path in benchmark_csvs:
        print(f"  {path}")
    print(f"wrote RQ3 Valgrind replay summary to {summary_csv}")
    return 0


def add_analyze_crashes_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "analyze-crashes",
        help="RQ3: reproduce and deduplicate CPython fuzzing crash findings.",
    )
    parser.add_argument("versions", nargs="*", help="Optional CPython versions to analyze, such as 3.10 or cpython-310")
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR, help="Root directory for study data")
    parser.add_argument("--timeout", type=int, default=10, help="Per-finding rerun timeout in seconds")
    parser.add_argument("--include-timeouts", action="store_true", help="Also deduplicate timeout findings, if timeout files were collected")
    parser.set_defaults(func=analyze_crashes)



def add_replay_crashes_parser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "replay-crashes",
        help="RQ3: replay stack-deduplicated crash representatives with Valgrind.",
    )
    parser.add_argument("versions", nargs="*", help="Optional CPython versions to replay, such as 3.10 or cpython-310")
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR, help="Root directory for study data")
    parser.add_argument("--timeout", type=int, default=120, help="Per-representative replay timeout in seconds")
    parser.set_defaults(func=replay_crashes)


def main(argv: Sequence[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    if not argv:
        argv = ["run"]
    elif argv[0] == "--fuzzing":
        argv = ["fuzz-cpython", *argv[1:]]
    elif argv[0] == "--reproduce-source":
        argv = ["reproduce-source", *argv[1:]]

    parser = argparse.ArgumentParser(
        description="PycLens empirical study tool for Python bytecode artifacts."
    )
    subparsers = parser.add_subparsers(dest="component", required=True)
    add_run_parser(subparsers)
    add_smoke_test_parser(subparsers)
    add_prepare_inputs_parser(subparsers)
    add_collect_parser(subparsers)
    add_collect_pypi_parser(subparsers)
    add_scan_parser(subparsers)
    add_summarize_rq1_parser(subparsers)
    add_prepare_analysis_env_parser(subparsers)
    add_analyze_tools_parser(subparsers)
    add_collect_failed_cases_parser(subparsers)
    add_fuzz_cpython_parser(subparsers)
    add_smoke_rq3_parser(subparsers)
    add_analyze_crashes_parser(subparsers)
    add_replay_crashes_parser(subparsers)
    add_reproduce_source_parser(subparsers)
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
