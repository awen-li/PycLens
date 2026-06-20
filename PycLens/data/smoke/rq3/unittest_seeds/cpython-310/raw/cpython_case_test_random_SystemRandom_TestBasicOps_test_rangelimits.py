# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: SystemRandom_TestBasicOps_test_rangelimits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (start, stop) in [(-2, 0), (-2 ** 60 - 2, -2 ** 60), (2 ** 60, 2 ** 60 + 2)]:
        self.assertEqual(set(range(start, stop)), set([self.gen.randrange(start, stop) for i in range(100)]))
