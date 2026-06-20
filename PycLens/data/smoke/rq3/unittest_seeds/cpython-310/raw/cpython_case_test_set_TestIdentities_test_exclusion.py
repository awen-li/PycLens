# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestIdentities_test_exclusion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (a, b, zero) = (self.a, self.b, set())
    self.assertEqual(a - b & b, zero)
    self.assertEqual(b - a & a, zero)
    self.assertEqual(a & b & (a ^ b), zero)
