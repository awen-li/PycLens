# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: MersenneTwister_TestBasicOps_test_randbytes_getrandbits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    seed = 2849427419
    gen2 = random.Random()
    self.gen.seed(seed)
    gen2.seed(seed)
    for n in range(9):
        self.assertEqual(self.gen.randbytes(n), gen2.getrandbits(n * 8).to_bytes(n, 'little'))
