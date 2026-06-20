# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: Coverage_test_divmod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    localcontext = self.decimal.localcontext
    InvalidOperation = self.decimal.InvalidOperation
    DivisionByZero = self.decimal.DivisionByZero
    with localcontext() as c:
        (q, r) = divmod(Decimal('10912837129'), 1001)
        self.assertEqual(q, Decimal('10901935'))
        self.assertEqual(r, Decimal('194'))
        (q, r) = divmod(Decimal('NaN'), 7)
        self.assertTrue(q.is_nan() and r.is_nan())
        c.traps[InvalidOperation] = False
        (q, r) = divmod(Decimal('NaN'), 7)
        self.assertTrue(q.is_nan() and r.is_nan())
        c.traps[InvalidOperation] = False
        c.clear_flags()
        (q, r) = divmod(Decimal('inf'), Decimal('inf'))
        self.assertTrue(q.is_nan() and r.is_nan())
        self.assertTrue(c.flags[InvalidOperation])
        c.clear_flags()
        (q, r) = divmod(Decimal('inf'), 101)
        self.assertTrue(q.is_infinite() and r.is_nan())
        self.assertTrue(c.flags[InvalidOperation])
        c.clear_flags()
        (q, r) = divmod(Decimal(0), 0)
        self.assertTrue(q.is_nan() and r.is_nan())
        self.assertTrue(c.flags[InvalidOperation])
        c.traps[DivisionByZero] = False
        c.clear_flags()
        (q, r) = divmod(Decimal(11), 0)
        self.assertTrue(q.is_infinite() and r.is_nan())
        self.assertTrue(c.flags[InvalidOperation] and c.flags[DivisionByZero])
