# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: Coverage_test_power

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    localcontext = self.decimal.localcontext
    Overflow = self.decimal.Overflow
    Rounded = self.decimal.Rounded
    with localcontext() as c:
        c.prec = 3
        c.clear_flags()
        self.assertEqual(Decimal('1.0') ** 100, Decimal('1.00'))
        self.assertTrue(c.flags[Rounded])
        c.prec = 1
        c.Emax = 1
        c.Emin = -1
        c.clear_flags()
        c.traps[Overflow] = False
        self.assertEqual(Decimal(10000) ** Decimal('0.5'), Decimal('inf'))
        self.assertTrue(c.flags[Overflow])
