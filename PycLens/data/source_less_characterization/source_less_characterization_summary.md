# Source-less Bytecode Characterization

Denominator: source-less `.pyc` rows retained in `data/rq2/tool_analysis.csv`, i.e., modern CPython bytecode in the RQ2 version-aware analysis scope. The full RQ1 scan inventory is not present in this local workspace, so these tables should not be mixed with the full RQ1 28,193-file denominator unless regenerated from the full scan CSV.

- Source-less `.pyc` files in this denominator: 21,541
- Source-less-containing artifacts: 1,387
- Source-less-containing packages: 1,046

## Q1 Metadata Taxonomy

### Distribution Type

| Artifact type | Source-less .pyc files | Percentage |
|---|---:|---:|
| tar | 13,636 | 63.30% |
| wheel | 7,856 | 36.47% |
| zip | 49 | 0.23% |

### Path Layout

| Layout | Source-less .pyc files | Percentage |
|---|---:|---:|
| pycache_import_cache | 14,186 | 65.86% |
| bare_pyc_module | 7,355 | 34.14% |

### Plausible Cause from Path Shape

| Plausible cause | Source-less .pyc files | Percentage |
|---|---:|---:|
| accidental_import_pycache | 7,925 | 36.79% |
| bare_compiled_only_module | 6,455 | 29.97% |
| bundled_environment_cache | 5,208 | 24.18% |
| accidental_test_pycache | 1,053 | 4.89% |
| bundled_environment_or_application | 538 | 2.50% |
| generated_or_build_artifact | 362 | 1.68% |

### Top Packages

| Package | Source-less .pyc files | Artifacts | Types | Versions |
|---|---:|---:|---|---|
| `bestfit` | 4,298 | 1 | tar | 0.3 |
| `lfedu` | 1,416 | 1 | tar | 0.0.1 |
| `optimeed` | 1,042 | 2 | tar;wheel | 2.5.3 |
| `tdw` | 561 | 1 | tar | 1.13.0.0 |
| `asyncchatpractice` | 537 | 1 | wheel | 0.1.3 |
| `xdis` | 458 | 1 | tar | 6.3.0 |
| `oracle-automlx` | 449 | 1 | wheel | 25.3.1 |
| `oracle-ml-insights` | 400 | 1 | wheel | 1.3.1 |
| `pykage` | 340 | 1 | tar | 0.2 |
| `isage-sage-benchmark` | 326 | 2 | tar;wheel | 0.1.0.6 |
| `uiflow2` | 264 | 1 | wheel | 0.0.5 |
| `igrep-tme` | 260 | 1 | wheel | 0.1.79 |
| `huangjb-sqlalchemy` | 256 | 1 | wheel | 2.0.41 |
| `wecon-sqlalchemy` | 256 | 1 | wheel | 2.0.41 |
| `leafmesh` | 170 | 1 | wheel | 2.2.46 |
| `isagellm-core` | 164 | 2 | tar;wheel | 0.5.4.26 |
| `reviewboardpowerpack` | 158 | 1 | wheel | 6.0 |
| `sf-pipelines-test` | 158 | 1 | tar | 0.3.0 |
| `sf-pipelines-test2` | 158 | 1 | tar | 0.1.0 |
| `isagellm-backend` | 148 | 2 | tar;wheel | 0.5.4.17 |

## Q3 Keyword-Flagged Artifacts

- Keyword-flagged source-less artifacts: 64

| Category | Artifacts | Percentage of keyword-flagged artifacts |
|---|---:|---:|
| security | 64 | 100.00% |
| network | 25 | 39.06% |
| data | 16 | 25.00% |
| testing | 16 | 25.00% |
| cli | 9 | 14.06% |
| build | 8 | 12.50% |
| ml | 8 | 12.50% |
| plugin | 5 | 7.81% |

Top keyword-flagged artifacts by source-less file count are in `q3_keyword_flagged_artifacts.csv`. Keyword definitions are in `q3_keyword_definitions.json`.
