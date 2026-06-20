# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CWhitebox_test_c_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = C.Decimal
    HAVE_CONFIG_64 = C.MAX_PREC > 425000000
    self.assertRaises(TypeError, Decimal(1).__format__, '=10.10', [], 9)
    self.assertRaises(TypeError, Decimal(1).__format__, '=10.10', 9)
    self.assertRaises(TypeError, Decimal(1).__format__, [])
    self.assertRaises(ValueError, Decimal(1).__format__, '<>=10.10')
    maxsize = 2 ** 63 - 1 if HAVE_CONFIG_64 else 2 ** 31 - 1
    self.assertRaises(ValueError, Decimal('1.23456789').__format__, '=%d.1' % maxsize)
