# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestGeometricMean_test_big_and_small

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    geometric_mean = statistics.geometric_mean
    large = 2.0 ** 1000
    big_gm = geometric_mean([54.0 * large, 24.0 * large, 36.0 * large])
    self.assertTrue(math.isclose(big_gm, 36.0 * large))
    self.assertFalse(math.isinf(big_gm))
    small = 2.0 ** (-1000)
    small_gm = geometric_mean([54.0 * small, 24.0 * small, 36.0 * small])
    self.assertTrue(math.isclose(small_gm, 36.0 * small))
    self.assertNotEqual(small_gm, 0.0)
