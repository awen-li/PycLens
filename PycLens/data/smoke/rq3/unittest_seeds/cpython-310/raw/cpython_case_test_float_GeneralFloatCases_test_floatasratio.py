# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: GeneralFloatCases_test_floatasratio

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (f, ratio) in [(0.875, (7, 8)), (-0.875, (-7, 8)), (0.0, (0, 1)), (11.5, (23, 2))]:
        self.assertEqual(f.as_integer_ratio(), ratio)
    for i in range(10000):
        f = random.random()
        f *= 10 ** random.randint(-100, 100)
        (n, d) = f.as_integer_ratio()
        self.assertEqual(float(n).__truediv__(d), f)
    R = fractions.Fraction
    self.assertEqual(R(0, 1), R(*float(0.0).as_integer_ratio()))
    self.assertEqual(R(5, 2), R(*float(2.5).as_integer_ratio()))
    self.assertEqual(R(1, 2), R(*float(0.5).as_integer_ratio()))
    self.assertEqual(R(4728779608739021, 2251799813685248), R(*float(2.1).as_integer_ratio()))
    self.assertEqual(R(-4728779608739021, 2251799813685248), R(*float(-2.1).as_integer_ratio()))
    self.assertEqual(R(-2100, 1), R(*float(-2100.0).as_integer_ratio()))
    self.assertRaises(OverflowError, float('inf').as_integer_ratio)
    self.assertRaises(OverflowError, float('-inf').as_integer_ratio)
    self.assertRaises(ValueError, float('nan').as_integer_ratio)
