# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: MersenneTwister_TestBasicOps_test_getrandbits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    super().test_getrandbits()
    self.gen.seed(1234567)
    self.assertEqual(self.gen.getrandbits(100), 97904845777343510404718956115)
