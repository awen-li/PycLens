# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: RoundTestCase_test_inf_nan

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(OverflowError, round, INF)
    self.assertRaises(OverflowError, round, -INF)
    self.assertRaises(ValueError, round, NAN)
    self.assertRaises(TypeError, round, INF, 0.0)
    self.assertRaises(TypeError, round, -INF, 1.0)
    self.assertRaises(TypeError, round, NAN, "ceci n'est pas un integer")
    self.assertRaises(TypeError, round, -0.0, 1j)
