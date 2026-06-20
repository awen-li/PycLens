# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestOptionChecks_test_no_const_for_action

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertOptionError("option -b: 'const' must not be supplied for action 'store'", ['-b'], {'action': 'store', 'const': 1})
