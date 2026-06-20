# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: TestMiscellaneous_test_getsetlocale_issue1813

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    oldlocale = locale.setlocale(locale.LC_CTYPE)
    self.addCleanup(locale.setlocale, locale.LC_CTYPE, oldlocale)
    try:
        locale.setlocale(locale.LC_CTYPE, 'tr_TR')
    except locale.Error:
        self.skipTest('test needs Turkish locale')
    loc = locale.getlocale(locale.LC_CTYPE)
    if verbose:
        print('testing with %a' % (loc,), end=' ', flush=True)
    try:
        locale.setlocale(locale.LC_CTYPE, loc)
    except locale.Error as exc:
        self.skipTest(f'setlocale(LC_CTYPE, {loc!r}) failed: {exc!r}')
    self.assertEqual(loc, locale.getlocale(locale.LC_CTYPE))
