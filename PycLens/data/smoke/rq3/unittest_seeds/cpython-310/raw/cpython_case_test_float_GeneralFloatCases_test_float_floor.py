# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: GeneralFloatCases_test_float_floor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsInstance(float(0.5).__floor__(), int)
    self.assertEqual(float(0.5).__floor__(), 0)
    self.assertEqual(float(1.0).__floor__(), 1)
    self.assertEqual(float(1.5).__floor__(), 1)
    self.assertEqual(float(-0.5).__floor__(), -1)
    self.assertEqual(float(-1.0).__floor__(), -1)
    self.assertEqual(float(-1.5).__floor__(), -2)
    self.assertEqual(float(1.23e+167).__floor__(), 1.23e+167)
    self.assertEqual(float(-1.23e+167).__floor__(), -1.23e+167)
    self.assertRaises(ValueError, float('nan').__floor__)
    self.assertRaises(OverflowError, float('inf').__floor__)
    self.assertRaises(OverflowError, float('-inf').__floor__)
