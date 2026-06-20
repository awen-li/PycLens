# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ArithmeticOperatorsTest_test_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    d1 = Decimal('5')
    d2 = Decimal('2')
    self.assertEqual(d1 % d2, Decimal('1'))
    self.assertEqual(d2 % d1, Decimal('2'))
    c = d1 % 4
    self.assertEqual(c, Decimal('1'))
    self.assertEqual(type(c), type(d1))
    c = 7 % d1
    self.assertEqual(c, Decimal('2'))
    self.assertEqual(type(c), type(d1))
    d1 %= d2
    self.assertEqual(d1, Decimal('1'))
    d1 %= 4
    self.assertEqual(d1, Decimal('1'))
