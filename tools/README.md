# pybcSEC Study Tool

This directory contains `pybcSEC`, a small Python package for quickly testing
whether Python package artifacts contain bytecode. The package lives under
`tools/pybcSEC`.

## Components

1. `run`: run input preparation, collection, and scanning in sequence.
2. `prepare-inputs`: generate reproducible real-dataset input lists under
   `data/inputs/`.
3. `collect`: collect all configured real dataset sources from `data/inputs/`.
4. `collect-pypi`: ordinary PyPI release metadata and distribution artifacts.
5. `collect-suspicious-pypi`: suspicious or malicious PyPI package lists.
6. `collect-github-release`: downloadable GitHub release assets.
7. `scan`: bytecode evidence component. Scans local package artifacts and writes
   a CSV report.

## Example Workflow

Install the tool in editable mode:

```bash
python3 -m pip install -e tools/pybcSEC
```

Create a package list:

```bash
printf "requests\nnumpy\n" > /tmp/packages.txt
```

Run the full default pipeline:

```bash
pybcSEC
```

By default, the PyPI input list contains all package names from the PyPI simple
index, and collection downloads only artifacts uploaded within the latest 5
years. For a smaller smoke test:

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

All collectors publish scanner-facing artifacts under:

```text
data/artifacts/<source>/
data/sources/<source>/manifest.csv
```

Collect a study package list:

```bash
pybcSEC collect --package-file /tmp/packages.txt
```

Collect other study sources:

```bash
pybcSEC collect-suspicious-pypi --package-file data/suspicious_packages.txt
pybcSEC collect-github-release --repo owner/project
```

Scan collected artifacts:

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


Key columns in `bytecode_scan.csv`:

- `pyc_files`: number of `.pyc` files found.
- `pycache_dirs`: number of `__pycache__` directories found.
- `source_less_pyc`: `.pyc` files without obvious matching `.py` source.
- `has_bytecode`: whether the artifact contains bytecode evidence.
- `has_dynamic_loading`: whether static source patterns suggest dynamic loading
  of bytecode or code objects.
