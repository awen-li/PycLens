# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: Coverage_test_round

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    localcontext = self.decimal.localcontext
    with localcontext() as c:
        c.prec = 28
        self.assertEqual(str(Decimal('9.99').__round__()), '10')
        self.assertEqual(str(Decimal('9.99e-5').__round__()), '0')
        self.assertEqual(str(Decimal('1.23456789').__round__(5)), '1.23457')
        self.assertEqual(str(Decimal('1.2345').__round__(10)), '1.2345000000')
        self.assertEqual(str(Decimal('1.2345').__round__(-10)), '0E+10')
        self.assertRaises(TypeError, Decimal('1.23').__round__, '5')
        self.assertRaises(TypeError, Decimal('1.23').__round__, 5, 8)
