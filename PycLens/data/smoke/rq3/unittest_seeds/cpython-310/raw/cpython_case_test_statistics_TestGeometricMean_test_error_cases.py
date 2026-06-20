# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestGeometricMean_test_error_cases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    geometric_mean = statistics.geometric_mean
    StatisticsError = statistics.StatisticsError
    with self.assertRaises(StatisticsError):
        geometric_mean([])
    with self.assertRaises(StatisticsError):
        geometric_mean([3.5, 0.0, 5.25])
    with self.assertRaises(StatisticsError):
        geometric_mean([3.5, -4.0, 5.25])
    with self.assertRaises(StatisticsError):
        geometric_mean(iter([]))
    with self.assertRaises(TypeError):
        geometric_mean(None)
    with self.assertRaises(TypeError):
        geometric_mean([10, None, 20])
    with self.assertRaises(TypeError):
        geometric_mean()
    with self.assertRaises(TypeError):
        geometric_mean([10, 20, 60], 70)
