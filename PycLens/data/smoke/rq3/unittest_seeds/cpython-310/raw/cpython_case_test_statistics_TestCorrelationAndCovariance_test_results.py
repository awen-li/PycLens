# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestCorrelationAndCovariance_test_results

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (x, y, result) in [([1, 2, 3], [1, 2, 3], 1), ([1, 2, 3], [-1, -2, -3], -1), ([1, 2, 3], [3, 2, 1], -1), ([1, 2, 3], [1, 2, 1], 0), ([1, 2, 3], [1, 3, 2], 0.5)]:
        self.assertAlmostEqual(statistics.correlation(x, y), result)
        self.assertAlmostEqual(statistics.covariance(x, y), result)
