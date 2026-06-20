# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CommandLineTestCase_test_option_locale

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFailure('-L')
    self.assertFailure('--locale')
    self.assertFailure('-L', 'en')
    (lang, enc) = locale.getdefaultlocale()
    lang = lang or 'C'
    enc = enc or 'UTF-8'
    try:
        oldlocale = locale.getlocale(locale.LC_TIME)
        try:
            locale.setlocale(locale.LC_TIME, (lang, enc))
        finally:
            locale.setlocale(locale.LC_TIME, oldlocale)
    except (locale.Error, ValueError):
        self.skipTest('cannot set the system default locale')
    stdout = self.run_ok('--locale', lang, '--encoding', enc, '2004')
    self.assertIn('2004'.encode(enc), stdout)
