# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: MathTests_test_inf_constant

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(math.isinf(math.inf))
    self.assertGreater(math.inf, 0.0)
    self.assertEqual(math.inf, float('inf'))
    self.assertEqual(-math.inf, float('-inf'))
