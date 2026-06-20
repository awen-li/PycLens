# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: SystemRandom_TestBasicOps_test_saverestore

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(NotImplementedError, self.gen.getstate)
    self.assertRaises(NotImplementedError, self.gen.setstate, None)
