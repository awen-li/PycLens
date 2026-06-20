# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_float_literals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(SyntaxError, eval, '2e')
    self.assertRaises(SyntaxError, eval, '2.0e+')
    self.assertRaises(SyntaxError, eval, '1e-')
    self.assertRaises(SyntaxError, eval, '3-4e/21')
