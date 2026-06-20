# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_indexOf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module
    self.assertRaises(TypeError, operator.indexOf)
    self.assertRaises(TypeError, operator.indexOf, None, None)
    self.assertRaises(ZeroDivisionError, operator.indexOf, BadIterable(), 1)
    self.assertEqual(operator.indexOf([4, 3, 2, 1], 3), 1)
    self.assertRaises(ValueError, operator.indexOf, [4, 3, 2, 1], 0)
    nan = float('nan')
    self.assertEqual(operator.indexOf([nan, nan, 21], nan), 0)
    self.assertEqual(operator.indexOf([{}, 1, {}, 2], {}), 0)
