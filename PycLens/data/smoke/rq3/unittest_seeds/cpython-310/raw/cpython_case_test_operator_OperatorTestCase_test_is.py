# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_is

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module
    a = b = 'xyzpdq'
    c = a[:3] + b[3:]
    self.assertRaises(TypeError, operator.is_)
    self.assertTrue(operator.is_(a, b))
    self.assertFalse(operator.is_(a, c))
