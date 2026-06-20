# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestIdentities_test_summations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (a, b) = (self.a, self.b)
    self.assertEqual(a - b | a & b | b - a, a | b)
    self.assertEqual(a & b | a ^ b, a | b)
    self.assertEqual(a | b - a, a | b)
    self.assertEqual(a - b | b, a | b)
    self.assertEqual(a - b | a & b, a)
    self.assertEqual(b - a | a & b, b)
    self.assertEqual(a - b | b - a, a ^ b)
