# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextFlags_test_float_operation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    FloatOperation = self.decimal.FloatOperation
    localcontext = self.decimal.localcontext
    with localcontext() as c:
        self.assertFalse(c.traps[FloatOperation])
        c.clear_flags()
        self.assertEqual(Decimal(7.5), 7.5)
        self.assertTrue(c.flags[FloatOperation])
        c.clear_flags()
        self.assertEqual(c.create_decimal(7.5), 7.5)
        self.assertTrue(c.flags[FloatOperation])
        c.clear_flags()
        x = Decimal.from_float(7.5)
        self.assertFalse(c.flags[FloatOperation])
        self.assertEqual(x, 7.5)
        self.assertTrue(c.flags[FloatOperation])
        c.clear_flags()
        x = c.create_decimal_from_float(7.5)
        self.assertFalse(c.flags[FloatOperation])
        self.assertEqual(x, 7.5)
        self.assertTrue(c.flags[FloatOperation])
        c.traps[FloatOperation] = True
        c.clear_flags()
        self.assertRaises(FloatOperation, Decimal, 7.5)
        self.assertTrue(c.flags[FloatOperation])
        c.clear_flags()
        self.assertRaises(FloatOperation, c.create_decimal, 7.5)
        self.assertTrue(c.flags[FloatOperation])
        c.clear_flags()
        x = Decimal.from_float(7.5)
        self.assertFalse(c.flags[FloatOperation])
        c.clear_flags()
        x = c.create_decimal_from_float(7.5)
        self.assertFalse(c.flags[FloatOperation])
