# Tool Robustness Bug Report

This report merges RQ2 and RQ4 tool robustness failures by analysis tool. A unique bug signature is defined by tool, CPython version, failure type, normalized cause, and traceback location when available. Counts are tool-result counts; signatures are deduplicated failure patterns for developer triage, not confirmed upstream issue IDs.

## Overall Statistics

| Tool | RQ2 outcomes | RQ2 unique signatures | RQ4 outcomes | RQ4 unique signatures | Combined outcomes | Combined unique signatures |
|---|---:|---:|---:|---:|---:|---:|
| `decompyle3` | 373 | 12 | 33 | 12 | 406 | 23 |
| `Decompyle++` | 0 | 0 | 4 | 3 | 4 | 3 |
| `dis` | 45 | 3 | 0 | 0 | 45 | 3 |
| `marshal` | 2 | 1 | 0 | 0 | 2 | 1 |
| `pylingual` | 3 | 2 | 19 | 8 | 22 | 8 |
| **Total** | **423** | **18** | **56** | **23** | **479** | **38** |

## Tool: `decompyle3`

- Combined outcomes: 406
- Combined unique signatures: 23
- RQ2 outcomes/signatures: 373/12
- RQ4 outcomes/signatures: 33/12

| ID | Version | Failure | Cause | RQ2 | RQ4 | Total |
|---|---|---|---|---:|---:|---:|
| `decompyle3-01` | CPython 3.8 | `ValueError` | uncaught bad marshal data | 211 | 0 | 211 |
| `decompyle3-02` | CPython 3.9 | `ValueError` | uncaught bad marshal data | 86 | 0 | 86 |
| `decompyle3-03` | CPython 3.8 | `Timeout` | did not terminate within 600s | 42 | 1 | 43 |
| `decompyle3-04` | CPython 3.9 | `EOFError` | uncaught marshal data too short | 10 | 0 | 10 |
| `decompyle3-05` | CPython 3.8 | `IndexError` | constant index out of range | 0 | 8 | 8 |
| `decompyle3-06` | CPython 3.13 | `SIGSEGV` | process crashed with signal 11 | 0 | 6 | 6 |
| `decompyle3-07` | CPython 3.8 | `AssertionError` | empty assertion message | 5 | 0 | 5 |
| `decompyle3-08` | CPython 3.12 | `SIGSEGV` | process crashed with signal 11 | 0 | 4 | 4 |
| `decompyle3-09` | CPython 3.8 | `AssertionError` | comp_if_not_or invariant | 4 | 0 | 4 |
| `decompyle3-10` | CPython 3.8 | `AssertionError` | ifpoplaststmtc expected c_stmts | 4 | 0 | 4 |
| `decompyle3-11` | CPython 3.8 | `AssertionError` | list_comp invariant | 3 | 0 | 3 |
| `decompyle3-12` | CPython 3.8 | `IndexError` | jump target or bytecode offset out of range | 0 | 3 | 3 |
| `decompyle3-13` | CPython 3.8 | `AssertionError` | c_try_except handler invariant | 2 | 0 | 2 |
| `decompyle3-14` | CPython 3.8 | `AssertionError` | comp_if_or invariant | 2 | 0 | 2 |
| `decompyle3-15` | CPython 3.8 | `AssertionError` | comp_if_or_not invariant | 2 | 0 | 2 |
| `decompyle3-16` | CPython 3.8 | `AssertionError` | empty message | 0 | 2 | 2 |
| `decompyle3-17` | CPython 3.8 | `AssertionError` | empty message | 0 | 2 | 2 |
| `decompyle3-18` | CPython 3.8 | `IndexError` | constant index out of range | 0 | 2 | 2 |
| `decompyle3-19` | CPython 3.8 | `TypeError` | argument of type 'int' is not iterable | 0 | 2 | 2 |
| `decompyle3-20` | CPython 3.9 | `SystemError` | uncaught code-object construction exception | 2 | 0 | 2 |
| `decompyle3-21` | CPython 3.12 | `SIGABRT` | allocator/heap abort | 0 | 1 | 1 |
| `decompyle3-22` | CPython 3.8 | `SIGABRT` | fatal Python runtime error | 0 | 1 | 1 |
| `decompyle3-23` | CPython 3.8 | `TypeError` | malformed marshal loader state | 0 | 1 | 1 |

### `decompyle3-01` CPython 3.8: `ValueError` / uncaught bad marshal data

- Combined outcomes: 211
- RQ2 outcomes/signatures: 211/1
- RQ4 outcomes/signatures: 0/0
- Observed statuses: `exit_2`=211
- Stack signature: `xdis.load:load_module_from_file_object`

Reproduction commands:

RQ2 representative (`rq2-decompyle3-f4df89b05af4`):
```bash
data/rq2/envs/cpython-38/bin/decompyle3 data/rq2/failed_cases/delphai-search-utils-0.2.1-cpython-38-6ad6b0602a75.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ2 | `rq2-decompyle3-f4df89b05af4` | 211 | `delphai_search_utils-0.2.1.tar.gz::delphai_search_utils-0.2.1/delphai_search_utils/tests/__pycache__/test_utils.cpython-38-pytest-5.4.3.pyc` | `PycLens/data/rq2/tool_robustness_failures/cpython-38/cpython-38-decompyle3-delphai_search_utils-0.2.1.tar.gz-delphai_search_utils-0.2.1-delphai_searc/stdout.txt; PycLens/data/rq2/tool_robustness_failures/cpython-38/cpython-38-decompyle3-delphai_search_utils-0.2.1.tar.gz-delphai_search_utils-0.2.1-delphai_searc/stderr.txt` |

Duplicate/example inputs:
- `delphai_search_utils-0.2.1.tar.gz::delphai_search_utils-0.2.1/delphai_search_utils/tests/__pycache__/test_utils.cpython-38-pytest-5.4.3.pyc`
- `decompyle3-3.9.3.tar.gz::decompyle3-3.9.3/test/__pycache__/test_pyenvlib.cpython-38-PYTEST.pyc`
- `decompyle3-3.9.3.tar.gz::decompyle3-3.9.3/test/__pycache__/test_pythonlib.cpython-38-PYTEST.pyc`
- `decompyle3-3.9.3.tar.gz::decompyle3-3.9.3/test/__pycache__/test_unpy37.cpython-38-PYTEST.pyc`
- `decompyle3-3.9.3.tar.gz::decompyle3-3.9.3/test/decompyle/__pycache__/test_empty.cpython-38-PYTEST.pyc`

### `decompyle3-02` CPython 3.9: `ValueError` / uncaught bad marshal data

- Combined outcomes: 86
- RQ2 outcomes/signatures: 86/1
- RQ4 outcomes/signatures: 0/0
- Observed statuses: `exit_2`=86
- Stack signature: `xdis.load:load_module_from_file_object`

Reproduction commands:

RQ2 representative (`rq2-decompyle3-eb90200e3b11`):
```bash
data/rq2/envs/cpython-39/bin/decompyle3 data/rq2/failed_cases/clustcrdist-0.1.5-cpython-39-06d1d321521d.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ2 | `rq2-decompyle3-eb90200e3b11` | 86 | `clustcrdist-0.1.5-py2.py3-none-any.whl::clustcrdist/constants/modules/olga/__pycache__/__init__.cpython-39.pyc` | `PycLens/data/rq2/tool_robustness_failures/cpython-39/cpython-39-decompyle3-clustcrdist-0.1.5-py2.py3-none-any.whl-clustcrdist-constants-modules-olga-/stdout.txt; PycLens/data/rq2/tool_robustness_failures/cpython-39/cpython-39-decompyle3-clustcrdist-0.1.5-py2.py3-none-any.whl-clustcrdist-constants-modules-olga-/stderr.txt` |

Duplicate/example inputs:
- `clustcrdist-0.1.5-py2.py3-none-any.whl::clustcrdist/constants/modules/olga/__pycache__/__init__.cpython-39.pyc`
- `clustcrdist-0.1.5-py2.py3-none-any.whl::clustcrdist/constants/modules/olga/__pycache__/load_model.cpython-39.pyc`
- `clustcrdist-0.1.5-py2.py3-none-any.whl::clustcrdist/constants/modules/olga/__pycache__/sequence_generation.cpython-39.pyc`
- `clustcrdist-0.1.5-py2.py3-none-any.whl::clustcrdist/constants/modules/olga/__pycache__/utils.cpython-39.pyc`
- `clustcrdist-0.1.5-py2.py3-none-any.whl::clustcrdist/constants/modules/tcrdist/__pycache__/__init__.cpython-39.pyc`

### `decompyle3-03` CPython 3.8: `Timeout` / did not terminate within 600s

- Combined outcomes: 43
- RQ2 outcomes/signatures: 42/1
- RQ4 outcomes/signatures: 1/1
- Observed statuses: `timeout`=43
- Stack signature: `not available`

Reproduction commands:

