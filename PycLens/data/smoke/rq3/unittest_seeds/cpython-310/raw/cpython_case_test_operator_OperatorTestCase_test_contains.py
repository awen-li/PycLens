# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_contains

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module
    self.assertRaises(TypeError, operator.contains)
    self.assertRaises(TypeError, operator.contains, None, None)
    self.assertRaises(ZeroDivisionError, operator.contains, BadIterable(), 1)
    self.assertTrue(operator.contains(range(4), 2))
    self.assertFalse(operator.contains(range(4), 5))
