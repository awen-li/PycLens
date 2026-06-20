# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_neg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module
    self.assertRaises(TypeError, operator.neg)
    self.assertRaises(TypeError, operator.neg, None)
    self.assertEqual(operator.neg(5), -5)
    self.assertEqual(operator.neg(-5), 5)
    self.assertEqual(operator.neg(0), 0)
    self.assertEqual(operator.neg(-0), 0)
