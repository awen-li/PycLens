# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestBool_test_bool_true

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (options, args) = self.assertParseOK(['-v'], {'verbose': 1}, [])
    self.assertTrue(options.verbose is True)
