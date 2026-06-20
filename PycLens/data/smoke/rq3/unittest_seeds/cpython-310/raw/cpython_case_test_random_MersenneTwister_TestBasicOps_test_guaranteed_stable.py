# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: MersenneTwister_TestBasicOps_test_guaranteed_stable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.gen.seed(3456147, version=1)
    self.assertEqual([self.gen.random().hex() for i in range(4)], ['0x1.ac362300d90d2p-1', '0x1.9d16f74365005p-1', '0x1.1ebb4352e4c4dp-1', '0x1.1a7422abf9c11p-1'])
    self.gen.seed('the quick brown fox', version=2)
    self.assertEqual([self.gen.random().hex() for i in range(4)], ['0x1.1239ddfb11b7cp-3', '0x1.b3cbb5c51b120p-4', '0x1.8c4f55116b60fp-1', '0x1.63eb525174a27p-1'])
