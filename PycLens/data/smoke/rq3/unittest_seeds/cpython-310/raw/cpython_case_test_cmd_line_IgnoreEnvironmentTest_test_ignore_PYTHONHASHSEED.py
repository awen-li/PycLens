# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: IgnoreEnvironmentTest_test_ignore_PYTHONHASHSEED

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.run_ignoring_vars('sys.flags.hash_randomization == 1', PYTHONHASHSEED='0')
