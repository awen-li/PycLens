# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestBivariateStatistics_test_unequal_size_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (x, y) in [([1, 2, 3], [1, 2]), ([1, 2], [1, 2, 3])]:
        with self.assertRaises(statistics.StatisticsError):
            statistics.covariance(x, y)
        with self.assertRaises(statistics.StatisticsError):
            statistics.correlation(x, y)
        with self.assertRaises(statistics.StatisticsError):
            statistics.linear_regression(x, y)
