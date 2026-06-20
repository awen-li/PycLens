# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_lt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module
    self.assertRaises(TypeError, operator.lt)
    self.assertRaises(TypeError, operator.lt, 1j, 2j)
    self.assertFalse(operator.lt(1, 0))
    self.assertFalse(operator.lt(1, 0.0))
    self.assertFalse(operator.lt(1, 1))
    self.assertFalse(operator.lt(1, 1.0))
    self.assertTrue(operator.lt(1, 2))
    self.assertTrue(operator.lt(1, 2.0))
