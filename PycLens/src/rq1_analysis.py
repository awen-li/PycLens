"""RQ1 bytecode exposure and packaging analysis."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

from analysis import RQAnalyze


class RQ1Analyzer(RQAnalyze):
    """Summarize bytecode exposure and packaging structure from scan outputs."""

    def __init__(
        self,
        data_dir: Path,
        scan_csv: Path | None = None,
        versions_csv: Path | None = None,
    ) -> None:
        super().__init__(data_dir)
        self.scan_csv = scan_csv or data_dir / "scan" / "bytecode_scan.csv"
        self.versions_csv = versions_csv or data_dir / "scan" / "cpython_versions.csv"
        self.out_dir = data_dir / "rq1"

    def analyze(self) -> None:
        print("[RQ1] summarizing bytecode exposure and packaging")
        if not self.scan_csv.exists():
            raise SystemExit(f"scan CSV not found: {self.scan_csv}")

        self.out_dir.mkdir(parents=True, exist_ok=True)
        totals, by_type, version_counts, magic_counts = self._aggregate_scan()

        summary_csv = self.out_dir / "rq1_summary.csv"
        by_type_csv = self.out_dir / "rq1_by_type.csv"
        versions_out = self.out_dir / "rq1_versions.csv"
        visibility_csv = self.out_dir / "rq1_source_visibility.csv"
        packaging_csv = self.out_dir / "rq1_packaging_structure.csv"
        paper_table_csv = self.out_dir / "rq1_paper_table.csv"
        paper_text = self.out_dir / "rq1_paper_numbers.txt"

        self._write_metric_csv(summary_csv, totals)
        self._write_by_type_csv(by_type_csv, by_type)
        self._write_versions_csv(versions_out, version_counts, magic_counts)
        self._write_source_visibility_csv(visibility_csv, totals, by_type)
        self._write_packaging_structure_csv(packaging_csv, totals, by_type)
        self._write_paper_table(paper_table_csv, totals, by_type)
        self._write_paper_numbers(paper_text, totals, by_type, version_counts)

        artifacts = totals["artifacts"]
        with_bytecode = totals["artifacts_with_bytecode"]
        rate = (with_bytecode / artifacts) if artifacts else 0.0
        print(
            "RQ1 summary: artifacts={artifacts}, with_bytecode={with_bytecode}, "
            "rate={rate:.6f}, pyc_files={pyc}, source_less_pyc={source_less}, dynamic_hits={dynamic}".format(
                artifacts=artifacts,
                with_bytecode=with_bytecode,
                rate=rate,
                pyc=totals["pyc_files"],
                source_less=totals["source_less_pyc"],
                dynamic=totals["dynamic_load_hits"],
            )
        )
        print(f"wrote RQ1 summary to {summary_csv}")
        print(f"wrote RQ1 by-type summary to {by_type_csv}")
        print(f"wrote RQ1 version summary to {versions_out}")
        print(f"wrote RQ1 source-visibility summary to {visibility_csv}")
        print(f"wrote RQ1 packaging-structure summary to {packaging_csv}")
        print(f"wrote RQ1 paper table to {paper_table_csv}")
        print(f"wrote RQ1 paper numbers to {paper_text}")

    def _aggregate_scan(self) -> tuple[Counter[str], dict[str, Counter[str]], Counter[str], Counter[str]]:
        totals: Counter[str] = Counter()
        by_type: dict[str, Counter[str]] = {}
        version_counts: Counter[str] = Counter()
        magic_counts: Counter[str] = Counter()

        with self.scan_csv.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                input_type = row.get("input_type") or "unknown"
                bucket = by_type.setdefault(input_type, Counter())
                pyc_files = int(row.get("pyc_files") or 0)
                py_files = int(row.get("py_files") or 0)
                source_less = int(row.get("source_less_pyc") or 0)
                pycache_dirs = int(row.get("pycache_dirs") or 0)
                dynamic_hits = int(row.get("dynamic_load_hits") or 0)
                has_bytecode = row.get("has_bytecode") == "True" or pyc_files > 0 or pycache_dirs > 0
                has_dynamic = row.get("has_dynamic_loading") == "True" or dynamic_hits > 0

                self._add_counts(totals, py_files, pyc_files, pycache_dirs, source_less, dynamic_hits, has_bytecode, has_dynamic)
                self._add_counts(bucket, py_files, pyc_files, pycache_dirs, source_less, dynamic_hits, has_bytecode, has_dynamic)
                self._add_semicolon_counts(version_counts, row.get("pyc_versions", ""))
                self._add_semicolon_counts(magic_counts, row.get("magic_numbers", ""))

        return totals, by_type, version_counts, magic_counts

    @staticmethod
    def _add_counts(
        counts: Counter[str],
        py_files: int,
        pyc_files: int,
        pycache_dirs: int,
        source_less: int,
        dynamic_hits: int,
        has_bytecode: bool,
        has_dynamic: bool,
    ) -> None:
        counts["artifacts"] += 1
        counts["py_files"] += py_files
        counts["pyc_files"] += pyc_files
        counts["pycache_dirs"] += pycache_dirs
        counts["source_less_pyc"] += source_less
        counts["dynamic_load_hits"] += dynamic_hits
        counts["artifacts_with_bytecode"] += int(has_bytecode)
        counts["artifacts_with_pyc"] += int(pyc_files > 0)
        counts["artifacts_with_pycache"] += int(pycache_dirs > 0)
        counts["artifacts_with_source_less_pyc"] += int(source_less > 0)
        counts["artifacts_with_dynamic_loading"] += int(has_dynamic)

    @staticmethod
    def _add_semicolon_counts(counter: Counter[str], text: str) -> None:
        for item in (text or "").split(";"):
            if not item:
                continue
            name, _, raw_count = item.partition(":")
            if not name:
                continue
            try:
                count = int(raw_count or "1")
            except ValueError:
                count = 1
            counter[name] += count

    @staticmethod
    def _write_metric_csv(path: Path, totals: Counter[str]) -> None:
        fieldnames = ["metric", "value"]
        rows = [{"metric": key, "value": totals[key]} for key in sorted(totals)]
        artifacts = totals["artifacts"]
        rows.extend(
            [
                {
                    "metric": "bytecode_artifact_rate",
                    "value": f"{totals['artifacts_with_bytecode'] / artifacts:.8f}" if artifacts else "0",
                },
                {
                    "metric": "source_less_pyc_rate_per_pyc",
                    "value": f"{totals['source_less_pyc'] / totals['pyc_files']:.8f}" if totals["pyc_files"] else "0",
                },
            ]
        )
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    @staticmethod
    def _write_by_type_csv(path: Path, by_type: dict[str, Counter[str]]) -> None:
        fieldnames = [
            "input_type",
            "artifacts",
            "artifacts_with_bytecode",
            "bytecode_artifact_rate",
            "artifacts_with_pyc",
            "artifacts_with_pycache",
            "artifacts_with_source_less_pyc",
            "artifacts_with_dynamic_loading",
            "py_files",
            "pyc_files",
            "pycache_dirs",
            "source_less_pyc",
            "dynamic_load_hits",
        ]
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            for input_type, counts in sorted(by_type.items()):
                artifacts = counts["artifacts"]
                row = {key: counts[key] for key in fieldnames if key != "input_type"}
                row["input_type"] = input_type
                row["bytecode_artifact_rate"] = f"{counts['artifacts_with_bytecode'] / artifacts:.8f}" if artifacts else "0"
                writer.writerow(row)

    @staticmethod
    def _write_source_visibility_csv(path: Path, totals: Counter[str], by_type: dict[str, Counter[str]]) -> None:
        fieldnames = [
            "group",
            "pyc_files",
            "source_backed_pyc",
            "source_backed_pyc_pct",
            "source_less_pyc",
            "source_less_pyc_pct",
            "artifacts_with_source_less_pyc",
        ]
        rows = [RQ1Analyzer._source_visibility_row("All", totals)]
        for input_type, counts in sorted(by_type.items()):
            rows.append(RQ1Analyzer._source_visibility_row(input_type, counts))
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    @staticmethod
    def _source_visibility_row(group: str, counts: Counter[str]) -> dict[str, str | int]:
        pyc_files = counts["pyc_files"]
        source_less = counts["source_less_pyc"]
        source_backed = max(pyc_files - source_less, 0)
        return {
            "group": group,
            "pyc_files": pyc_files,
            "source_backed_pyc": source_backed,
            "source_backed_pyc_pct": percent(source_backed, pyc_files),
            "source_less_pyc": source_less,
            "source_less_pyc_pct": percent(source_less, pyc_files),
            "artifacts_with_source_less_pyc": counts["artifacts_with_source_less_pyc"],
        }

    @staticmethod
    def _write_packaging_structure_csv(path: Path, totals: Counter[str], by_type: dict[str, Counter[str]]) -> None:
        fieldnames = [
            "group",
            "artifacts",
            "artifacts_with_bytecode",
            "bytecode_artifact_pct",
            "artifacts_with_pyc",
            "artifacts_with_pycache",
            "pycache_among_bytecode_artifacts_pct",
            "pyc_files",
            "pyc_per_bytecode_artifact",
            "pycache_dirs",
            "source_less_pyc",
            "source_less_pyc_pct",
            "artifacts_with_dynamic_loading",
            "dynamic_loading_artifact_pct",
        ]
        rows = [RQ1Analyzer._packaging_structure_row("All", totals)]
        for input_type, counts in sorted(by_type.items()):
            rows.append(RQ1Analyzer._packaging_structure_row(input_type, counts))
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    @staticmethod
    def _packaging_structure_row(group: str, counts: Counter[str]) -> dict[str, str | int]:
        artifacts = counts["artifacts"]
        with_bytecode = counts["artifacts_with_bytecode"]
        pyc_files = counts["pyc_files"]
        return {
            "group": group,
            "artifacts": artifacts,
            "artifacts_with_bytecode": with_bytecode,
            "bytecode_artifact_pct": percent(with_bytecode, artifacts),
            "artifacts_with_pyc": counts["artifacts_with_pyc"],
            "artifacts_with_pycache": counts["artifacts_with_pycache"],
            "pycache_among_bytecode_artifacts_pct": percent(counts["artifacts_with_pycache"], with_bytecode),
            "pyc_files": pyc_files,
            "pyc_per_bytecode_artifact": f"{pyc_files / with_bytecode:.2f}" if with_bytecode else "0.00",
            "pycache_dirs": counts["pycache_dirs"],
            "source_less_pyc": counts["source_less_pyc"],
            "source_less_pyc_pct": percent(counts["source_less_pyc"], pyc_files),
            "artifacts_with_dynamic_loading": counts["artifacts_with_dynamic_loading"],
            "dynamic_loading_artifact_pct": percent(counts["artifacts_with_dynamic_loading"], artifacts),
        }

    def _write_versions_csv(self, path: Path, version_counts: Counter[str], magic_counts: Counter[str]) -> None:
        fieldnames = ["kind", "name", "count", "interpreter"]
        rows = []
        interpreter_by_tag = {}
        if self.versions_csv.exists():
            with self.versions_csv.open(newline="", encoding="utf-8") as handle:
                for row in csv.DictReader(handle):
                    tag = row.get("python_tag", "")
                    if tag:
                        interpreter_by_tag[tag] = row.get("interpreter", "")
        for name, count in sorted(version_counts.items()):
            rows.append(
                {
                    "kind": "python_tag",
                    "name": name,
                    "count": count,
                    "interpreter": interpreter_by_tag.get(name, ""),
                }
            )
        for name, count in sorted(magic_counts.items()):
            rows.append({"kind": "magic_number", "name": name, "count": count, "interpreter": ""})
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    @staticmethod
    def _write_paper_table(path: Path, totals: Counter[str], by_type: dict[str, Counter[str]]) -> None:
        fieldnames = [
            "group",
            "artifacts",
            "with_bytecode",
            "with_bytecode_pct",
            "pyc_files",
            "source_less_pyc",
            "source_less_pyc_pct",
            "with_dynamic_loading",
            "with_dynamic_loading_pct",
        ]
        rows = [RQ1Analyzer._paper_row("All", totals)]
        for input_type, counts in sorted(by_type.items()):
            rows.append(RQ1Analyzer._paper_row(input_type, counts))
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    @staticmethod
    def _paper_row(group: str, counts: Counter[str]) -> dict[str, str | int]:
        artifacts = counts["artifacts"]
        pyc_files = counts["pyc_files"]
        return {
            "group": group,
            "artifacts": artifacts,
            "with_bytecode": counts["artifacts_with_bytecode"],
            "with_bytecode_pct": percent(counts["artifacts_with_bytecode"], artifacts),
            "pyc_files": pyc_files,
            "source_less_pyc": counts["source_less_pyc"],
            "source_less_pyc_pct": percent(counts["source_less_pyc"], pyc_files),
            "with_dynamic_loading": counts["artifacts_with_dynamic_loading"],
            "with_dynamic_loading_pct": percent(counts["artifacts_with_dynamic_loading"], artifacts),
        }

    @staticmethod
    def _write_paper_numbers(
        path: Path,
        totals: Counter[str],
        by_type: dict[str, Counter[str]],
        version_counts: Counter[str],
    ) -> None:
        artifacts = totals["artifacts"]
        with_bytecode = totals["artifacts_with_bytecode"]
        lines = [
            "RQ1 paper-ready numbers",
            "",
            f"Artifacts scanned: {artifacts}",
            f"Artifacts with bytecode: {with_bytecode} ({percent(with_bytecode, artifacts)})",
            f"Python source files: {totals['py_files']}",
            f"Bytecode files: {totals['pyc_files']}",
            f"Source-less bytecode files: {totals['source_less_pyc']} ({percent(totals['source_less_pyc'], totals['pyc_files'])} of .pyc files)",
            f"Source-backed bytecode files: {max(totals['pyc_files'] - totals['source_less_pyc'], 0)} ({percent(max(totals['pyc_files'] - totals['source_less_pyc'], 0), totals['pyc_files'])} of .pyc files)",
            f"Artifacts with pycache directories: {totals['artifacts_with_pycache']} ({percent(totals['artifacts_with_pycache'], with_bytecode)} of bytecode-containing artifacts)",
            f"Artifacts with dynamic-loading indicators: {totals['artifacts_with_dynamic_loading']} ({percent(totals['artifacts_with_dynamic_loading'], artifacts)})",
            "",
            "By artifact type:",
        ]
        for input_type, counts in sorted(by_type.items()):
            lines.append(
                "  {kind}: {with_bc}/{total} artifacts with bytecode ({rate}), {pyc} .pyc files, {src_less} source-less .pyc".format(
                    kind=input_type,
                    with_bc=counts["artifacts_with_bytecode"],
                    total=counts["artifacts"],
                    rate=percent(counts["artifacts_with_bytecode"], counts["artifacts"]),
                    pyc=counts["pyc_files"],
                    src_less=counts["source_less_pyc"],
                )
            )
        lines.extend(["", "Packaging structure by artifact type:"])
        for input_type, counts in sorted(by_type.items()):
            with_bc = counts["artifacts_with_bytecode"]
            pyc_files = counts["pyc_files"]
            lines.append(
                "  {kind}: pycache in {pycache}/{with_bc} bytecode artifacts ({pycache_rate}); "
                "{source_less} source-less .pyc ({source_less_rate}); {pyc_per} .pyc files per bytecode artifact".format(
                    kind=input_type,
                    pycache=counts["artifacts_with_pycache"],
                    with_bc=with_bc,
                    pycache_rate=percent(counts["artifacts_with_pycache"], with_bc),
                    source_less=counts["source_less_pyc"],
                    source_less_rate=percent(counts["source_less_pyc"], pyc_files),
                    pyc_per=f"{pyc_files / with_bc:.2f}" if with_bc else "0.00",
                )
            )
        lines.extend(["", "Observed bytecode version tags:"])
        if version_counts:
            for tag, count in sorted(version_counts.items()):
                lines.append(f"  {tag}: {count} .pyc files")
        else:
            lines.append("  none")
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def percent(numerator: int, denominator: int) -> str:
    if not denominator:
        return "0.00%"
    return f"{(numerator / denominator) * 100:.2f}%"
