# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CWhitebox_test_sizeof

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = C.Decimal
    HAVE_CONFIG_64 = C.MAX_PREC > 425000000
    self.assertGreater(Decimal(0).__sizeof__(), 0)
    if HAVE_CONFIG_64:
        x = Decimal(10 ** (19 * 24)).__sizeof__()
        y = Decimal(10 ** (19 * 25)).__sizeof__()
        self.assertEqual(y, x + 8)
    else:
        x = Decimal(10 ** (9 * 24)).__sizeof__()
        y = Decimal(10 ** (9 * 25)).__sizeof__()
        self.assertEqual(y, x + 4)
