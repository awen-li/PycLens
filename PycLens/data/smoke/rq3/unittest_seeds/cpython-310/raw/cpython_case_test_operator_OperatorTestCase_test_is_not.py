# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_is_not

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module
    a = b = 'xyzpdq'
    c = a[:3] + b[3:]
    self.assertRaises(TypeError, operator.is_not)
    self.assertFalse(operator.is_not(a, b))
    self.assertTrue(operator.is_not(a, c))
