# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_pos

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module
    self.assertRaises(TypeError, operator.pos)
    self.assertRaises(TypeError, operator.pos, None)
    self.assertEqual(operator.pos(5), 5)
    self.assertEqual(operator.pos(-5), -5)
    self.assertEqual(operator.pos(0), 0)
    self.assertEqual(operator.pos(-0), 0)
