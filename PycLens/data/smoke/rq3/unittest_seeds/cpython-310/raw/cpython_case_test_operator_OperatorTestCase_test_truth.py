# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_truth

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module

    class C(object):

        def __bool__(self):
            raise SyntaxError
    self.assertRaises(TypeError, operator.truth)
    self.assertRaises(SyntaxError, operator.truth, C())
    self.assertTrue(operator.truth(5))
    self.assertTrue(operator.truth([0]))
    self.assertFalse(operator.truth(0))
    self.assertFalse(operator.truth([]))
