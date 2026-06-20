# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pstats.py
# case: StatsTestCase_test_get_stats_profile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def pass1():
        pass

    def pass2():
        pass

    def pass3():
        pass
    pr = cProfile.Profile()
    pr.enable()
    pass1()
    pass2()
    pass3()
    pr.create_stats()
    ps = pstats.Stats(pr)
    stats_profile = ps.get_stats_profile()
    funcs_called = set(stats_profile.func_profiles.keys())
    self.assertIn('pass1', funcs_called)
    self.assertIn('pass2', funcs_called)
    self.assertIn('pass3', funcs_called)
