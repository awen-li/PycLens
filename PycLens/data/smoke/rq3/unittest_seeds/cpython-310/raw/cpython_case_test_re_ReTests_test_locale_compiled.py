# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_locale_compiled

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
    locale.setlocale(locale.LC_CTYPE, 'en_US.iso88591')
    p1 = re.compile(b'\xc5\xe5', re.L | re.I)
    p2 = re.compile(b'[a\xc5][a\xe5]', re.L | re.I)
    p3 = re.compile(b'[az\xc5][az\xe5]', re.L | re.I)
    p4 = re.compile(b'[^\xc5][^\xe5]', re.L | re.I)
    for p in (p1, p2, p3):
        self.assertTrue(p.match(b'\xc5\xe5'))
        self.assertTrue(p.match(b'\xe5\xe5'))
        self.assertTrue(p.match(b'\xc5\xc5'))
    self.assertIsNone(p4.match(b'\xe5\xc5'))
    self.assertIsNone(p4.match(b'\xe5\xe5'))
    self.assertIsNone(p4.match(b'\xc5\xc5'))
    locale.setlocale(locale.LC_CTYPE, 'en_US.utf8')
    for p in (p1, p2, p3):
        self.assertTrue(p.match(b'\xc5\xe5'))
        self.assertIsNone(p.match(b'\xe5\xe5'))
        self.assertIsNone(p.match(b'\xc5\xc5'))
    self.assertTrue(p4.match(b'\xe5\xc5'))
    self.assertIsNone(p4.match(b'\xe5\xe5'))
    self.assertIsNone(p4.match(b'\xc5\xc5'))
