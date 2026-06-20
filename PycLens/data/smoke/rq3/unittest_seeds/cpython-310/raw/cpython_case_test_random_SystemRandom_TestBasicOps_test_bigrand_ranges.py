# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: SystemRandom_TestBasicOps_test_bigrand_ranges

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in [40, 80, 160, 200, 211, 250, 375, 512, 550]:
        start = self.gen.randrange(2 ** (i - 2))
        stop = self.gen.randrange(2 ** i)
        if stop <= start:
            continue
        self.assertTrue(start <= self.gen.randrange(start, stop) < stop)
