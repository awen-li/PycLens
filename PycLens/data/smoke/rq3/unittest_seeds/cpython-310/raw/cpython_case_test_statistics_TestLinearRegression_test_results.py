# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestLinearRegression_test_results

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (x, y, true_intercept, true_slope) in [([1, 2, 3], [0, 0, 0], 0, 0), ([1, 2, 3], [1, 2, 3], 0, 1), ([1, 2, 3], [100, 100, 100], 100, 0), ([1, 2, 3], [12, 14, 16], 10, 2), ([1, 2, 3], [-1, -2, -3], 0, -1), ([1, 2, 3], [21, 22, 23], 20, 1), ([1, 2, 3], [5.1, 5.2, 5.3], 5, 0.1)]:
        (slope, intercept) = statistics.linear_regression(x, y)
        self.assertAlmostEqual(intercept, true_intercept)
        self.assertAlmostEqual(slope, true_slope)
