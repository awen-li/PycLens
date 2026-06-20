# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestFMean_test_error_cases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fmean = statistics.fmean
    StatisticsError = statistics.StatisticsError
    with self.assertRaises(StatisticsError):
        fmean([])
    with self.assertRaises(StatisticsError):
        fmean(iter([]))
    with self.assertRaises(TypeError):
        fmean(None)
    with self.assertRaises(TypeError):
        fmean([10, None, 20])
    with self.assertRaises(TypeError):
        fmean()
    with self.assertRaises(TypeError):
        fmean([10, 20, 60], 70)
