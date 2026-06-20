# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestCorrelationAndCovariance_test_different_scales

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = [1, 2, 3]
    y = [10, 30, 20]
    self.assertAlmostEqual(statistics.correlation(x, y), 0.5)
    self.assertAlmostEqual(statistics.covariance(x, y), 5)
    y = [0.1, 0.2, 0.3]
    self.assertAlmostEqual(statistics.correlation(x, y), 1)
    self.assertAlmostEqual(statistics.covariance(x, y), 0.1)