RQ2 representative (`rq2-decompyle3-6009e4188f1c`):
```bash
data/rq2/envs/cpython-38/bin/decompyle3 data/rq2/failed_cases/astromorphlib-1.0.13-cpython-38-1a9217268814.pyc
```
RQ4 representative (`rq4-decompyle3-6009e4188f1c`):
```bash
/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/bin/decompyle3 data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-74d96dc3cf62.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ2 | `rq2-decompyle3-6009e4188f1c` | 42 | `astromorphlib-1.0.13.tar.gz::astromorphlib-1.0.13/stat_lib/__pycache__/__init__.cpython-38.pyc` | `PycLens/data/rq2/tool_robustness_failures/cpython-38/cpython-38-decompyle3-astromorphlib-1.0.13.tar.gz-astromorphlib-1.0.13-stat_lib-__pycache__-__in/stdout.txt; PycLens/data/rq2/tool_robustness_failures/cpython-38/cpython-38-decompyle3-astromorphlib-1.0.13.tar.gz-astromorphlib-1.0.13-stat_lib-__pycache__-__in/stderr.txt` |
| RQ4 | `rq4-decompyle3-6009e4188f1c` | 1 | `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-74d96dc3cf62.pyc` | `data/rq4/tool_traces/cpython-38/cpython-38-74d96dc3cf62/decompyle3.stdout.txt; data/rq4/tool_traces/cpython-38/cpython-38-74d96dc3cf62/decompyle3.stderr.txt` |

Duplicate/example inputs:
- `astromorphlib-1.0.13.tar.gz::astromorphlib-1.0.13/stat_lib/__pycache__/__init__.cpython-38.pyc`
- `astromorphlib-1.0.13-py3-none-any.whl::stat_lib/__pycache__/__init__.cpython-38.pyc`
- `cbapi-patched-1.7.5.linux-x86_64.tar.gz::home/fsantos/opt/pyenv/versions/hunts/lib/python3.8/site-packages/cbapi/__pycache__/winerror.cpython-38.pyc`
- `dovado_rtl-0.10.12.tar.gz::dovado_rtl-0.10.12/dovado_rtl/parsers/utilities/antlr/__pycache__/vhdlParser.cpython-38.pyc`
- `flask_admin_plus-1.6.22.tar.gz::flask_admin_plus-1.6.22/flask_admin/tests/mongoengine/__pycache__/test_basic.cpython-38-pytest-7.1.2.pyc`
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-74d96dc3cf62.pyc`

Trace excerpt from `data/rq4/tool_traces/cpython-38/cpython-38-74d96dc3cf62/decompyle3.stderr.txt`:
```text
timeout_after_600s
```

### `decompyle3-04` CPython 3.9: `EOFError` / uncaught marshal data too short

- Combined outcomes: 10
- RQ2 outcomes/signatures: 10/1
- RQ4 outcomes/signatures: 0/0
- Observed statuses: `exit_2`=10
- Stack signature: `xdis.load:load_module_from_file_object`

Reproduction commands:

RQ2 representative (`rq2-decompyle3-e17af279bca3`):
```bash
data/rq2/envs/cpython-39/bin/decompyle3 data/rq2/failed_cases/clustcrdist-0.1.5-cpython-39-06d1d321521d.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ2 | `rq2-decompyle3-e17af279bca3` | 10 | `clustcrdist-0.1.5-py2.py3-none-any.whl::clustcrdist/constants/modules/olga/__pycache__/generation_probability.cpython-39.pyc` | `PycLens/data/rq2/tool_robustness_failures/cpython-39/cpython-39-decompyle3-clustcrdist-0.1.5-py2.py3-none-any.whl-clustcrdist-constants-modules-olga-/stdout.txt; PycLens/data/rq2/tool_robustness_failures/cpython-39/cpython-39-decompyle3-clustcrdist-0.1.5-py2.py3-none-any.whl-clustcrdist-constants-modules-olga-/stderr.txt` |

Duplicate/example inputs:
- `clustcrdist-0.1.5-py2.py3-none-any.whl::clustcrdist/constants/modules/olga/__pycache__/generation_probability.cpython-39.pyc`
- `clustcrdist-0.1.5-py2.py3-none-any.whl::clustcrdist/constants/modules/olga/__pycache__/preprocess_generative_model_and_data.cpython-39.pyc`
- `clustcrdist-0.1.5-py2.py3-none-any.whl::clustcrdist/constants/modules/tcrdist/__pycache__/tcr_distances_blosum.cpython-39.pyc`
- `clustcrdist-0.1.5-py2.py3-none-any.whl::clustcrdist/constants/modules/tcrdist/__pycache__/util.cpython-39.pyc`
- `clustcrdist-0.1.5.tar.gz::clustcrdist-0.1.5/clustcrdist/constants/modules/olga/__pycache__/generation_probability.cpython-39.pyc`

### `decompyle3-05` CPython 3.8: `IndexError` / constant index out of range

- Combined outcomes: 8
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 8/1
- Observed statuses: `exit_1`=8
- Stack signature: `site-packages/decompyle3/scanners/scanner37.py:ingest <- site-packages/decompyle3/scanners/scanner37base.py:ingest <- site-packages/decompyle3/scanner.py:build_instructions <- site-packages/xdis/bytecode.py:get_instructions_bytes <- site-packages/xdis/bytecode.py:get_logical_instruction_at_offset <- site-packages/xdis/bytecode.py:get_const_info`

Reproduction commands:

RQ4 representative (`rq4-decompyle3-34887820cf0f`):
```bash
/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/bin/decompyle3 data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-1023437964e6.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ4 | `rq4-decompyle3-34887820cf0f` | 8 | `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-1023437964e6.pyc` | `data/rq4/tool_traces/cpython-38/cpython-38-1023437964e6/decompyle3.stdout.txt; data/rq4/tool_traces/cpython-38/cpython-38-1023437964e6/decompyle3.stderr.txt` |

Duplicate/example inputs:
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-1023437964e6.pyc`
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-05df3261717a.pyc`
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-428375de16b7.pyc`
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-7b90ad31f7e8.pyc`
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-c18f3ce00206.pyc`

Trace excerpt from `data/rq4/tool_traces/cpython-38/cpython-38-1023437964e6/decompyle3.stderr.txt`:
```text
Traceback (most recent call last):
  File "data/rq2/envs/cpython-38/bin/decompyle3", line 8, in <module>
    sys.exit(main_bin())
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1161, in __call__
    return self.main(*args, **kwargs)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1082, in main
    rv = self.invoke(ctx)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1443, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 788, in invoke
    return __callback(*args, **kwargs)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/decompyle3/bin/decompile.py", line 175, in main_bin
```

### `decompyle3-06` CPython 3.13: `SIGSEGV` / process crashed with signal 11

- Combined outcomes: 6
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 6/1
- Observed statuses: `exit_-11`=6
- Stack signature: `not available`

Reproduction commands:

RQ4 representative (`rq4-decompyle3-205cb50c5c0c`):
```bash
/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-313/bin/decompyle3 data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-089a998b290e.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ4 | `rq4-decompyle3-205cb50c5c0c` | 6 | `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-089a998b290e.pyc` | `data/rq4/tool_traces/cpython-313/cpython-313-089a998b290e/decompyle3.stdout.txt; data/rq4/tool_traces/cpython-313/cpython-313-089a998b290e/decompyle3.stderr.txt` |

Duplicate/example inputs:
- `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-089a998b290e.pyc`
- `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-437dc676a244.pyc`
- `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-67ca27a414de.pyc`
- `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-7c3c7040a8a0.pyc`
- `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-8ac23cabb596.pyc`

Trace excerpt from `data/rq4/tool_traces/cpython-313/cpython-313-089a998b290e/decompyle3.stderr.txt`:
```text
/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-313/lib/python3.13/site-packages/click/core.py:1307: UserWarning: The parameter --version is used more than once. Remove its duplicate as parameters should be unique.
  parser = self.make_parser(ctx)
/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-313/lib/python3.13/site-packages/click/core.py:1300: UserWarning: The parameter --version is used more than once. Remove its duplicate as parameters should be unique.
  self.parse_args(ctx, args)
```

### `decompyle3-07` CPython 3.8: `AssertionError` / empty assertion message

- Combined outcomes: 5
- RQ2 outcomes/signatures: 5/1
- RQ4 outcomes/signatures: 0/0
- Observed statuses: `exit_1`=5
- Stack signature: `not available`

Reproduction commands:

RQ2 representative (`rq2-decompyle3-1c3080b6b90c`):
```bash
data/rq2/envs/cpython-38/bin/decompyle3 data/rq2/failed_cases/assignment-autograder-3.7.6-cpython-38-6c3a28494a6e.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ2 | `rq2-decompyle3-1c3080b6b90c` | 5 | `assignment-autograder-3.7.6.tar.gz::assignment-autograder-3.7.6/autograder/testcase_utils/__pycache__/shell.cpython-38.pyc` | `PycLens/data/rq2/tool_robustness_failures/cpython-38/cpython-38-decompyle3-assignment-autograder-3.7.6.tar.gz-assignment-autograder-3.7.6-autograder-/stdout.txt; PycLens/data/rq2/tool_robustness_failures/cpython-38/cpython-38-decompyle3-assignment-autograder-3.7.6.tar.gz-assignment-autograder-3.7.6-autograder-/stderr.txt` |

Duplicate/example inputs:
- `assignment-autograder-3.7.6.tar.gz::assignment-autograder-3.7.6/autograder/testcase_utils/__pycache__/shell.cpython-38.pyc`
- `autograder-3.7.7.tar.gz::autograder-3.7.7/autograder/testcase_utils/__pycache__/shell.cpython-38.pyc`
- `django_connectwise-1.20.0-py3-none-any.whl::djconnectwise/__pycache__/api.cpython-38.pyc`
- `mwahpy-2.1.5-py3-none-any.whl::mwahpy/__pycache__/plot.cpython-38.pyc`
- `bestFit-0.3.tar.gz::bestFit-0.3/venv/lib/python3.8/site-packages/matplotlib/axes/__pycache__/_base.cpython-38.pyc`

### `decompyle3-08` CPython 3.12: `SIGSEGV` / process crashed with signal 11

- Combined outcomes: 4
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 4/1
- Observed statuses: `exit_-11`=4
- Stack signature: `not available`

Reproduction commands:

RQ4 representative (`rq4-decompyle3-4f2ab4edd998`):
```bash
/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-312/bin/decompyle3 data/rq3/cpython-3.12/unique_bug_pyc/cpython-312-2bcc6ad1f7bb.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ4 | `rq4-decompyle3-4f2ab4edd998` | 4 | `data/rq3/cpython-3.12/unique_bug_pyc/cpython-312-2bcc6ad1f7bb.pyc` | `data/rq4/tool_traces/cpython-312/cpython-312-2bcc6ad1f7bb/decompyle3.stdout.txt; data/rq4/tool_traces/cpython-312/cpython-312-2bcc6ad1f7bb/decompyle3.stderr.txt` |

