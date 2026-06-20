# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextWithStatement_test_nested_with_statements

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    Context = self.decimal.Context
    getcontext = self.decimal.getcontext
    localcontext = self.decimal.localcontext
    Clamped = self.decimal.Clamped
    Overflow = self.decimal.Overflow
    orig_ctx = getcontext()
    orig_ctx.clear_flags()
    new_ctx = Context(Emax=384)
    with localcontext() as c1:
        self.assertEqual(c1.flags, orig_ctx.flags)
        self.assertEqual(c1.traps, orig_ctx.traps)
        c1.traps[Clamped] = True
        c1.Emin = -383
        self.assertNotEqual(orig_ctx.Emin, -383)
        self.assertRaises(Clamped, c1.create_decimal, '0e-999')
        self.assertTrue(c1.flags[Clamped])
        with localcontext(new_ctx) as c2:
            self.assertEqual(c2.flags, new_ctx.flags)
            self.assertEqual(c2.traps, new_ctx.traps)
            self.assertRaises(Overflow, c2.power, Decimal('3.4e200'), 2)
            self.assertFalse(c2.flags[Clamped])
            self.assertTrue(c2.flags[Overflow])
            del c2
        self.assertFalse(c1.flags[Overflow])
        del c1
    self.assertNotEqual(orig_ctx.Emin, -383)
    self.assertFalse(orig_ctx.flags[Clamped])
    self.assertFalse(orig_ctx.flags[Overflow])
    self.assertFalse(new_ctx.flags[Clamped])
    self.assertFalse(new_ctx.flags[Overflow])
