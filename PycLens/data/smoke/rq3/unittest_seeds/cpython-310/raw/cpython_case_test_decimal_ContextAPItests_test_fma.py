# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextAPItests_test_fma

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    Context = self.decimal.Context
    c = Context()
    d = c.fma(Decimal(2), Decimal(3), Decimal(4))
    self.assertEqual(c.fma(2, 3, 4), d)
    self.assertEqual(c.fma(Decimal(2), 3, 4), d)
    self.assertEqual(c.fma(2, Decimal(3), 4), d)
    self.assertEqual(c.fma(2, 3, Decimal(4)), d)
    self.assertEqual(c.fma(Decimal(2), Decimal(3), 4), d)
    self.assertRaises(TypeError, c.fma, '2', 3, 4)
    self.assertRaises(TypeError, c.fma, 2, '3', 4)
    self.assertRaises(TypeError, c.fma, 2, 3, '4')
    self.assertRaises(TypeError, c.fma, Decimal('Infinity'), Decimal(0), 'not a decimal')
    self.assertRaises(TypeError, c.fma, Decimal(1), Decimal('snan'), 1.222)
    self.assertRaises(TypeError, Decimal('Infinity').fma, Decimal(0), 'not a decimal')
    self.assertRaises(TypeError, Decimal(1).fma, Decimal('snan'), 1.222)
