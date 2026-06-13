# pybcSEC

`pybcSEC` is a small Python package for the PyBC-Sec study. It supports two
early-study components:

1. `run`: run input preparation, collection, and scanning in sequence.
2. `smoke-test`: collect and scan a 1,000-item PyPI sample.
3. `prepare-inputs`: generate reproducible real-dataset input lists under
   `data/inputs/`.
4. `collect`: collect configured PyPI packages from `data/inputs/` and write
   a CSV manifest.
5. `collect-pypi`: collect ordinary PyPI release metadata and distribution
   artifacts.
6. `scan`: scan package directories or distribution archives for bytecode
   evidence and write a CSV summary.
7. `analyze-tools`: run the RQ2 practical analyzability analysis on discovered
   bytecode artifacts.
8. `fuzz-cpython`: run the RQ3 CPython bytecode fuzzing campaign with
   honggfuzz.

Install the tool in editable mode:

```bash
python3 -m pip install -e tools/pybcSEC
```

Run the full default pipeline:

```bash
pybcSEC
```

This prepares the PyPI input list, collects artifacts, and scans the unified
artifact directory. By default, the PyPI list contains all package names from
the PyPI simple index, and collection downloads only artifacts uploaded within
the latest 5 years.

```bash
pybcSEC smoke-test
```

The smoke test writes to `data/smoke/` by default and uses 1,000 items from
PyPI. It generates its own PyPI sample from the PyPI simple index.

You can also run phases manually:

```bash
pybcSEC prepare-inputs
pybcSEC collect
pybcSEC scan
```

To collect a fixed-size PyPI slice:

```bash
pybcSEC collect --items-per-source 1000
```

By default, PyPI data is saved under:

```text
data/artifacts/pypi/
data/sources/pypi/manifest.csv
```

Collect a study package list:

```bash
pybcSEC collect --package-file data/packages.txt
```

Scan the collected artifacts:

```bash
pybcSEC scan
```

By default, scan results are saved under:

```text
data/scan/bytecode_scan.csv
```

The scanner is package-oriented: pass an extracted package directory, a wheel,
or a source distribution archive. With no input path, it scans the unified
collector output under `data/artifacts/`.

Summarize RQ1 after scanning:

```bash
pybcSEC summarize-rq1
```

This writes the bytecode exposure, source-visibility, packaging-structure, and
version summaries to:

```text
data/rq1/rq1_summary.csv
data/rq1/rq1_by_type.csv
data/rq1/rq1_source_visibility.csv
data/rq1/rq1_packaging_structure.csv
data/rq1/rq1_versions.csv
data/rq1/rq1_paper_table.csv
data/rq1/rq1_paper_numbers.txt
```

The source-visibility summary separates source-backed and source-less `.pyc`
files under the conservative artifact-local check. The packaging-structure
summary reports artifact type, pycache presence, `.pyc` density, source-less
bytecode, dynamic-loading indicators, and bytecode version evidence.

Run the RQ2 tool analyzability analysis after scanning:

```bash
pybcSEC prepare-analysis-env
pybcSEC analyze-tools
```

By default, this reads `data/scan/bytecode_scan.csv`, reopens only artifacts
that contain bytecode, and writes one row per `.pyc` file to:

```text
data/rq2/tool_analysis.csv
```

The RQ2 CSV includes per-tool statuses and an overall analyzability level:

```text
0 = not analyzable by any selected tool
1 = loadable only
2 = disassemblable
3 = partially decompilable by locally available decompilers
4 = fully decompilable by locally available decompilers
```

Each tool also has a `*_reason` column. For failures, this records the concrete
reason, such as a timeout, process exit status, exception type, or a short
stderr/stdout excerpt. The `python_tag` column records version tags from `.pyc`
filenames, such as `cpython-38` or `cpython-39`, to help diagnose compatibility
issues.

`prepare-analysis-env` reads `data/rq1/rq1_versions.csv`, checks for the
required `pythonX.Y` interpreters, creates per-version virtual environments
under `data/rq2/envs/`, and installs `uncompyle6` and `decompyle3` in those
environments. `pylingual` is intentionally treated as a global tool and is not
installed per interpreter.

