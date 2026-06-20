# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CWhitebox_test_c_funcs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = C.Decimal
    InvalidOperation = C.InvalidOperation
    DivisionByZero = C.DivisionByZero
    getcontext = C.getcontext
    localcontext = C.localcontext
    self.assertEqual(Decimal('9.99e10').to_eng_string(), '99.9E+9')
    self.assertRaises(TypeError, pow, Decimal(1), 2, '3')
    self.assertRaises(TypeError, Decimal(9).number_class, 'x', 'y')
    self.assertRaises(TypeError, Decimal(9).same_quantum, 3, 'x', 'y')
    self.assertRaises(TypeError, Decimal('1.23456789').quantize, Decimal('1e-100000'), [])
    self.assertRaises(TypeError, Decimal('1.23456789').quantize, Decimal('1e-100000'), getcontext())
    self.assertRaises(TypeError, Decimal('1.23456789').quantize, Decimal('1e-100000'), 10)
    self.assertRaises(TypeError, Decimal('1.23456789').quantize, Decimal('1e-100000'), ROUND_UP, 1000)
    with localcontext() as c:
        c.clear_traps()
        self.assertRaises(TypeError, c.copy_sign, Decimal(1), 'x', 'y')
        self.assertRaises(TypeError, c.canonical, 200)
        self.assertRaises(TypeError, c.is_canonical, 200)
        self.assertRaises(TypeError, c.divmod, 9, 8, 'x', 'y')
        self.assertRaises(TypeError, c.same_quantum, 9, 3, 'x', 'y')
        self.assertEqual(str(c.canonical(Decimal(200))), '200')
        self.assertEqual(c.radix(), 10)
        c.traps[DivisionByZero] = True
        self.assertRaises(DivisionByZero, Decimal(9).__divmod__, 0)
        self.assertRaises(DivisionByZero, c.divmod, 9, 0)
        self.assertTrue(c.flags[InvalidOperation])
        c.clear_flags()
        c.traps[InvalidOperation] = True
        self.assertRaises(InvalidOperation, Decimal(9).__divmod__, 0)
        self.assertRaises(InvalidOperation, c.divmod, 9, 0)
        self.assertTrue(c.flags[DivisionByZero])
        c.traps[InvalidOperation] = True
        c.prec = 2
        self.assertRaises(InvalidOperation, pow, Decimal(1000), 1, 501)
