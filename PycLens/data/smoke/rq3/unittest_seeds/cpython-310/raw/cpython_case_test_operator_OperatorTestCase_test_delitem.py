# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_delitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module
    a = [4, 3, 2, 1]
    self.assertRaises(TypeError, operator.delitem, a)
    self.assertRaises(TypeError, operator.delitem, a, None)
    self.assertIsNone(operator.delitem(a, 1))
    self.assertEqual(a, [4, 2, 1])
