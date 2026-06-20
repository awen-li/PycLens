# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ArithmeticOperatorsTest_test_subtraction

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    d1 = Decimal('-11.1')
    d2 = Decimal('22.2')
    self.assertEqual(d1 - d2, Decimal('-33.3'))
    self.assertEqual(d2 - d1, Decimal('33.3'))
    c = d1 - 5
    self.assertEqual(c, Decimal('-16.1'))
    self.assertEqual(type(c), type(d1))
    c = 5 - d1
    self.assertEqual(c, Decimal('16.1'))
    self.assertEqual(type(c), type(d1))
    d1 -= d2
    self.assertEqual(d1, Decimal('-33.3'))
    d1 -= 5
    self.assertEqual(d1, Decimal('-38.3'))
