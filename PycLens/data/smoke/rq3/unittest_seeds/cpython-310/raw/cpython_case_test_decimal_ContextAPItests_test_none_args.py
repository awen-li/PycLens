# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextAPItests_test_none_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Context = self.decimal.Context
    InvalidOperation = self.decimal.InvalidOperation
    DivisionByZero = self.decimal.DivisionByZero
    Overflow = self.decimal.Overflow
    c1 = Context()
    c2 = Context(prec=None, rounding=None, Emax=None, Emin=None, capitals=None, clamp=None, flags=None, traps=None)
    for c in [c1, c2]:
        self.assertEqual(c.prec, 28)
        self.assertEqual(c.rounding, ROUND_HALF_EVEN)
        self.assertEqual(c.Emax, 999999)
        self.assertEqual(c.Emin, -999999)
        self.assertEqual(c.capitals, 1)
        self.assertEqual(c.clamp, 0)
        assert_signals(self, c, 'flags', [])
        assert_signals(self, c, 'traps', [InvalidOperation, DivisionByZero, Overflow])
