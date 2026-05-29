# pybcSEC

`pybcSEC` is a small Python package for the PyBC-Sec study. It supports two
early-study components:

1. `run`: run input preparation, collection, and scanning in sequence.
2. `prepare-inputs`: generate reproducible real-dataset input lists under
   `data/inputs/`.
3. `collect`: collect all configured real dataset sources from `data/inputs/`
   and write source-specific CSV manifests.
4. `collect-pypi`: collect ordinary PyPI release metadata and distribution
   artifacts.
5. `collect-suspicious-pypi`: collect suspicious or malicious PyPI package
   lists into a separate source directory.
6. `collect-local`: collect local bundles, archives, directories, or runtime
   corpus artifacts.
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
the latest 5 years. For a smaller smoke test:

```bash
pybcSEC run --pypi-size 1000
```

To change the recency window:

```bash
pybcSEC run --max-age-years 3
pybcSEC run --max-age-years 0   # disable the age filter
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

Collect local bundles or runtime corpus artifacts:

```bash
pybcSEC collect-local /path/to/bundle.whl /path/to/extracted-app
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
