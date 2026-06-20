# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: IgnoreEnvironmentTest_test_sys_flags_not_set

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_outcome = '\n            (sys.flags.debug == sys.flags.optimize ==\n             sys.flags.dont_write_bytecode == sys.flags.verbose == 0)\n        '
    self.run_ignoring_vars(expected_outcome, PYTHONDEBUG='1', PYTHONOPTIMIZE='1', PYTHONDONTWRITEBYTECODE='1', PYTHONVERBOSE='1')
