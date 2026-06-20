# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: Coverage_test_implicit_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    localcontext = self.decimal.localcontext
    with localcontext() as c:
        c.prec = 1
        c.Emax = 1
        c.Emin = -1
        self.assertEqual(abs(Decimal('-10')), 10)
        self.assertEqual(Decimal('7') + 1, 8)
        self.assertEqual(Decimal('10') / 5, 2)
        self.assertEqual(Decimal('10') // 7, 1)
        self.assertEqual(Decimal('1.2').fma(Decimal('0.01'), 1), 1)
        self.assertIs(Decimal('NaN').fma(7, 1).is_nan(), True)
        self.assertEqual(pow(Decimal(10), 2, 7), 2)
        self.assertEqual(Decimal('1.01').exp(), 3)
        self.assertIs(Decimal('0.01').is_normal(), False)
        self.assertIs(Decimal('0.01').is_subnormal(), True)
        self.assertEqual(Decimal('20').ln(), 3)
        self.assertEqual(Decimal('20').log10(), 1)
        self.assertEqual(Decimal('580').logb(), 2)
        self.assertEqual(Decimal('10').logical_invert(), 1)
        self.assertEqual(-Decimal('-10'), 10)
        self.assertEqual(Decimal('2') * 4, 8)
        self.assertEqual(Decimal('10').next_minus(), 9)
        self.assertEqual(Decimal('10').next_plus(), Decimal('2E+1'))
        self.assertEqual(Decimal('-10').normalize(), Decimal('-1E+1'))
        self.assertEqual(Decimal('10').number_class(), '+Normal')
        self.assertEqual(+Decimal('-1'), -1)
        self.assertEqual(Decimal('10') % 7, 3)
        self.assertEqual(Decimal('10') - 7, 3)
        self.assertEqual(Decimal('1.12345').to_integral_exact(), 1)
        self.assertTrue(Decimal('1').is_canonical())
        self.assertTrue(Decimal('1').is_finite())
        self.assertTrue(Decimal('1').is_finite())
        self.assertTrue(Decimal('snan').is_snan())
        self.assertTrue(Decimal('-1').is_signed())
        self.assertTrue(Decimal('0').is_zero())
        self.assertTrue(Decimal('0').is_zero())
    with localcontext() as c:
        c.prec = 10000
        x = 1228 ** 1523
        y = -Decimal(x)
        z = y.copy_abs()
        self.assertEqual(z, x)
        z = y.copy_negate()
        self.assertEqual(z, x)
        z = y.copy_sign(Decimal(1))
        self.assertEqual(z, x)