Duplicate/example inputs:
- `data/rq3/cpython-3.12/unique_bug_pyc/cpython-312-2bcc6ad1f7bb.pyc`
- `data/rq3/cpython-3.12/unique_bug_pyc/cpython-312-58e8048ac5da.pyc`
- `data/rq3/cpython-3.12/unique_bug_pyc/cpython-312-901be4fc6696.pyc`
- `data/rq3/cpython-3.12/unique_bug_pyc/cpython-312-a121b010b70b.pyc`

Trace excerpt from `data/rq4/tool_traces/cpython-312/cpython-312-2bcc6ad1f7bb/decompyle3.stderr.txt`:
```text
/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-312/lib/python3.12/site-packages/click/core.py:1307: UserWarning: The parameter --version is used more than once. Remove its duplicate as parameters should be unique.
  parser = self.make_parser(ctx)
/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-312/lib/python3.12/site-packages/click/core.py:1300: UserWarning: The parameter --version is used more than once. Remove its duplicate as parameters should be unique.
  self.parse_args(ctx, args)
```

### `decompyle3-09` CPython 3.8: `AssertionError` / comp_if_not_or invariant

- Combined outcomes: 4
- RQ2 outcomes/signatures: 4/1
- RQ4 outcomes/signatures: 0/0
- Observed statuses: `exit_1`=4
- Stack signature: `not available`

Reproduction commands:

RQ2 representative (`rq2-decompyle3-c8252badafc6`):
```bash
data/rq2/envs/cpython-38/bin/decompyle3 data/rq2/failed_cases/jembe-0.3.15-cpython-38-8db6662a7e0a.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ2 | `rq2-decompyle3-c8252badafc6` | 4 | `jembe-0.3.15-py3-none-any.whl::jembe/__pycache__/processor.cpython-38.pyc` | `PycLens/data/rq2/tool_robustness_failures/cpython-38/cpython-38-decompyle3-jembe-0.3.15-py3-none-any.whl-jembe-__pycache__-processor.cpython-38.pyc/stdout.txt; PycLens/data/rq2/tool_robustness_failures/cpython-38/cpython-38-decompyle3-jembe-0.3.15-py3-none-any.whl-jembe-__pycache__-processor.cpython-38.pyc/stderr.txt` |

Duplicate/example inputs:
- `jembe-0.3.15-py3-none-any.whl::jembe/__pycache__/processor.cpython-38.pyc`
- `jembe-0.3.15.tar.gz::jembe-0.3.15/jembe/__pycache__/processor.cpython-38.pyc`
- `pobm-1.2.0.tar.gz::pobm-1.2.0/.eggs/PyScaffold-3.2.3-py3.8.egg/pyscaffold/contrib/__pycache__/ptr.cpython-38.pyc`
- `uniqgift_custom-1.0.7-py3-none-any.whl::django/db/models/__pycache__/options.cpython-38.pyc`

### `decompyle3-10` CPython 3.8: `AssertionError` / ifpoplaststmtc expected c_stmts

- Combined outcomes: 4
- RQ2 outcomes/signatures: 4/1
- RQ4 outcomes/signatures: 0/0
- Observed statuses: `exit_1`=4
- Stack signature: `not available`

Reproduction commands:

RQ2 representative (`rq2-decompyle3-6d10da60efcb`):
```bash
data/rq2/envs/cpython-38/bin/decompyle3 data/rq2/failed_cases/aioinstagrapi-1.1.21-cpython-38-4b50f1a66772.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ2 | `rq2-decompyle3-6d10da60efcb` | 4 | `aioinstagrapi-1.1.21-py3-none-any.whl::aioinstagrapi/mixins/__pycache__/hashtag.cpython-38.pyc` | `PycLens/data/rq2/tool_robustness_failures/cpython-38/cpython-38-decompyle3-aioinstagrapi-1.1.21-py3-none-any.whl-aioinstagrapi-mixins-__pycache__-has/stdout.txt; PycLens/data/rq2/tool_robustness_failures/cpython-38/cpython-38-decompyle3-aioinstagrapi-1.1.21-py3-none-any.whl-aioinstagrapi-mixins-__pycache__-has/stderr.txt` |

Duplicate/example inputs:
- `aioinstagrapi-1.1.21-py3-none-any.whl::aioinstagrapi/mixins/__pycache__/hashtag.cpython-38.pyc`
- `aioinstagrapi-1.1.21.tar.gz::aioinstagrapi-1.1.21/aioinstagrapi/mixins/__pycache__/hashtag.cpython-38.pyc`
- `mqc-2.0.2-py3-none-any.whl::mqc/control/__pycache__/atp_control.cpython-38.pyc`
- `mqc-2.0.2.tar.gz::mqc-2.0.2/mqc/control/__pycache__/atp_control.cpython-38.pyc`

### `decompyle3-11` CPython 3.8: `AssertionError` / list_comp invariant

- Combined outcomes: 3
- RQ2 outcomes/signatures: 3/1
- RQ4 outcomes/signatures: 0/0
- Observed statuses: `exit_1`=3
- Stack signature: `not available`

Reproduction commands:

RQ2 representative (`rq2-decompyle3-49b7bb1162cc`):
```bash
data/rq2/envs/cpython-38/bin/decompyle3 data/rq2/failed_cases/bestfit-0.3-cpython-38-1a7f74664829.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ2 | `rq2-decompyle3-49b7bb1162cc` | 3 | `bestFit-0.3.tar.gz::bestFit-0.3/venv/lib/python3.8/site-packages/babel/messages/__pycache__/mofile.cpython-38.pyc` | `PycLens/data/rq2/tool_robustness_failures/cpython-38/cpython-38-decompyle3-bestFit-0.3.tar.gz-bestFit-0.3-venv-lib-python3.8-site-packages-babel-mess/stdout.txt; PycLens/data/rq2/tool_robustness_failures/cpython-38/cpython-38-decompyle3-bestFit-0.3.tar.gz-bestFit-0.3-venv-lib-python3.8-site-packages-babel-mess/stderr.txt` |

Duplicate/example inputs:
- `bestFit-0.3.tar.gz::bestFit-0.3/venv/lib/python3.8/site-packages/babel/messages/__pycache__/mofile.cpython-38.pyc`
- `uniqgift_custom-1.0.7-py3-none-any.whl::django/forms/__pycache__/models.cpython-38.pyc`
- `uniqgift_custom-1.0.7-py3-none-any.whl::django/test/__pycache__/testcases.cpython-38.pyc`

### `decompyle3-12` CPython 3.8: `IndexError` / jump target or bytecode offset out of range

- Combined outcomes: 3
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 3/1
- Observed statuses: `exit_1`=3
- Stack signature: `site-packages/decompyle3/semantics/make_function36.py:make_function36 <- site-packages/decompyle3/scanner.py:__init__ <- site-packages/decompyle3/scanners/scanner38.py:ingest <- site-packages/decompyle3/scanners/scanner37.py:ingest <- site-packages/decompyle3/scanners/scanner37base.py:ingest <- site-packages/decompyle3/scanner.py:get_inst`

Reproduction commands:

RQ4 representative (`rq4-decompyle3-a414ee2fcdbb`):
```bash
/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/bin/decompyle3 data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-172b46bc6f63.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ4 | `rq4-decompyle3-a414ee2fcdbb` | 3 | `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-172b46bc6f63.pyc` | `data/rq4/tool_traces/cpython-38/cpython-38-172b46bc6f63/decompyle3.stdout.txt; data/rq4/tool_traces/cpython-38/cpython-38-172b46bc6f63/decompyle3.stderr.txt` |

Duplicate/example inputs:
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-172b46bc6f63.pyc`
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-6273a738710f.pyc`
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-717ef7a927e1.pyc`

Trace excerpt from `data/rq4/tool_traces/cpython-38/cpython-38-172b46bc6f63/decompyle3.stderr.txt`:
```text
Traceback (most recent call last):
  File "data/rq2/envs/cpython-38/bin/decompyle3", line 8, in <module>
    sys.exit(main_bin())
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1161, in __call__
    return self.main(*args, **kwargs)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1082, in main
    rv = self.invoke(ctx)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1443, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 788, in invoke
    return __callback(*args, **kwargs)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/decompyle3/bin/decompile.py", line 175, in main_bin
