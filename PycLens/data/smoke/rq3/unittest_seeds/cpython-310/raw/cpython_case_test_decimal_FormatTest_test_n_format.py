# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: FormatTest_test_n_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = self.decimal.Decimal
    try:
        from locale import CHAR_MAX
    except ImportError:
        self.skipTest('locale.CHAR_MAX not available')

    def make_grouping(lst):
        return ''.join([chr(x) for x in lst]) if self.decimal == C else lst

    def get_fmt(x, override=None, fmt='n'):
        if self.decimal == C:
            return Decimal(x).__format__(fmt, override)
        else:
            return Decimal(x).__format__(fmt, _localeconv=override)
    en_US = {'decimal_point': '.', 'grouping': make_grouping([3, 3, 0]), 'thousands_sep': ','}
    fr_FR = {'decimal_point': ',', 'grouping': make_grouping([CHAR_MAX]), 'thousands_sep': ''}
    ru_RU = {'decimal_point': ',', 'grouping': make_grouping([3, 3, 0]), 'thousands_sep': ' '}
    crazy = {'decimal_point': '&', 'grouping': make_grouping([1, 4, 2, CHAR_MAX]), 'thousands_sep': '-'}
    dotsep_wide = {'decimal_point': b'\xc2\xbf'.decode('utf-8'), 'grouping': make_grouping([3, 3, 0]), 'thousands_sep': b'\xc2\xb4'.decode('utf-8')}
    self.assertEqual(get_fmt(Decimal('12.7'), en_US), '12.7')
    self.assertEqual(get_fmt(Decimal('12.7'), fr_FR), '12,7')
    self.assertEqual(get_fmt(Decimal('12.7'), ru_RU), '12,7')
    self.assertEqual(get_fmt(Decimal('12.7'), crazy), '1-2&7')
    self.assertEqual(get_fmt(123456789, en_US), '123,456,789')
    self.assertEqual(get_fmt(123456789, fr_FR), '123456789')
    self.assertEqual(get_fmt(123456789, ru_RU), '123 456 789')
    self.assertEqual(get_fmt(1234567890123, crazy), '123456-78-9012-3')
    self.assertEqual(get_fmt(123456789, en_US, '.6n'), '1.23457e+8')
    self.assertEqual(get_fmt(123456789, fr_FR, '.6n'), '1,23457e+8')
    self.assertEqual(get_fmt(123456789, ru_RU, '.6n'), '1,23457e+8')
    self.assertEqual(get_fmt(123456789, crazy, '.6n'), '1&23457e+8')
    self.assertEqual(get_fmt(1234, fr_FR, '03n'), '1234')
    self.assertEqual(get_fmt(1234, fr_FR, '04n'), '1234')
    self.assertEqual(get_fmt(1234, fr_FR, '05n'), '01234')
    self.assertEqual(get_fmt(1234, fr_FR, '06n'), '001234')
    self.assertEqual(get_fmt(12345, en_US, '05n'), '12,345')
    self.assertEqual(get_fmt(12345, en_US, '06n'), '12,345')
    self.assertEqual(get_fmt(12345, en_US, '07n'), '012,345')
    self.assertEqual(get_fmt(12345, en_US, '08n'), '0,012,345')
    self.assertEqual(get_fmt(12345, en_US, '09n'), '0,012,345')
    self.assertEqual(get_fmt(12345, en_US, '010n'), '00,012,345')
    self.assertEqual(get_fmt(123456, crazy, '06n'), '1-2345-6')
    self.assertEqual(get_fmt(123456, crazy, '07n'), '1-2345-6')
    self.assertEqual(get_fmt(123456, crazy, '08n'), '1-2345-6')
    self.assertEqual(get_fmt(123456, crazy, '09n'), '01-2345-6')
    self.assertEqual(get_fmt(123456, crazy, '010n'), '0-01-2345-6')
    self.assertEqual(get_fmt(123456, crazy, '011n'), '0-01-2345-6')
    self.assertEqual(get_fmt(123456, crazy, '012n'), '00-01-2345-6')
    self.assertEqual(get_fmt(123456, crazy, '013n'), '000-01-2345-6')
    self.assertEqual(get_fmt(Decimal('-1.5'), dotsep_wide, '020n'), '-0´000´000´000´001¿5')
