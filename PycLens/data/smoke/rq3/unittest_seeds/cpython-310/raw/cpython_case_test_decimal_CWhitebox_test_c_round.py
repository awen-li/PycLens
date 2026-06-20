# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CWhitebox_test_c_round

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = C.Decimal
    InvalidOperation = C.InvalidOperation
    localcontext = C.localcontext
    MAX_EMAX = C.MAX_EMAX
    MIN_ETINY = C.MIN_ETINY
    int_max = 2 ** 63 - 1 if C.MAX_PREC > 425000000 else 2 ** 31 - 1
    with localcontext() as c:
        c.traps[InvalidOperation] = True
        self.assertRaises(InvalidOperation, Decimal('1.23').__round__, -int_max - 1)
        self.assertRaises(InvalidOperation, Decimal('1.23').__round__, int_max)
        self.assertRaises(InvalidOperation, Decimal('1').__round__, int(MAX_EMAX + 1))
        self.assertRaises(C.InvalidOperation, Decimal('1').__round__, -int(MIN_ETINY - 1))
        self.assertRaises(OverflowError, Decimal('1.23').__round__, -int_max - 2)
        self.assertRaises(OverflowError, Decimal('1.23').__round__, int_max + 1)
