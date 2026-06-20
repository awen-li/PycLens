# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_algorithms_available

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(set(hashlib.algorithms_guaranteed).issubset(hashlib.algorithms_available))
    self.assertNotIn('undefined', hashlib.algorithms_available)
    for name in hashlib.algorithms_available:
        digest = hashlib.new(name, usedforsecurity=False)
