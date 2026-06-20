# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hash.py
# case: HashEqualityTestCase_test_numeric_literals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.same_hash(1, 1, 1.0, 1.0 + 0j)
    self.same_hash(0, 0.0, 0.0 + 0j)
    self.same_hash(-1, -1.0, -1.0 + 0j)
    self.same_hash(-2, -2.0, -2.0 + 0j)
