# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: Coverage_test_quantize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    localcontext = self.decimal.localcontext
    InvalidOperation = self.decimal.InvalidOperation
    with localcontext() as c:
        c.prec = 1
        c.Emax = 1
        c.Emin = -1
        c.traps[InvalidOperation] = False
        x = Decimal(99).quantize(Decimal('1e1'))
        self.assertTrue(x.is_nan())
