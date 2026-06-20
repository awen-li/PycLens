# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestOptionChecks_test_type_invalid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertOptionError("option -b: invalid option type: 'foo'", ['-b'], {'type': 'foo'})
    self.assertOptionError("option -b: invalid option type: 'tuple'", ['-b'], {'type': tuple})
