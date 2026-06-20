# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pstats.py
# case: StatsTestCase_test_sort_stats_partial

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sortkey = 'filename'
    for sort_name in ['f', 'fi', 'fil', 'file', 'filen', 'filena', 'filenam', 'filename']:
        self.stats.sort_stats(sort_name)
        self.assertEqual(self.stats.sort_type, self.stats.sort_arg_dict_default[sortkey][-1])
