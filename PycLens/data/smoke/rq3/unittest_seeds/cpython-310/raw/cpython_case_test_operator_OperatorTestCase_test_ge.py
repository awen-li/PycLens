# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_ge

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module
    self.assertRaises(TypeError, operator.ge)
    self.assertRaises(TypeError, operator.ge, 1j, 2j)
    self.assertTrue(operator.ge(1, 0))
    self.assertTrue(operator.ge(1, 0.0))
    self.assertTrue(operator.ge(1, 1))
    self.assertTrue(operator.ge(1, 1.0))
    self.assertFalse(operator.ge(1, 2))
    self.assertFalse(operator.ge(1, 2.0))
