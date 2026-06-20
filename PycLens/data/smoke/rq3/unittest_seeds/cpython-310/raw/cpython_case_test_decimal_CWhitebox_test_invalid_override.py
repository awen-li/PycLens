# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CWhitebox_test_invalid_override

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = C.Decimal
    try:
        from locale import CHAR_MAX
    except ImportError:
        self.skipTest('locale.CHAR_MAX not available')

    def make_grouping(lst):
        return ''.join([chr(x) for x in lst])

    def get_fmt(x, override=None, fmt='n'):
        return Decimal(x).__format__(fmt, override)
    invalid_grouping = {'decimal_point': ',', 'grouping': make_grouping([255, 255, 0]), 'thousands_sep': ','}
    invalid_dot = {'decimal_point': 'xxxxx', 'grouping': make_grouping([3, 3, 0]), 'thousands_sep': ','}
    invalid_sep = {'decimal_point': '.', 'grouping': make_grouping([3, 3, 0]), 'thousands_sep': 'yyyyy'}
    if CHAR_MAX == 127:
        self.assertRaises(ValueError, get_fmt, 12345, invalid_grouping, 'g')
    self.assertRaises(ValueError, get_fmt, 12345, invalid_dot, 'g')
    self.assertRaises(ValueError, get_fmt, 12345, invalid_sep, 'g')
