# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_bug_9025

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    n = 100000
    randrange = self.gen.randrange
    k = sum((randrange(6755399441055744) % 3 == 2 for i in range(n)))
    self.assertTrue(0.3 < k / n < 0.37, k / n)
