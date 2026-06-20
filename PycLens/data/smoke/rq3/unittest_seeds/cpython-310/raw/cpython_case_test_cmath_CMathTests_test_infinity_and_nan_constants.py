# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmath.py
# case: CMathTests_test_infinity_and_nan_constants

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(cmath.inf.real, math.inf)
    self.assertEqual(cmath.inf.imag, 0.0)
    self.assertEqual(cmath.infj.real, 0.0)
    self.assertEqual(cmath.infj.imag, math.inf)
    self.assertTrue(math.isnan(cmath.nan.real))
    self.assertEqual(cmath.nan.imag, 0.0)
    self.assertEqual(cmath.nanj.real, 0.0)
    self.assertTrue(math.isnan(cmath.nanj.imag))
    self.assertEqual(repr(cmath.inf), 'inf')
    self.assertEqual(repr(cmath.infj), 'infj')
    self.assertEqual(repr(cmath.nan), 'nan')
    self.assertEqual(repr(cmath.nanj), 'nanj')
