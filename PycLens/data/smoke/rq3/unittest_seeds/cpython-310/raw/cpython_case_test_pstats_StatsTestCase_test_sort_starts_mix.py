# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pstats.py
# case: StatsTestCase_test_sort_starts_mix

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, self.stats.sort_stats, 'calls', SortKey.TIME)
    self.assertRaises(TypeError, self.stats.sort_stats, SortKey.TIME, 'calls')
