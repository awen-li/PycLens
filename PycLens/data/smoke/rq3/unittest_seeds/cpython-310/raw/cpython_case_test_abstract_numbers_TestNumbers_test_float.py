# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abstract_numbers.py
# case: TestNumbers_test_float

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(issubclass(float, Rational))
    self.assertTrue(issubclass(float, Real))
    self.assertEqual(7.3, float(7.3).real)
    self.assertEqual(0, float(7.3).imag)
    self.assertEqual(7.3, float(7.3).conjugate())
    self.assertEqual(-7.3, float(-7.3).conjugate())
