# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: FormatTest_test_wide_char_separator_decimal_point

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    decimal_point = locale.localeconv()['decimal_point']
    thousands_sep = locale.localeconv()['thousands_sep']
    if decimal_point != '٫':
        self.skipTest('inappropriate decimal point separator ({!a} not {!a})'.format(decimal_point, '٫'))
    if thousands_sep != '٬':
        self.skipTest('inappropriate thousands separator ({!a} not {!a})'.format(thousands_sep, '٬'))
    self.assertEqual(format(Decimal('100000000.123'), 'n'), '100٬000٬000٫123')
