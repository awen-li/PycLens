# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CWhitebox_test_exact_conversion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = C.Decimal
    localcontext = C.localcontext
    InvalidOperation = C.InvalidOperation
    with localcontext() as c:
        c.traps[InvalidOperation] = True
        x = '0e%d' % sys.maxsize
        self.assertRaises(InvalidOperation, Decimal, x)
        x = '0e%d' % (-sys.maxsize - 1)
        self.assertRaises(InvalidOperation, Decimal, x)
        x = '1e%d' % sys.maxsize
        self.assertRaises(InvalidOperation, Decimal, x)
        x = '1e%d' % (-sys.maxsize - 1)
        self.assertRaises(InvalidOperation, Decimal, x)
