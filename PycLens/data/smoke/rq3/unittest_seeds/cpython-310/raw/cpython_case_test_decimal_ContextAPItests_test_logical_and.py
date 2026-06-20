# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextAPItests_test_logical_and

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    Context = self.decimal.Context
    c = Context()
    d = c.logical_and(Decimal(1), Decimal(1))
    self.assertEqual(c.logical_and(1, 1), d)
    self.assertEqual(c.logical_and(Decimal(1), 1), d)
    self.assertEqual(c.logical_and(1, Decimal(1)), d)
    self.assertRaises(TypeError, c.logical_and, '1', 1)
    self.assertRaises(TypeError, c.logical_and, 1, '1')