```

### `decompyle3-13` CPython 3.8: `AssertionError` / c_try_except handler invariant

- Combined outcomes: 2
- RQ2 outcomes/signatures: 2/1
- RQ4 outcomes/signatures: 0/0
- Observed statuses: `exit_1`=2
- Stack signature: `not available`

Reproduction commands:

RQ2 representative (`rq2-decompyle3-1328af067a6e`):
```bash
data/rq2/envs/cpython-38/bin/decompyle3 data/rq2/failed_cases/multiqc-vlad-1.30.dev20250821143134-cpython-38-9fb18e630a65.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ2 | `rq2-decompyle3-1328af067a6e` | 2 | `multiqc_vlad-1.30.dev20250821143134.tar.gz::multiqc_vlad-1.30.dev20250821143134/multiqc/plots/__pycache__/table_object.cpython-38.pyc` | `PycLens/data/rq2/tool_robustness_failures/cpython-38/cpython-38-decompyle3-multiqc_vlad-1.30.dev20250821143134.tar.gz-multiqc_vlad-1.30.dev2025082114/stdout.txt; PycLens/data/rq2/tool_robustness_failures/cpython-38/cpython-38-decompyle3-multiqc_vlad-1.30.dev20250821143134.tar.gz-multiqc_vlad-1.30.dev2025082114/stderr.txt` |

Duplicate/example inputs:
- `multiqc_vlad-1.30.dev20250821143134.tar.gz::multiqc_vlad-1.30.dev20250821143134/multiqc/plots/__pycache__/table_object.cpython-38.pyc`
- `multiqc_vlad-1.30.dev20250821143134-py3-none-any.whl::multiqc/plots/__pycache__/table_object.cpython-38.pyc`

### `decompyle3-14` CPython 3.8: `AssertionError` / comp_if_or invariant

- Combined outcomes: 2
- RQ2 outcomes/signatures: 2/1
- RQ4 outcomes/signatures: 0/0
- Observed statuses: `exit_1`=2
- Stack signature: `not available`

Reproduction commands:

RQ2 representative (`rq2-decompyle3-c3f3843b06df`):
```bash
data/rq2/envs/cpython-38/bin/decompyle3 data/rq2/failed_cases/bestfit-0.3-cpython-38-1a7f74664829.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ2 | `rq2-decompyle3-c3f3843b06df` | 2 | `bestFit-0.3.tar.gz::bestFit-0.3/venv/lib/python3.8/site-packages/poetry/core/_vendor/lark/__pycache__/reconstruct.cpython-38.pyc` | `PycLens/data/rq2/tool_robustness_failures/cpython-38/cpython-38-decompyle3-bestFit-0.3.tar.gz-bestFit-0.3-venv-lib-python3.8-site-packages-poetry-cor/stdout.txt; PycLens/data/rq2/tool_robustness_failures/cpython-38/cpython-38-decompyle3-bestFit-0.3.tar.gz-bestFit-0.3-venv-lib-python3.8-site-packages-poetry-cor/stderr.txt` |

Duplicate/example inputs:
- `bestFit-0.3.tar.gz::bestFit-0.3/venv/lib/python3.8/site-packages/poetry/core/_vendor/lark/__pycache__/reconstruct.cpython-38.pyc`
- `bestFit-0.3.tar.gz::bestFit-0.3/venv/lib/python3.8/site-packages/poetry/core/_vendor/lark/__pycache__/reconstruct2.cpython-38.pyc`

### `decompyle3-15` CPython 3.8: `AssertionError` / comp_if_or_not invariant

- Combined outcomes: 2
- RQ2 outcomes/signatures: 2/1
- RQ4 outcomes/signatures: 0/0
- Observed statuses: `exit_1`=2
- Stack signature: `not available`

Reproduction commands:

RQ2 representative (`rq2-decompyle3-3bfbe0cf6989`):
```bash
data/rq2/envs/cpython-38/bin/decompyle3 data/rq2/failed_cases/aimmocore-0.1.15-cpython-38-925f60668dba.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ2 | `rq2-decompyle3-3bfbe0cf6989` | 2 | `aimmocore-0.1.15-py3-none-any.whl::aimmocore/core/__pycache__/storages.cpython-38.pyc` | `PycLens/data/rq2/tool_robustness_failures/cpython-38/cpython-38-decompyle3-aimmocore-0.1.15-py3-none-any.whl-aimmocore-core-__pycache__-storages.cpyt/stdout.txt; PycLens/data/rq2/tool_robustness_failures/cpython-38/cpython-38-decompyle3-aimmocore-0.1.15-py3-none-any.whl-aimmocore-core-__pycache__-storages.cpyt/stderr.txt` |

Duplicate/example inputs:
- `aimmocore-0.1.15-py3-none-any.whl::aimmocore/core/__pycache__/storages.cpython-38.pyc`
- `aimmocore-0.1.15.tar.gz::aimmocore-0.1.15/aimmocore/core/__pycache__/storages.cpython-38.pyc`

### `decompyle3-16` CPython 3.8: `AssertionError` / empty message

- Combined outcomes: 2
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 2/1
- Observed statuses: `exit_1`=2
- Stack signature: `site-packages/decompyle3/main.py:decompile_file <- site-packages/decompyle3/main.py:decompile <- site-packages/decompyle3/semantics/pysource.py:code_deparse <- site-packages/decompyle3/scanners/scanner38.py:ingest <- site-packages/decompyle3/scanners/scanner37.py:ingest <- site-packages/decompyle3/scanners/scanner37base.py:bound_collection_from_tokens`

Reproduction commands:

RQ4 representative (`rq4-decompyle3-b21e73d9982b`):
```bash
/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/bin/decompyle3 data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-6fc7c4e73992.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ4 | `rq4-decompyle3-b21e73d9982b` | 2 | `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-6fc7c4e73992.pyc` | `data/rq4/tool_traces/cpython-38/cpython-38-6fc7c4e73992/decompyle3.stdout.txt; data/rq4/tool_traces/cpython-38/cpython-38-6fc7c4e73992/decompyle3.stderr.txt` |

Duplicate/example inputs:
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-6fc7c4e73992.pyc`
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-d9e88510d3f6.pyc`

Trace excerpt from `data/rq4/tool_traces/cpython-38/cpython-38-6fc7c4e73992/decompyle3.stderr.txt`:
```text
Traceback (most recent call last):
  File "data/rq2/envs/cpython-38/bin/decompyle3", line 8, in <module>
    sys.exit(main_bin())
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1161, in __call__
    return self.main(*args, **kwargs)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1082, in main
    rv = self.invoke(ctx)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1443, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 788, in invoke
    return __callback(*args, **kwargs)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/decompyle3/bin/decompile.py", line 175, in main_bin
```

### `decompyle3-17` CPython 3.8: `AssertionError` / empty message

- Combined outcomes: 2
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 2/1
- Observed statuses: `exit_1`=2
- Stack signature: `site-packages/decompyle3/semantics/make_function36.py:make_function36 <- site-packages/decompyle3/scanner.py:__init__ <- site-packages/decompyle3/scanners/scanner38.py:ingest <- site-packages/decompyle3/scanners/scanner37.py:ingest <- site-packages/decompyle3/scanners/scanner37base.py:ingest <- site-packages/decompyle3/scanner.py:get_inst`

Reproduction commands:

RQ4 representative (`rq4-decompyle3-d8259630f68d`):
```bash
/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/bin/decompyle3 data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-0e6ea9f74fdd.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ4 | `rq4-decompyle3-d8259630f68d` | 2 | `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-0e6ea9f74fdd.pyc` | `data/rq4/tool_traces/cpython-38/cpython-38-0e6ea9f74fdd/decompyle3.stdout.txt; data/rq4/tool_traces/cpython-38/cpython-38-0e6ea9f74fdd/decompyle3.stderr.txt` |

Duplicate/example inputs:
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-0e6ea9f74fdd.pyc`
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-46a59a1a86c9.pyc`

Trace excerpt from `data/rq4/tool_traces/cpython-38/cpython-38-0e6ea9f74fdd/decompyle3.stderr.txt`:
```text
Traceback (most recent call last):
  File "data/rq2/envs/cpython-38/bin/decompyle3", line 8, in <module>
    sys.exit(main_bin())
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1161, in __call__
    return self.main(*args, **kwargs)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1082, in main
    rv = self.invoke(ctx)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1443, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 788, in invoke
    return __callback(*args, **kwargs)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/decompyle3/bin/decompile.py", line 175, in main_bin
```

### `decompyle3-18` CPython 3.8: `IndexError` / constant index out of range

- Combined outcomes: 2
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 2/1
- Observed statuses: `exit_1`=2
- Stack signature: `site-packages/decompyle3/scanners/scanner38.py:ingest <- site-packages/decompyle3/scanners/scanner37.py:ingest <- site-packages/decompyle3/scanners/scanner37base.py:ingest <- site-packages/decompyle3/scanner.py:build_instructions <- site-packages/xdis/bytecode.py:get_instructions_bytes <- site-packages/xdis/bytecode.py:get_logical_instruction_at_offset`

Reproduction commands:

RQ4 representative (`rq4-decompyle3-e35c258e69bb`):
```bash
/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/bin/decompyle3 data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-3cebf488677b.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ4 | `rq4-decompyle3-e35c258e69bb` | 2 | `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-3cebf488677b.pyc` | `data/rq4/tool_traces/cpython-38/cpython-38-3cebf488677b/decompyle3.stdout.txt; data/rq4/tool_traces/cpython-38/cpython-38-3cebf488677b/decompyle3.stderr.txt` |

Duplicate/example inputs:
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-3cebf488677b.pyc`
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-9a9fb65de558.pyc`

Trace excerpt from `data/rq4/tool_traces/cpython-38/cpython-38-3cebf488677b/decompyle3.stderr.txt`:
```text
Traceback (most recent call last):
  File "data/rq2/envs/cpython-38/bin/decompyle3", line 8, in <module>
    sys.exit(main_bin())
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1161, in __call__
    return self.main(*args, **kwargs)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1082, in main
    rv = self.invoke(ctx)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1443, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 788, in invoke
    return __callback(*args, **kwargs)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/decompyle3/bin/decompile.py", line 175, in main_bin
