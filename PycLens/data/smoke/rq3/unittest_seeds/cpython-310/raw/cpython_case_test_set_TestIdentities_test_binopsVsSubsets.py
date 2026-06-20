# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestIdentities_test_binopsVsSubsets

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (a, b) = (self.a, self.b)
    self.assertTrue(a - b < a)
    self.assertTrue(b - a < b)
    self.assertTrue(a & b < a)
    self.assertTrue(a & b < b)
    self.assertTrue(a | b > a)
    self.assertTrue(a | b > b)
    self.assertTrue(a ^ b < a | b)
