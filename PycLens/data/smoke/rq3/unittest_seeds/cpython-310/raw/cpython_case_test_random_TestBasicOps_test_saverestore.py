# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_saverestore

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    N = 1000
    self.gen.seed()
    state = self.gen.getstate()
    randseq = self.randomlist(N)
    self.gen.setstate(state)
    self.assertEqual(randseq, self.randomlist(N))