```

### `decompyle3-19` CPython 3.8: `TypeError` / argument of type 'int' is not iterable

- Combined outcomes: 2
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 2/1
- Observed statuses: `exit_1`=2
- Stack signature: `site-packages/decompyle3/semantics/n_actions.py:n_mkfunc <- site-packages/decompyle3/semantics/make_function36.py:make_function36 <- site-packages/decompyle3/scanner.py:__init__ <- site-packages/decompyle3/scanners/scanner38.py:ingest <- site-packages/decompyle3/scanners/scanner37.py:ingest <- site-packages/decompyle3/scanners/scanner37base.py:ingest`

Reproduction commands:

RQ4 representative (`rq4-decompyle3-5c1bac28ece4`):
```bash
/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/bin/decompyle3 data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-5e5346c1cf8a.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ4 | `rq4-decompyle3-5c1bac28ece4` | 2 | `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-5e5346c1cf8a.pyc` | `data/rq4/tool_traces/cpython-38/cpython-38-5e5346c1cf8a/decompyle3.stdout.txt; data/rq4/tool_traces/cpython-38/cpython-38-5e5346c1cf8a/decompyle3.stderr.txt` |

Duplicate/example inputs:
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-5e5346c1cf8a.pyc`
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-b0c2992e0f7d.pyc`

Trace excerpt from `data/rq4/tool_traces/cpython-38/cpython-38-5e5346c1cf8a/decompyle3.stderr.txt`:
```text
Traceback (most recent call last):
  File "data/rq2/envs/cpython-38/bin/decompyle3", line 8, in <module>
    sys.exit(main_bin())
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1161, in __call__
    return self.main(*args, **kwargs)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1082, in main
    rv = self.invoke(ctx)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1443, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 788, in invoke
    return __callback(*args, **kwargs)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/decompyle3/bin/decompile.py", line 175, in main_bin
```

### `decompyle3-20` CPython 3.9: `SystemError` / uncaught code-object construction exception

- Combined outcomes: 2
- RQ2 outcomes/signatures: 2/1
- RQ4 outcomes/signatures: 0/0
- Observed statuses: `exit_2`=2
- Stack signature: `not available`

Reproduction commands:

RQ2 representative (`rq2-decompyle3-d72f6c756b02`):
```bash
data/rq2/envs/cpython-39/bin/decompyle3 data/rq2/failed_cases/clustcrdist-0.1.5-cpython-39-06d1d321521d.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ2 | `rq2-decompyle3-d72f6c756b02` | 2 | `clustcrdist-0.1.5-py2.py3-none-any.whl::clustcrdist/constants/modules/tcrdist/__pycache__/tcrdist_svg_basic.cpython-39.pyc` | `PycLens/data/rq2/tool_robustness_failures/cpython-39/cpython-39-decompyle3-clustcrdist-0.1.5-py2.py3-none-any.whl-clustcrdist-constants-modules-tcrdi/stdout.txt; PycLens/data/rq2/tool_robustness_failures/cpython-39/cpython-39-decompyle3-clustcrdist-0.1.5-py2.py3-none-any.whl-clustcrdist-constants-modules-tcrdi/stderr.txt` |

Duplicate/example inputs:
- `clustcrdist-0.1.5-py2.py3-none-any.whl::clustcrdist/constants/modules/tcrdist/__pycache__/tcrdist_svg_basic.cpython-39.pyc`
- `clustcrdist-0.1.5.tar.gz::clustcrdist-0.1.5/clustcrdist/constants/modules/tcrdist/__pycache__/tcrdist_svg_basic.cpython-39.pyc`

### `decompyle3-21` CPython 3.12: `SIGABRT` / allocator/heap abort

- Combined outcomes: 1
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 1/1
- Observed statuses: `exit_-6`=1
- Stack signature: `not available`

Reproduction commands:

RQ4 representative (`rq4-decompyle3-0ed71adf3dff`):
```bash
data/rq2/envs/cpython-312/bin/decompyle3 data/rq3/cpython-3.12/unique_bug_pyc/cpython-312-eb581a73e180.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ4 | `rq4-decompyle3-0ed71adf3dff` | 1 | `data/rq3/cpython-3.12/unique_bug_pyc/cpython-312-eb581a73e180.pyc` | `data/rq4/tool_traces/cpython-312/cpython-312-eb581a73e180/decompyle3.stdout.txt; data/rq4/tool_traces/cpython-312/cpython-312-eb581a73e180/decompyle3.stderr.txt` |

Duplicate/example inputs:
- `data/rq3/cpython-3.12/unique_bug_pyc/cpython-312-eb581a73e180.pyc`

Trace excerpt from `data/rq4/tool_traces/cpython-312/cpython-312-eb581a73e180/decompyle3.stderr.txt`:
```text
/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-312/lib/python3.12/site-packages/click/core.py:1307: UserWarning: The parameter --version is used more than once. Remove its duplicate as parameters should be unique.
  parser = self.make_parser(ctx)
/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-312/lib/python3.12/site-packages/click/core.py:1300: UserWarning: The parameter --version is used more than once. Remove its duplicate as parameters should be unique.
  self.parse_args(ctx, args)
malloc(): invalid size (unsorted)
```

### `decompyle3-22` CPython 3.8: `SIGABRT` / fatal Python runtime error

- Combined outcomes: 1
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 1/1
- Observed statuses: `exit_-6`=1
- Stack signature: `not available`

Reproduction commands:

RQ4 representative (`rq4-decompyle3-8f2190c11f24`):
```bash
/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/bin/decompyle3 data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-770a9e21632b.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ4 | `rq4-decompyle3-8f2190c11f24` | 1 | `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-770a9e21632b.pyc` | `data/rq4/tool_traces/cpython-38/cpython-38-770a9e21632b/decompyle3.stdout.txt; data/rq4/tool_traces/cpython-38/cpython-38-770a9e21632b/decompyle3.stderr.txt` |

Duplicate/example inputs:
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-770a9e21632b.pyc`

Trace excerpt from `data/rq4/tool_traces/cpython-38/cpython-38-770a9e21632b/decompyle3.stderr.txt`:
```text
Fatal Python error: non-string found in code slot
Python runtime state: initialized
Current thread 0x00007ffb36138000 (most recent call first):
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/xdis/load.py", line 328 in load_module_from_file_object
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/xdis/load.py", line 194 in load_module
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/decompyle3/main.py", line 212 in decompile_file
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/decompyle3/main.py", line 336 in main
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/decompyle3/bin/decompile.py", line 175 in main_bin
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 788 in invoke
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1443 in invoke
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1082 in main
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/click/core.py", line 1161 in __call__
```

### `decompyle3-23` CPython 3.8: `TypeError` / malformed marshal loader state

- Combined outcomes: 1
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 1/1
- Observed statuses: `exit_2`=1
- Stack signature: `site-packages/xdis/load.py:load_module_from_file_object <- site-packages/xdis/unmarshal.py:load_code <- site-packages/xdis/unmarshal.py:load <- site-packages/xdis/unmarshal.py:r_object <- site-packages/xdis/unmarshal.py:t_code`

Reproduction commands:

RQ4 representative (`rq4-decompyle3-f2c2accc5c76`):
```bash
/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/bin/decompyle3 data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-09cf932ac7c9.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ4 | `rq4-decompyle3-f2c2accc5c76` | 1 | `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-09cf932ac7c9.pyc` | `data/rq4/tool_traces/cpython-38/cpython-38-09cf932ac7c9/decompyle3.stdout.txt; data/rq4/tool_traces/cpython-38/cpython-38-09cf932ac7c9/decompyle3.stderr.txt` |

Duplicate/example inputs:
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-09cf932ac7c9.pyc`

Trace excerpt from `data/rq4/tool_traces/cpython-38/cpython-38-09cf932ac7c9/decompyle3.stderr.txt`:
```text
Unknown type 64 (hex 40) @
Unknown type 0 (hex 0) \x00
Unknown type 0 (hex 0) \x00
Unknown type 0 (hex 0) \x00
Traceback (most recent call last):
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/xdis/load.py", line 337, in load_module_from_file_object
    co = xdis.unmarshal.load_code(fp, magic_int, code_objects)
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/xdis/unmarshal.py", line 652, in load_code
    return um_gen.load()
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/xdis/unmarshal.py", line 189, in load
    return self.r_object()
  File "/home/awen/git/PybcSEC/PycLens/data/rq2/envs/cpython-38/lib/python3.8/site-packages/xdis/unmarshal.py", line 233, in r_object
```

## Tool: `dis`

- Combined outcomes: 45
- Combined unique signatures: 3
- RQ2 outcomes/signatures: 45/3
- RQ4 outcomes/signatures: 0/0

| ID | Version | Failure | Cause | RQ2 | RQ4 | Total |
|---|---|---|---|---:|---:|---:|
| `dis-01` | CPython 3.10 | `IndexError` | tuple index out of range | 42 | 0 | 42 |
| `dis-02` | CPython 3.14 | `ValueError` | bad marshal data (unknown type code) | 2 | 0 | 2 |
| `dis-03` | CPython 3.12 | `ValueError` | bad marshal data (unknown type code) | 1 | 0 | 1 |

### `dis-01` CPython 3.10: `IndexError` / tuple index out of range

