# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodecsModuleTest_test_lookup_issue1813

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    oldlocale = locale.setlocale(locale.LC_CTYPE)
    self.addCleanup(locale.setlocale, locale.LC_CTYPE, oldlocale)
    try:
        locale.setlocale(locale.LC_CTYPE, 'tr_TR')
    except locale.Error:
        self.skipTest('test needs Turkish locale')
    c = codecs.lookup('ASCII')
    self.assertEqual(c.name, 'ascii')
