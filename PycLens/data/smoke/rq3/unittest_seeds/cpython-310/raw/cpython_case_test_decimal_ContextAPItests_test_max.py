# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextAPItests_test_max

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    Context = self.decimal.Context
    c = Context()
    d = c.max(Decimal(1), Decimal(2))
    self.assertEqual(c.max(1, 2), d)
    self.assertEqual(c.max(Decimal(1), 2), d)
    self.assertEqual(c.max(1, Decimal(2)), d)
    self.assertRaises(TypeError, c.max, '1', 2)
    self.assertRaises(TypeError, c.max, 1, '2')
