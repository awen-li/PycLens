# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestHarmonicMean_test_negative_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exc = statistics.StatisticsError
    for values in ([-1], [1, -2, 3]):
        with self.subTest(values=values):
            self.assertRaises(exc, self.func, values)
