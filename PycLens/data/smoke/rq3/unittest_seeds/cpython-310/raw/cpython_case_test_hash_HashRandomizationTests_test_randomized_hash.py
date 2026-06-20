# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hash.py
# case: HashRandomizationTests_test_randomized_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    run1 = self.get_hash(self.repr_, seed='random')
    run2 = self.get_hash(self.repr_, seed='random')
    self.assertNotEqual(run1, run2)