- Combined outcomes: 42
- RQ2 outcomes/signatures: 42/1
- RQ4 outcomes/signatures: 0/0
- Observed statuses: `error`=42
- Stack signature: `<stdin>:replay_stdlib <- pythonlib/dis.py:_get_instructions_bytes <- pythonlib/dis.py:_get_const_info`

Reproduction commands:

RQ2 representative (`rq2-dis-84ace3ac8c52`):
```bash
data/rq2/envs/cpython-310/bin/python -c 'import marshal,dis,sys; data=open(sys.argv[1],'"'"'rb'"'"').read(); co=marshal.loads(data[16:]); dis.Bytecode(co).dis()' data/rq2/failed_cases/rtx-deep-1.3.9-cpython-310-04ae890b0018.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ2 | `rq2-dis-84ace3ac8c52` | 42 | `rtx_deep-1.3.9-py310-none-any.whl::rtx_deep/__init__.pyc` | `PycLens/data/rq2/tool_robustness_failures/cpython-310/cpython-310-dis-rtx_deep-1.3.9-py310-none-any.whl-rtx_deep-__init__.pyc/stdout.txt; PycLens/data/rq2/tool_robustness_failures/cpython-310/cpython-310-dis-rtx_deep-1.3.9-py310-none-any.whl-rtx_deep-__init__.pyc/stderr.txt` |

Duplicate/example inputs:
- `rtx_deep-1.3.9-py310-none-any.whl::rtx_deep/__init__.pyc`
- `rtx_deep-1.3.9-py310-none-any.whl::rtx_deep/deploy_lib/__init__.pyc`
- `rtx_deep-1.3.9-py310-none-any.whl::rtx_deep/deploy_lib/convert_trt.pyc`
- `rtx_deep-1.3.9-py310-none-any.whl::rtx_deep/deploy_lib/converter_registry.pyc`
- `rtx_deep-1.3.9-py310-none-any.whl::rtx_deep/deploy_lib/converter_utils.pyc`

### `dis-02` CPython 3.14: `ValueError` / bad marshal data (unknown type code)

- Combined outcomes: 2
- RQ2 outcomes/signatures: 2/1
- RQ4 outcomes/signatures: 0/0
- Observed statuses: `error`=2
- Stack signature: `<stdin>:load_code_candidates`

Reproduction commands:

RQ2 representative (`rq2-dis-5719621e930d`):
```bash
data/rq2/envs/cpython-314/bin/python -c 'import marshal,dis,sys; data=open(sys.argv[1],'"'"'rb'"'"').read(); co=marshal.loads(data[16:]); dis.Bytecode(co).dis()' data/rq2/failed_cases/libmercury-0.85-cpython-314-3ca8e7528adb.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ2 | `rq2-dis-5719621e930d` | 2 | `libmercury-0.85-py3-none-any.whl::libmercury/__pycache__/__init__.cpython-314.pyc` | `PycLens/data/rq2/tool_robustness_failures/cpython-314/cpython-314-dis-libmercury-0.85-py3-none-any.whl-libmercury-__pycache__-__init__.cpython-314.pyc/stdout.txt; PycLens/data/rq2/tool_robustness_failures/cpython-314/cpython-314-dis-libmercury-0.85-py3-none-any.whl-libmercury-__pycache__-__init__.cpython-314.pyc/stderr.txt` |

Duplicate/example inputs:
- `libmercury-0.85-py3-none-any.whl::libmercury/__pycache__/__init__.cpython-314.pyc`
- `libmercury-0.85.tar.gz::libmercury-0.85/src/libmercury/__pycache__/__init__.cpython-314.pyc`

### `dis-03` CPython 3.12: `ValueError` / bad marshal data (unknown type code)

- Combined outcomes: 1
- RQ2 outcomes/signatures: 1/1
- RQ4 outcomes/signatures: 0/0
- Observed statuses: `error`=1
- Stack signature: `<stdin>:load_code_candidates`

Reproduction commands:

RQ2 representative (`rq2-dis-65caab073471`):
```bash
data/rq2/envs/cpython-312/bin/python -c 'import marshal,dis,sys; data=open(sys.argv[1],'"'"'rb'"'"').read(); co=marshal.loads(data[16:]); dis.Bytecode(co).dis()' data/rq2/failed_cases/tkfly-0.1.0b3-cpython-312-e4fc05c09ee6.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ2 | `rq2-dis-65caab073471` | 1 | `tkfly-0.1.0b3.tar.gz::tkfly-0.1.0b3/tkfly/_tklib/__pycache__/__init__.cpython-312.pyc` | `PycLens/data/rq2/tool_robustness_failures/cpython-312/cpython-312-dis-tkfly-0.1.0b3.tar.gz-tkfly-0.1.0b3-tkfly-_tklib-__pycache__-__init__.cpython-312/stdout.txt; PycLens/data/rq2/tool_robustness_failures/cpython-312/cpython-312-dis-tkfly-0.1.0b3.tar.gz-tkfly-0.1.0b3-tkfly-_tklib-__pycache__-__init__.cpython-312/stderr.txt` |

Duplicate/example inputs:
- `tkfly-0.1.0b3.tar.gz::tkfly-0.1.0b3/tkfly/_tklib/__pycache__/__init__.cpython-312.pyc`

## Tool: `marshal`

- Combined outcomes: 2
- Combined unique signatures: 1
- RQ2 outcomes/signatures: 2/1
- RQ4 outcomes/signatures: 0/0

| ID | Version | Failure | Cause | RQ2 | RQ4 | Total |
|---|---|---|---|---:|---:|---:|
| `marshal-01` | CPython 3.9 | `EOFError` | marshal data too short | 2 | 0 | 2 |

### `marshal-01` CPython 3.9: `EOFError` / marshal data too short

- Combined outcomes: 2
- RQ2 outcomes/signatures: 2/1
- RQ4 outcomes/signatures: 0/0
- Observed statuses: `error`=2
- Stack signature: `<stdin>:load_code_candidates`

Reproduction commands:

RQ2 representative (`rq2-marshal-8f98856658d1`):
```bash
data/rq2/envs/cpython-39/bin/python -c 'import marshal,sys; data=open(sys.argv[1],'"'"'rb'"'"').read(); marshal.loads(data[16:])' data/rq2/failed_cases/clustcrdist-0.1.5-cpython-39-06d1d321521d.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ2 | `rq2-marshal-8f98856658d1` | 2 | `clustcrdist-0.1.5-py2.py3-none-any.whl::clustcrdist/constants/modules/tcrdist/__pycache__/tcrdist_svg_basic.cpython-39.pyc` | `PycLens/data/rq2/tool_robustness_failures/cpython-39/cpython-39-marshal-clustcrdist-0.1.5-py2.py3-none-any.whl-clustcrdist-constants-modules-tcrdist-/stdout.txt; PycLens/data/rq2/tool_robustness_failures/cpython-39/cpython-39-marshal-clustcrdist-0.1.5-py2.py3-none-any.whl-clustcrdist-constants-modules-tcrdist-/stderr.txt` |

Duplicate/example inputs:
- `clustcrdist-0.1.5-py2.py3-none-any.whl::clustcrdist/constants/modules/tcrdist/__pycache__/tcrdist_svg_basic.cpython-39.pyc`
- `clustcrdist-0.1.5.tar.gz::clustcrdist-0.1.5/clustcrdist/constants/modules/tcrdist/__pycache__/tcrdist_svg_basic.cpython-39.pyc`

## Tool: `pylingual`

- Combined outcomes: 22
- Combined unique signatures: 8
- RQ2 outcomes/signatures: 3/2
- RQ4 outcomes/signatures: 19/8

| ID | Version | Failure | Cause | RQ2 | RQ4 | Total |
|---|---|---|---|---:|---:|---:|
| `pylingual-01` | CPython 3.8 | `Timeout` | did not terminate within 600s | 2 | 3 | 5 |
| `pylingual-02` | CPython 3.12 | `SIGSEGV` | process crashed with signal 11 | 0 | 4 | 4 |
| `pylingual-03` | CPython 3.10 | `SIGILL` | process crashed with signal 4 | 0 | 3 | 3 |
| `pylingual-04` | CPython 3.12 | `SIGABRT` | allocator/heap abort | 0 | 3 | 3 |
| `pylingual-05` | CPython 3.9 | `Timeout` | did not terminate within 600s | 1 | 2 | 3 |
| `pylingual-06` | CPython 3.9 | `SIGILL` | process crashed with signal 4 | 0 | 2 | 2 |
| `pylingual-07` | CPython 3.10 | `Timeout` | did not terminate within 600s | 0 | 1 | 1 |
| `pylingual-08` | CPython 3.8 | `SIGILL` | process crashed with signal 4 | 0 | 1 | 1 |

### `pylingual-01` CPython 3.8: `Timeout` / did not terminate within 600s

- Combined outcomes: 5
- RQ2 outcomes/signatures: 2/1
- RQ4 outcomes/signatures: 3/1
- Observed statuses: `timeout`=5
- Stack signature: `not available`

Reproduction commands:

