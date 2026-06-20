# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_setitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module
    a = list(range(3))
    self.assertRaises(TypeError, operator.setitem, a)
    self.assertRaises(TypeError, operator.setitem, a, None, None)
    self.assertIsNone(operator.setitem(a, 0, 2))
    self.assertEqual(a, [2, 1, 2])
    self.assertRaises(IndexError, operator.setitem, a, 4, 2)
