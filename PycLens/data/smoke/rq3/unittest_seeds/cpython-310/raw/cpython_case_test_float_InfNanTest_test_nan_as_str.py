# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: InfNanTest_test_nan_as_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(repr(1e+300 * 1e+300 * 0), 'nan')
    self.assertEqual(repr(-1e+300 * 1e+300 * 0), 'nan')
    self.assertEqual(str(1e+300 * 1e+300 * 0), 'nan')
    self.assertEqual(str(-1e+300 * 1e+300 * 0), 'nan')