RQ2 representative (`rq2-pylingual-80ef8f93c939`):
```bash
data/rq2/envs/cpython-38/bin/pylingual data/rq2/failed_cases/sceleto2-1.1.2-cpython-38-b3e039fd9d1c.pyc
```
RQ4 representative (`rq4-pylingual-80ef8f93c939`):
```bash
data/rq2/envs/cpython-38/bin/pylingual data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-80372b990fd5.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ2 | `rq2-pylingual-80ef8f93c939` | 2 | `sceleto2-1.1.2-py3-none-any.whl::sceleto2/__pycache__/data.cpython-38.pyc` | `PycLens/data/rq2/tool_robustness_failures/cpython-38/cpython-38-pylingual-sceleto2-1.1.2-py3-none-any.whl-sceleto2-__pycache__-data.cpython-38.pyc/stdout.txt; PycLens/data/rq2/tool_robustness_failures/cpython-38/cpython-38-pylingual-sceleto2-1.1.2-py3-none-any.whl-sceleto2-__pycache__-data.cpython-38.pyc/stderr.txt` |
| RQ4 | `rq4-pylingual-80ef8f93c939` | 3 | `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-80372b990fd5.pyc` | `data/rq4/tool_traces/cpython-38/cpython-38-80372b990fd5/pylingual.stdout.txt; data/rq4/tool_traces/cpython-38/cpython-38-80372b990fd5/pylingual.stderr.txt` |

Duplicate/example inputs:
- `sceleto2-1.1.2-py3-none-any.whl::sceleto2/__pycache__/data.cpython-38.pyc`
- `sceleto2-1.1.2.tar.gz::sceleto2-1.1.2/sceleto2/__pycache__/data.cpython-38.pyc`
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-80372b990fd5.pyc`
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-8757a6d804b7.pyc`
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-ba15f27986b7.pyc`

Trace excerpt from `data/rq4/tool_traces/cpython-38/cpython-38-80372b990fd5/pylingual.stderr.txt`:
```text
timeout_after_600s
```

### `pylingual-02` CPython 3.12: `SIGSEGV` / process crashed with signal 11

- Combined outcomes: 4
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 4/1
- Observed statuses: `exit_-11`=4
- Stack signature: `not available`

Reproduction commands:

RQ4 representative (`rq4-pylingual-78e556653975`):
```bash
/usr/local/bin/pylingual -o /home/awen/git/PybcSEC/PycLens/data/rq4/replayed_tool_robustness/002-pylingual-cpython-312-cpython-312-2bcc6ad1f7bb/pylingual_out data/rq3/cpython-3.12/unique_bug_pyc/cpython-312-2bcc6ad1f7bb.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ4 | `rq4-pylingual-78e556653975` | 4 | `data/rq3/cpython-3.12/unique_bug_pyc/cpython-312-2bcc6ad1f7bb.pyc` | `data/rq4/tool_traces/cpython-312/cpython-312-2bcc6ad1f7bb/pylingual.stdout.txt; data/rq4/tool_traces/cpython-312/cpython-312-2bcc6ad1f7bb/pylingual.stderr.txt` |

Duplicate/example inputs:
- `data/rq3/cpython-3.12/unique_bug_pyc/cpython-312-2bcc6ad1f7bb.pyc`
- `data/rq3/cpython-3.12/unique_bug_pyc/cpython-312-58e8048ac5da.pyc`
- `data/rq3/cpython-3.12/unique_bug_pyc/cpython-312-901be4fc6696.pyc`
- `data/rq3/cpython-3.12/unique_bug_pyc/cpython-312-a121b010b70b.pyc`

Trace excerpt from `data/rq4/tool_traces/cpython-312/cpython-312-2bcc6ad1f7bb/pylingual.stdout.txt`:
```text
────────────────────────────────────────────────────────────────────────────────
 ,ggggggggggg,              ,gggg,
dP"""88""""""Y8,           d8" "8I
,dPYb,
Yb,  88      `8b           88  ,dP
IP'`Yb
 `"  88      ,8P        8888888P"     gg
I8  8I
     88aaaad8P"            88         ""
I8  8'
     88"""""gg     gg      88         gg    ,ggg,,ggg,     ,gggg,gg  gg      gg
,gggg,gg  I8 dP
```

### `pylingual-03` CPython 3.10: `SIGILL` / process crashed with signal 4

- Combined outcomes: 3
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 3/1
- Observed statuses: `exit_-4`=3
- Stack signature: `not available`

Reproduction commands:

RQ4 representative (`rq4-pylingual-e2f199efc530`):
```bash
data/rq2/envs/cpython-310/bin/pylingual data/rq3/cpython-3.10/unique_bug_pyc/cpython-310-987b9fe188ce.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ4 | `rq4-pylingual-e2f199efc530` | 3 | `data/rq3/cpython-3.10/unique_bug_pyc/cpython-310-987b9fe188ce.pyc` | `data/rq4/tool_traces/cpython-310/cpython-310-987b9fe188ce/pylingual.stdout.txt; data/rq4/tool_traces/cpython-310/cpython-310-987b9fe188ce/pylingual.stderr.txt` |

Duplicate/example inputs:
- `data/rq3/cpython-3.10/unique_bug_pyc/cpython-310-987b9fe188ce.pyc`
- `data/rq3/cpython-3.10/unique_bug_pyc/cpython-310-bfa4ec2fcc83.pyc`
- `data/rq3/cpython-3.10/unique_bug_pyc/cpython-310-ed6225ecbcc3.pyc`

Trace excerpt from `data/rq4/tool_traces/cpython-310/cpython-310-987b9fe188ce/pylingual.stdout.txt`:
```text
────────────────────────────────────────────────────────────────────────────────
 ,ggggggggggg,              ,gggg,
dP"""88""""""Y8,           d8" "8I
,dPYb,
Yb,  88      `8b           88  ,dP
IP'`Yb
 `"  88      ,8P        8888888P"     gg
I8  8I
     88aaaad8P"            88         ""
I8  8'
     88"""""gg     gg      88         gg    ,ggg,,ggg,     ,gggg,gg  gg      gg
,gggg,gg  I8 dP
```

### `pylingual-04` CPython 3.12: `SIGABRT` / allocator/heap abort

- Combined outcomes: 3
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 3/1
- Observed statuses: `exit_-6`=3
- Stack signature: `not available`

Reproduction commands:

RQ4 representative (`rq4-pylingual-4cfed44c0425`):
```bash
data/rq2/envs/cpython-312/bin/pylingual data/rq3/cpython-3.12/unique_bug_pyc/cpython-312-413e7385bec6.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ4 | `rq4-pylingual-4cfed44c0425` | 3 | `data/rq3/cpython-3.12/unique_bug_pyc/cpython-312-413e7385bec6.pyc` | `data/rq4/tool_traces/cpython-312/cpython-312-413e7385bec6/pylingual.stdout.txt; data/rq4/tool_traces/cpython-312/cpython-312-413e7385bec6/pylingual.stderr.txt` |

Duplicate/example inputs:
- `data/rq3/cpython-3.12/unique_bug_pyc/cpython-312-413e7385bec6.pyc`
- `data/rq3/cpython-3.12/unique_bug_pyc/cpython-312-6e3193687da1.pyc`
- `data/rq3/cpython-3.12/unique_bug_pyc/cpython-312-eb581a73e180.pyc`

Trace excerpt from `data/rq4/tool_traces/cpython-312/cpython-312-413e7385bec6/pylingual.stderr.txt`:
```text
free(): invalid pointer
```

### `pylingual-05` CPython 3.9: `Timeout` / did not terminate within 600s

- Combined outcomes: 3
- RQ2 outcomes/signatures: 1/1
- RQ4 outcomes/signatures: 2/1
- Observed statuses: `timeout`=3
- Stack signature: `not available`

Reproduction commands:

RQ2 representative (`rq2-pylingual-c69a3fae2ac0`):
```bash
data/rq2/envs/cpython-39/bin/pylingual data/rq2/failed_cases/dovado-rtl-0.10.12-cpython-39-9f8abbc82d0c.pyc
```
RQ4 representative (`rq4-pylingual-c69a3fae2ac0`):
```bash
data/rq2/envs/cpython-39/bin/pylingual data/rq3/cpython-3.9/unique_bug_pyc/cpython-39-02bda83cf25f.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ2 | `rq2-pylingual-c69a3fae2ac0` | 1 | `dovado_rtl-0.10.12.tar.gz::dovado_rtl-0.10.12/dovado_rtl/parsers/system_verilog/generated/__pycache__/SystemVerilogParser.cpython-39.pyc` | `PycLens/data/rq2/tool_robustness_failures/cpython-39/cpython-39-pylingual-dovado_rtl-0.10.12.tar.gz-dovado_rtl-0.10.12-dovado_rtl-parsers-system_veri/stdout.txt; PycLens/data/rq2/tool_robustness_failures/cpython-39/cpython-39-pylingual-dovado_rtl-0.10.12.tar.gz-dovado_rtl-0.10.12-dovado_rtl-parsers-system_veri/stderr.txt` |
| RQ4 | `rq4-pylingual-c69a3fae2ac0` | 2 | `data/rq3/cpython-3.9/unique_bug_pyc/cpython-39-02bda83cf25f.pyc` | `data/rq4/tool_traces/cpython-39/cpython-39-02bda83cf25f/pylingual.stdout.txt; data/rq4/tool_traces/cpython-39/cpython-39-02bda83cf25f/pylingual.stderr.txt` |

Duplicate/example inputs:
- `dovado_rtl-0.10.12.tar.gz::dovado_rtl-0.10.12/dovado_rtl/parsers/system_verilog/generated/__pycache__/SystemVerilogParser.cpython-39.pyc`
- `data/rq3/cpython-3.9/unique_bug_pyc/cpython-39-02bda83cf25f.pyc`
- `data/rq3/cpython-3.9/unique_bug_pyc/cpython-39-ccfa2db55ee1.pyc`

Trace excerpt from `data/rq4/tool_traces/cpython-39/cpython-39-02bda83cf25f/pylingual.stderr.txt`:
```text
timeout_after_600s
```

