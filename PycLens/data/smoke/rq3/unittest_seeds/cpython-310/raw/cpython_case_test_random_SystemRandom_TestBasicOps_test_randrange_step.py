# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: SystemRandom_TestBasicOps_test_randrange_step

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    randrange = self.gen.randrange
    with self.assertRaises(TypeError):
        randrange(1000, step=100)
    with self.assertRaises(TypeError):
        randrange(1000, None, step=100)
