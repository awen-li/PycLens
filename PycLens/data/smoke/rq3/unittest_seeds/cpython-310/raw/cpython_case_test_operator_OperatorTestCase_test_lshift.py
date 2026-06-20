# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_lshift

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module
    self.assertRaises(TypeError, operator.lshift)
    self.assertRaises(TypeError, operator.lshift, None, 42)
    self.assertEqual(operator.lshift(5, 1), 10)
    self.assertEqual(operator.lshift(5, 0), 5)
    self.assertRaises(ValueError, operator.lshift, 2, -1)
