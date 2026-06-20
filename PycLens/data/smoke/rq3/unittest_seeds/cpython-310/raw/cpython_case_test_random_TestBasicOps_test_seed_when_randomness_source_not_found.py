# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_seed_when_randomness_source_not_found

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    urandom_mock.side_effect = NotImplementedError
    self.test_seedargs()
