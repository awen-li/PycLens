# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestIdentities_test_commutativity

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (a, b) = (self.a, self.b)
    self.assertEqual(a & b, b & a)
    self.assertEqual(a | b, b | a)
    self.assertEqual(a ^ b, b ^ a)
    if a != b:
        self.assertNotEqual(a - b, b - a)
