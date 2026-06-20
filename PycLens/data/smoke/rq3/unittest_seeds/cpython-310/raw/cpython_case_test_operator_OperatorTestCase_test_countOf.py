# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_countOf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module
    self.assertRaises(TypeError, operator.countOf)
    self.assertRaises(TypeError, operator.countOf, None, None)
    self.assertRaises(ZeroDivisionError, operator.countOf, BadIterable(), 1)
    self.assertEqual(operator.countOf([1, 2, 1, 3, 1, 4], 3), 1)
    self.assertEqual(operator.countOf([1, 2, 1, 3, 1, 4], 5), 0)
    nan = float('nan')
    self.assertEqual(operator.countOf([nan, nan, 21], nan), 2)
    self.assertEqual(operator.countOf([{}, 1, {}, 2], {}), 2)
