# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_rshift

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module
    self.assertRaises(TypeError, operator.rshift)
    self.assertRaises(TypeError, operator.rshift, None, 42)
    self.assertEqual(operator.rshift(5, 1), 2)
    self.assertEqual(operator.rshift(5, 0), 5)
    self.assertRaises(ValueError, operator.rshift, 2, -1)
