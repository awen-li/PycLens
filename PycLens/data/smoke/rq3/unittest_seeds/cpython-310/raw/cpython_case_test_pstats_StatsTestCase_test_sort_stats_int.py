# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pstats.py
# case: StatsTestCase_test_sort_stats_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    valid_args = {-1: 'stdname', 0: 'calls', 1: 'time', 2: 'cumulative'}
    for (arg_int, arg_str) in valid_args.items():
        self.stats.sort_stats(arg_int)
        self.assertEqual(self.stats.sort_type, self.stats.sort_arg_dict_default[arg_str][-1])
