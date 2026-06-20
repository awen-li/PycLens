# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestOptionChecks_test_no_nargs_for_action

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertOptionError("option -b: 'nargs' must not be supplied for action 'count'", ['-b'], {'action': 'count', 'nargs': 2})
