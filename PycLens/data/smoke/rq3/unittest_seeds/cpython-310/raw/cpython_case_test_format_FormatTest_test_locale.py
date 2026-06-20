# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_format.py
# case: FormatTest_test_locale

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        oldloc = locale.setlocale(locale.LC_ALL)
        locale.setlocale(locale.LC_ALL, '')
    except locale.Error as err:
        self.skipTest('Cannot set locale: {}'.format(err))
    try:
        localeconv = locale.localeconv()
        sep = localeconv['thousands_sep']
        point = localeconv['decimal_point']
        grouping = localeconv['grouping']
        text = format(123456789, 'n')
        if grouping:
            self.assertIn(sep, text)
        self.assertEqual(text.replace(sep, ''), '123456789')
        text = format(1234.5, 'n')
        if grouping:
            self.assertIn(sep, text)
        self.assertIn(point, text)
        self.assertEqual(text.replace(sep, ''), '1234' + point + '5')
    finally:
        locale.setlocale(locale.LC_ALL, oldloc)
