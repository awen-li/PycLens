# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextAPItests_test_power

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    Context = self.decimal.Context
    c = Context()
    d = c.power(Decimal(1), Decimal(4))
    self.assertEqual(c.power(1, 4), d)
    self.assertEqual(c.power(Decimal(1), 4), d)
    self.assertEqual(c.power(1, Decimal(4)), d)
    self.assertEqual(c.power(Decimal(1), Decimal(4)), d)
    self.assertRaises(TypeError, c.power, '1', 4)
    self.assertRaises(TypeError, c.power, 1, '4')
    self.assertEqual(c.power(modulo=5, b=8, a=2), 1)
