# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_pow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module
    self.assertRaises(TypeError, operator.pow)
    self.assertRaises(TypeError, operator.pow, None, None)
    self.assertEqual(operator.pow(3, 5), 3 ** 5)
    self.assertRaises(TypeError, operator.pow, 1)
    self.assertRaises(TypeError, operator.pow, 1, 2, 3)
