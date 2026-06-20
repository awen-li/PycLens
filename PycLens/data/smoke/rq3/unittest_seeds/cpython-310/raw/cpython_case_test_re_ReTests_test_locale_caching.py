# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_locale_caching

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    oldlocale = locale.setlocale(locale.LC_CTYPE)
    self.addCleanup(locale.setlocale, locale.LC_CTYPE, oldlocale)
    for loc in ('en_US.iso88591', 'en_US.utf8'):
        try:
            locale.setlocale(locale.LC_CTYPE, loc)
        except locale.Error:
            self.skipTest('test needs %s locale' % loc)
    re.purge()
    self.check_en_US_iso88591()
    self.check_en_US_utf8()
    re.purge()
    self.check_en_US_utf8()
    self.check_en_US_iso88591()
