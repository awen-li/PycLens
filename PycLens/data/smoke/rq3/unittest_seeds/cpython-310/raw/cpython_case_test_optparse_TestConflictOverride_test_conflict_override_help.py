# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestConflictOverride_test_conflict_override_help

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertOutput(['-h'], 'Options:\n  -h, --help     show this help message and exit\n  -n, --dry-run  dry run mode\n')
