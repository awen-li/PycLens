# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unary.py
# case: UnaryOpTestCase_test_negation_of_exponentiation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(-2 ** 3, -8)
    self.assertEqual((-2) ** 3, -8)
    self.assertEqual(-2 ** 4, -16)
    self.assertEqual((-2) ** 4, 16)