Interpreter handling is automatic. The tool checks existing prepared
environments, `PATH`, common system locations, pyenv/asdf locations, and
manylinux-style `/opt/python/cpXY-cpXY/bin/python` paths. If a required
interpreter is missing, it first ensures `uv` is available, installs `uv` with
pip when necessary, and then runs `uv python install X.Y`. If that path fails,
it falls back to `apt-get` or `pyenv` when available; otherwise the missing
interpreter is reported in `data/rq2/analysis_environment.csv`.

RQ2 also writes reproducibility and paper-table outputs:

```text
data/rq2/tool_versions.csv
data/rq2/rq2_summary.csv
```

Run the RQ3 CPython fuzzing campaign:

```bash
pybcSEC prepare-analysis-env
```

```bash
pybcSEC --fuzzing 3.10 --workers 6 --duration 3600
```

The explicit command is equivalent:

```bash
pybcSEC fuzz-cpython 3.10 --workers 6 --duration 3600
```

Run a short smoke test for one CPython version:

```bash
pybcSEC smoke-rq3 3.10
```

After fuzzing, reproduce and deduplicate crash findings for RQ3:

```bash
pybcSEC analyze-crashes
```

This reruns saved crash inputs under the matching version-specific CPython
harness and writes:

```text
data/rq3/crash_findings.csv
data/rq3/unique_bugs.csv
data/rq3/crash_summary.csv
data/rq3/unique_bug_report.md
data/rq3/<cpython-version>/unique_bugs.csv
data/rq3/<cpython-version>/unique_bug_pyc/
```

`unique_bug_pyc/` contains one representative `.pyc` input for each unique
stack-signature bug and is the compact artifact corpus for RQ3. Use
`--include-timeouts` if timeout files should be grouped together with crash
findings.

Without a version argument, RQ3 fuzzes all CPython versions involved in the
study. RQ3 expects the required base interpreters to have been prepared by
`prepare-analysis-env`; it does not install CPython environments itself. For
each version, pybcSEC downloads or reuses the matching CPython
source release, builds an instrumented interpreter with honggfuzz's compiler
wrapper, extracts source seeds from CPython's unittest suite, compiles those
seeds into version-matched `.pyc` files with the instrumented interpreter, and
then runs honggfuzz against a CPython bytecode execution harness. Reruns reuse
per-version directories such as `data/rq3/cpython-3.10/instrumented/` and
`data/rq3/cpython-3.10/seeds/`. If source preparation or instrumentation fails,
the full RQ3 command reports the failure rather than silently downgrading the
campaign.

Before running RQ3 from the repository, load the honggfuzz environment:

```bash
source tools/setenv.sh
```

`fuzz-cpython` uses the honggfuzz tree selected by `PYBCSEC_HONGGFUZZ_HOME`.
Full RQ3 fuzzing also requires `hfuzz-clang` or `hfuzz-gcc` in that tree.
`smoke-rq3` is intentionally uninstrumented and only checks the end-to-end
workflow.

RQ3 outputs are written under:

```text
data/rq3/bytecode_seeds.csv
data/rq3/fuzz_runs.csv
data/rq3/rq3_summary.csv
data/rq3/cpython-3.10/source/
data/rq3/cpython-3.10/unittest_seeds/raw/
data/rq3/cpython-3.10/seeds/
data/rq3/cpython-3.10/bytecode_seeds.csv
data/rq3/cpython-3.10/fuzz_runs.csv
data/rq3/cpython-3.10/rq3_summary.csv
data/rq3/cpython-3.10/instrumented/
data/rq3/cpython-3.10/fuzz/
data/rq3/cpython-3.10/fuzz/HONGGFUZZ.REPORT.TXT
data/rq3/cpython-3.10/fuzz/honggfuzz.log
data/rq3/cpython-3.10/fuzz/coverage_stats.csv
data/rq3/cpython-3.10/fuzz/crashes/
data/rq3/cpython-3.10/fuzz/timeouts/
```

Run the RQ4 source-reproduction analysis after RQ3:

```bash
pybcSEC --reproduce-source 3.10
```

RQ4 checks whether bytecode findings discovered in RQ3 can be reproduced
through ordinary source using the selected decompilation tools. The result is
tool-bounded: if no source candidate reproduces a finding, pybcSEC reports it
as `not_reproduced_by_selected_tools`, not as proof that no source-level
reproduction exists.

RQ4 outputs are written under:

```text
data/rq4/source_reproduction.csv
data/rq4/rq4_summary.csv
data/rq4/source_candidates/<cpython-tag>/
```
