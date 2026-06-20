# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_utf8_mode.py
# case: UTF8ModeTests_test_posix_locale

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import sys; print(sys.flags.utf8_mode)'
    for loc in POSIX_LOCALES:
        with self.subTest(LC_ALL=loc):
            out = self.get_output('-c', code, LC_ALL=loc)
            self.assertEqual(out, '1')
