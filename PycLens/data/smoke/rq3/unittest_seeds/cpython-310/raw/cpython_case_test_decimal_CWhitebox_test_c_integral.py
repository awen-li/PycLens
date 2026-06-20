# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CWhitebox_test_c_integral

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = C.Decimal
    Inexact = C.Inexact
    localcontext = C.localcontext
    x = Decimal(10)
    self.assertEqual(x.to_integral(), 10)
    self.assertRaises(TypeError, x.to_integral, '10')
    self.assertRaises(TypeError, x.to_integral, 10, 'x')
    self.assertRaises(TypeError, x.to_integral, 10)
    self.assertEqual(x.to_integral_value(), 10)
    self.assertRaises(TypeError, x.to_integral_value, '10')
    self.assertRaises(TypeError, x.to_integral_value, 10, 'x')
    self.assertRaises(TypeError, x.to_integral_value, 10)
    self.assertEqual(x.to_integral_exact(), 10)
    self.assertRaises(TypeError, x.to_integral_exact, '10')
    self.assertRaises(TypeError, x.to_integral_exact, 10, 'x')
    self.assertRaises(TypeError, x.to_integral_exact, 10)
    with localcontext() as c:
        x = Decimal('99999999999999999999999999.9').to_integral_value(ROUND_UP)
        self.assertEqual(x, Decimal('100000000000000000000000000'))
        x = Decimal('99999999999999999999999999.9').to_integral_exact(ROUND_UP)
        self.assertEqual(x, Decimal('100000000000000000000000000'))
        c.traps[Inexact] = True
        self.assertRaises(Inexact, Decimal('999.9').to_integral_exact, ROUND_UP)
