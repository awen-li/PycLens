# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: SystemRandom_TestBasicOps_test_53_bits_per_float

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    span = 2 ** 53
    cum = 0
    for i in range(100):
        cum |= int(self.gen.random() * span)
    self.assertEqual(cum, span - 1)
