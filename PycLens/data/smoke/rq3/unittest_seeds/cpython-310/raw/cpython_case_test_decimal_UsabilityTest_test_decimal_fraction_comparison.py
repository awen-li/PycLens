# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: UsabilityTest_test_decimal_fraction_comparison

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    D = self.decimal.Decimal
    F = fractions[self.decimal].Fraction
    Context = self.decimal.Context
    localcontext = self.decimal.localcontext
    InvalidOperation = self.decimal.InvalidOperation
    emax = C.MAX_EMAX if C else 999999999
    emin = C.MIN_EMIN if C else -999999999
    etiny = C.MIN_ETINY if C else -1999999997
    c = Context(Emax=emax, Emin=emin)
    with localcontext(c):
        c.prec = emax
        self.assertLess(D(0), F(1, 9999999999999999999999999999999999999))
        self.assertLess(F(-1, 9999999999999999999999999999999999999), D(0))
        self.assertLess(F(0, 1), D('1e' + str(etiny)))
        self.assertLess(D('-1e' + str(etiny)), F(0, 1))
        self.assertLess(F(0, 9999999999999999999999999), D('1e' + str(etiny)))
        self.assertLess(D('-1e' + str(etiny)), F(0, 9999999999999999999999999))
        self.assertEqual(D('0.1'), F(1, 10))
        self.assertEqual(F(1, 10), D('0.1'))
        c.prec = 300
        self.assertNotEqual(D(1) / 3, F(1, 3))
        self.assertNotEqual(F(1, 3), D(1) / 3)
        self.assertLessEqual(F(120984237, 9999999999), D('9e' + str(emax)))
        self.assertGreaterEqual(D('9e' + str(emax)), F(120984237, 9999999999))
        self.assertGreater(D('inf'), F(99999999999, 123))
        self.assertGreater(D('inf'), F(-99999999999, 123))
        self.assertLess(D('-inf'), F(99999999999, 123))
        self.assertLess(D('-inf'), F(-99999999999, 123))
        self.assertRaises(InvalidOperation, D('nan').__gt__, F(-9, 123))
        self.assertIs(NotImplemented, F(-9, 123).__lt__(D('nan')))
        self.assertNotEqual(D('nan'), F(-9, 123))
        self.assertNotEqual(F(-9, 123), D('nan'))
