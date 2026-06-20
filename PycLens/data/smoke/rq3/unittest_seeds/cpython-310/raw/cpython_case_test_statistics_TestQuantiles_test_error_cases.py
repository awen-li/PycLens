# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestQuantiles_test_error_cases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    quantiles = statistics.quantiles
    StatisticsError = statistics.StatisticsError
    with self.assertRaises(TypeError):
        quantiles()
    with self.assertRaises(TypeError):
        quantiles([10, 20, 30], 13, n=4)
    with self.assertRaises(TypeError):
        quantiles([10, 20, 30], 4)
    with self.assertRaises(StatisticsError):
        quantiles([10, 20, 30], n=0)
    with self.assertRaises(StatisticsError):
        quantiles([10, 20, 30], n=-1)
    with self.assertRaises(TypeError):
        quantiles([10, 20, 30], n=1.5)
    with self.assertRaises(ValueError):
        quantiles([10, 20, 30], method='X')
    with self.assertRaises(StatisticsError):
        quantiles([10], n=4)
    with self.assertRaises(TypeError):
        quantiles([10, None, 30], n=4)
