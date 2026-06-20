# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_utf8_mode.py
# case: UTF8ModeTests_test_locale_getpreferredencoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import locale; print(locale.getpreferredencoding(False), locale.getpreferredencoding(True))'
    out = self.get_output('-X', 'utf8', '-c', code)
    self.assertEqual(out, 'UTF-8 UTF-8')
    for loc in POSIX_LOCALES:
        with self.subTest(LC_ALL=loc):
            out = self.get_output('-X', 'utf8', '-c', code, LC_ALL=loc)
            self.assertEqual(out, 'UTF-8 UTF-8')
