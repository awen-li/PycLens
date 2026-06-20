# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: UnivariateCommonMixin_test_empty_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for empty in ([], (), iter([])):
        self.assertRaises(statistics.StatisticsError, self.func, empty)
