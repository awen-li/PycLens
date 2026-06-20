# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_eq

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module

    class C(object):

        def __eq__(self, other):
            raise SyntaxError
    self.assertRaises(TypeError, operator.eq)
    self.assertRaises(SyntaxError, operator.eq, C(), C())
    self.assertFalse(operator.eq(1, 0))
    self.assertFalse(operator.eq(1, 0.0))
    self.assertTrue(operator.eq(1, 1))
    self.assertTrue(operator.eq(1, 1.0))
    self.assertFalse(operator.eq(1, 2))
    self.assertFalse(operator.eq(1, 2.0))
