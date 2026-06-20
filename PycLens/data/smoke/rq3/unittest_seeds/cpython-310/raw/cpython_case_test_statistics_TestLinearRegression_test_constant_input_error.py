# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestLinearRegression_test_constant_input_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = [1, 1, 1]
    y = [1, 2, 3]
    with self.assertRaises(statistics.StatisticsError):
        statistics.linear_regression(x, y)
