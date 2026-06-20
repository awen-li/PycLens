# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abstract_numbers.py
# case: TestNumbers_test_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(issubclass(int, Integral))
    self.assertTrue(issubclass(int, Complex))
    self.assertEqual(7, int(7).real)
    self.assertEqual(0, int(7).imag)
    self.assertEqual(7, int(7).conjugate())
    self.assertEqual(-7, int(-7).conjugate())
    self.assertEqual(7, int(7).numerator)
    self.assertEqual(1, int(7).denominator)
