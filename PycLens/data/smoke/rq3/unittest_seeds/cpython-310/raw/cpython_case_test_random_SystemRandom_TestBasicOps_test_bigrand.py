# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: SystemRandom_TestBasicOps_test_bigrand

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    span = 2 ** 500
    cum = 0
    for i in range(100):
        r = self.gen.randrange(span)
        self.assertTrue(0 <= r < span)
        cum |= r
    self.assertEqual(cum, span - 1)
