# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_sample_inputs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.gen.sample(range(20), 2)
    self.gen.sample(range(20), 2)
    self.gen.sample(str('abcdefghijklmnopqrst'), 2)
    self.gen.sample(tuple('abcdefghijklmnopqrst'), 2)