### `pylingual-06` CPython 3.9: `SIGILL` / process crashed with signal 4

- Combined outcomes: 2
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 2/1
- Observed statuses: `exit_-4`=2
- Stack signature: `not available`

Reproduction commands:

RQ4 representative (`rq4-pylingual-0d74aa1517e6`):
```bash
data/rq2/envs/cpython-39/bin/pylingual data/rq3/cpython-3.9/unique_bug_pyc/cpython-39-ccda63e4c86c.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ4 | `rq4-pylingual-0d74aa1517e6` | 2 | `data/rq3/cpython-3.9/unique_bug_pyc/cpython-39-ccda63e4c86c.pyc` | `data/rq4/tool_traces/cpython-39/cpython-39-ccda63e4c86c/pylingual.stdout.txt; data/rq4/tool_traces/cpython-39/cpython-39-ccda63e4c86c/pylingual.stderr.txt` |

Duplicate/example inputs:
- `data/rq3/cpython-3.9/unique_bug_pyc/cpython-39-ccda63e4c86c.pyc`
- `data/rq3/cpython-3.9/unique_bug_pyc/cpython-39-d6e24fa7ea2c.pyc`

Trace excerpt from `data/rq4/tool_traces/cpython-39/cpython-39-ccda63e4c86c/pylingual.stdout.txt`:
```text
────────────────────────────────────────────────────────────────────────────────
 ,ggggggggggg,              ,gggg,
dP"""88""""""Y8,           d8" "8I
,dPYb,
Yb,  88      `8b           88  ,dP
IP'`Yb
 `"  88      ,8P        8888888P"     gg
I8  8I
     88aaaad8P"            88         ""
I8  8'
     88"""""gg     gg      88         gg    ,ggg,,ggg,     ,gggg,gg  gg      gg
,gggg,gg  I8 dP
```

### `pylingual-07` CPython 3.10: `Timeout` / did not terminate within 600s

- Combined outcomes: 1
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 1/1
- Observed statuses: `timeout`=1
- Stack signature: `not available`

Reproduction commands:

RQ4 representative (`rq4-pylingual-ef6abb195900`):
```bash
data/rq2/envs/cpython-310/bin/pylingual data/rq3/cpython-3.10/unique_bug_pyc/cpython-310-7c36e44e9194.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ4 | `rq4-pylingual-ef6abb195900` | 1 | `data/rq3/cpython-3.10/unique_bug_pyc/cpython-310-7c36e44e9194.pyc` | `data/rq4/tool_traces/cpython-310/cpython-310-7c36e44e9194/pylingual.stdout.txt; data/rq4/tool_traces/cpython-310/cpython-310-7c36e44e9194/pylingual.stderr.txt` |

Duplicate/example inputs:
- `data/rq3/cpython-3.10/unique_bug_pyc/cpython-310-7c36e44e9194.pyc`

Trace excerpt from `data/rq4/tool_traces/cpython-310/cpython-310-7c36e44e9194/pylingual.stderr.txt`:
```text
timeout_after_600s
```

### `pylingual-08` CPython 3.8: `SIGILL` / process crashed with signal 4

- Combined outcomes: 1
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 1/1
- Observed statuses: `exit_-4`=1
- Stack signature: `not available`

Reproduction commands:

RQ4 representative (`rq4-pylingual-08252ec6a983`):
```bash
data/rq2/envs/cpython-38/bin/pylingual data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-ee3258669fff.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ4 | `rq4-pylingual-08252ec6a983` | 1 | `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-ee3258669fff.pyc` | `data/rq4/tool_traces/cpython-38/cpython-38-ee3258669fff/pylingual.stdout.txt; data/rq4/tool_traces/cpython-38/cpython-38-ee3258669fff/pylingual.stderr.txt` |

Duplicate/example inputs:
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-ee3258669fff.pyc`

Trace excerpt from `data/rq4/tool_traces/cpython-38/cpython-38-ee3258669fff/pylingual.stdout.txt`:
```text
────────────────────────────────────────────────────────────────────────────────
 ,ggggggggggg,              ,gggg,
dP"""88""""""Y8,           d8" "8I
,dPYb,
Yb,  88      `8b           88  ,dP
IP'`Yb
 `"  88      ,8P        8888888P"     gg
I8  8I
     88aaaad8P"            88         ""
I8  8'
     88"""""gg     gg      88         gg    ,ggg,,ggg,     ,gggg,gg  gg      gg
,gggg,gg  I8 dP
```


## Tool: `Decompyle++`

- Combined outcomes: 4
- Combined unique signatures: 3
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 4/3
- RQ2 note: Decompyle++ produced controlled rejection diagnostics on the RQ2 failed-case replay corpus, but none were classified as robustness failures because they did not timeout, crash, or raise an uncaught traceback.
- Deduplication note: retained RQ4 stdout/stderr does not include native stack frames for the signal-terminated cases, so those cases are deduplicated by tool, CPython version, and signal/status.

| ID | Version | Failure | Cause | RQ2 | RQ4 | Total |
|---|---|---|---|---:|---:|---:|
| `decompylepp-01` | CPython 3.8 | `SIGSEGV` | process crashed with signal 11 | 0 | 2 | 2 |
| `decompylepp-02` | CPython 3.11 | `Timeout` | did not terminate within 600s | 0 | 1 | 1 |
| `decompylepp-03` | CPython 3.13 | `SIGKILL` | process terminated with signal 9 | 0 | 1 | 1 |

### `decompylepp-01` CPython 3.8: `SIGSEGV` / process crashed with signal 11

- Combined outcomes: 2
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 2/1
- Observed statuses: `exit_-11`=2
- Stack signature: not available; grouped by Decompyle++, CPython 3.8, and `SIGSEGV`

Reproduction commands:

RQ4 representative (`cpython-38-4938b2ed0078`):
```bash
PycLens/data/rq2/envs/global-decompylepp/bin/pycdc PycLens/data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-4938b2ed0078.pyc
```

RQ4 duplicate example (`cpython-38-6fc7c4e73992`):
```bash
PycLens/data/rq2/envs/global-decompylepp/bin/pycdc PycLens/data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-6fc7c4e73992.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ4 | `cpython-38-4938b2ed0078` | 1 | `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-4938b2ed0078.pyc` | `PycLens/data/rq4/tool_traces/cpython-38/cpython-38-4938b2ed0078/decompylepp.stdout.txt; PycLens/data/rq4/tool_traces/cpython-38/cpython-38-4938b2ed0078/decompylepp.stderr.txt` |
| RQ4 | `cpython-38-6fc7c4e73992` | 1 | `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-6fc7c4e73992.pyc` | `PycLens/data/rq4/tool_traces/cpython-38/cpython-38-6fc7c4e73992/decompylepp.stdout.txt; PycLens/data/rq4/tool_traces/cpython-38/cpython-38-6fc7c4e73992/decompylepp.stderr.txt` |

Trace excerpt:
- Retained stdout/stderr are empty for both signal-terminated runs; the subprocess status records `exit_-11`.

Duplicate/example inputs:
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-4938b2ed0078.pyc`
- `data/rq3/cpython-3.8/unique_bug_pyc/cpython-38-6fc7c4e73992.pyc`

### `decompylepp-02` CPython 3.11: `Timeout` / did not terminate within 600s

- Combined outcomes: 1
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 1/1
- Observed statuses: `timeout`=1
- Stack signature: not available; grouped by Decompyle++, CPython 3.11, and timeout status

Reproduction command:

RQ4 representative (`cpython-311-8748dd3d40bc`):
```bash
timeout 600s PycLens/data/rq2/envs/global-decompylepp/bin/pycdc PycLens/data/rq3/cpython-3.11/unique_bug_pyc/cpython-311-8748dd3d40bc.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ4 | `cpython-311-8748dd3d40bc` | 1 | `data/rq3/cpython-3.11/unique_bug_pyc/cpython-311-8748dd3d40bc.pyc` | `PycLens/data/rq4/tool_traces/cpython-311/cpython-311-8748dd3d40bc/decompylepp.stdout.txt; PycLens/data/rq4/tool_traces/cpython-311/cpython-311-8748dd3d40bc/decompylepp.stderr.txt` |

Trace excerpt:
- `timeout_after_600s`

Duplicate/example inputs:
- `data/rq3/cpython-3.11/unique_bug_pyc/cpython-311-8748dd3d40bc.pyc`

### `decompylepp-03` CPython 3.13: `SIGKILL` / process terminated with signal 9

- Combined outcomes: 1
- RQ2 outcomes/signatures: 0/0
- RQ4 outcomes/signatures: 1/1
- Observed statuses: `exit_-9`=1
- Stack signature: not available; grouped by Decompyle++, CPython 3.13, and `SIGKILL`

Reproduction command:

RQ4 representative (`cpython-313-2293b72ed067`):
```bash
PycLens/data/rq2/envs/global-decompylepp/bin/pycdc PycLens/data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-2293b72ed067.pyc
```

| Phase | Phase bug id | Outcomes | Representative input | Trace files |
|---|---|---:|---|---|
| RQ4 | `cpython-313-2293b72ed067` | 1 | `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-2293b72ed067.pyc` | `PycLens/data/rq4/tool_traces/cpython-313/cpython-313-2293b72ed067/decompylepp.stdout.txt; PycLens/data/rq4/tool_traces/cpython-313/cpython-313-2293b72ed067/decompylepp.stderr.txt` |

Trace excerpt:
- Retained stdout/stderr are empty; the subprocess status records `exit_-9`.

Duplicate/example inputs:
- `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-2293b72ed067.pyc`
