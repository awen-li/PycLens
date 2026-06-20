# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fractions.py
# case: FractionTest_test_as_integer_ratio

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(F(4, 6).as_integer_ratio(), (2, 3))
    self.assertEqual(F(-4, 6).as_integer_ratio(), (-2, 3))
    self.assertEqual(F(4, -6).as_integer_ratio(), (-2, 3))
    self.assertEqual(F(0, 6).as_integer_ratio(), (0, 1))
