# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ArithmeticOperatorsTest_test_floor_div_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    d1 = Decimal('5')
    d2 = Decimal('2')
    (p, q) = divmod(d1, d2)
    self.assertEqual(p, Decimal('2'))
    self.assertEqual(q, Decimal('1'))
    self.assertEqual(type(p), type(d1))
    self.assertEqual(type(q), type(d1))
    (p, q) = divmod(d1, 4)
    self.assertEqual(p, Decimal('1'))
    self.assertEqual(q, Decimal('1'))
    self.assertEqual(type(p), type(d1))
    self.assertEqual(type(q), type(d1))
    (p, q) = divmod(7, d1)
    self.assertEqual(p, Decimal('1'))
    self.assertEqual(q, Decimal('2'))
    self.assertEqual(type(p), type(d1))
    self.assertEqual(type(q), type(d1))
