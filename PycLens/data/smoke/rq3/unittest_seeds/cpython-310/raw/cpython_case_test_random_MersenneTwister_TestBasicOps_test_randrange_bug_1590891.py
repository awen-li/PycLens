# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: MersenneTwister_TestBasicOps_test_randrange_bug_1590891

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    start = 1000000000000
    stop = -100000000000000000000
    step = -200
    x = self.gen.randrange(start, stop, step)
    self.assertTrue(stop < x <= start)
    self.assertEqual((x + stop) % step, 0)
