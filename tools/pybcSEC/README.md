# pybcSEC

`pybcSEC` is a small Python package for the PyBC-Sec study. It supports two
early-study components:

1. `run`: run input preparation, collection, and scanning in sequence.
2. `smoke-test`: collect and scan a 1,000-item sample from each configured
   source.
3. `prepare-inputs`: generate reproducible real-dataset input lists under
   `data/inputs/`.
4. `collect`: collect all configured real dataset sources from `data/inputs/`
   and write source-specific CSV manifests.
5. `collect-pypi`: collect ordinary PyPI release metadata and distribution
   artifacts.
6. `collect-suspicious-pypi`: collect suspicious or malicious PyPI package
   lists into a separate source directory.
7. `collect-github-release`: collect downloadable assets from GitHub releases.
8. `scan`: scan package directories or distribution archives for bytecode
   evidence and write a CSV summary.

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
each source. It generates its own PyPI sample, and expects at least 1,000
entries in:

```text
data/inputs/suspicious_pypi_packages.txt
data/inputs/github_repositories.txt
```

You can also run phases manually:

```bash
pybcSEC prepare-inputs
pybcSEC collect
pybcSEC scan
```

By default, PyPI data is saved under:

```text
data/artifacts/pypi/
data/sources/pypi/manifest.csv
```

Other collectors use the same convention:

```text
data/artifacts/<source>/
data/sources/<source>/manifest.csv
```

Collect a study package list:

```bash
pybcSEC collect --package-file data/packages.txt
```

Collect suspicious PyPI packages from a curated list:

```bash
pybcSEC collect-suspicious-pypi --package-file data/suspicious_packages.txt
```

Collect GitHub release assets:

```bash
pybcSEC collect-github-release --repo owner/project
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
