# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_autoseed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.gen.seed()
    state1 = self.gen.getstate()
    time.sleep(0.1)
    self.gen.seed()
    state2 = self.gen.getstate()
    self.assertNotEqual(state1, state2)
