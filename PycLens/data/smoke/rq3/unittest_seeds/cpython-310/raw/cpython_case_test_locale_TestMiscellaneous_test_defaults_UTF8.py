# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: TestMiscellaneous_test_defaults_UTF8

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _locale
    import os
    self.assertEqual(locale._parse_localename('UTF-8'), (None, 'UTF-8'))
    if hasattr(_locale, '_getdefaultlocale'):
        orig_getlocale = _locale._getdefaultlocale
        del _locale._getdefaultlocale
    else:
        orig_getlocale = None
    orig_env = {}
    try:
        for key in ('LC_ALL', 'LC_CTYPE', 'LANG', 'LANGUAGE'):
            if key in os.environ:
                orig_env[key] = os.environ[key]
                del os.environ[key]
        os.environ['LC_CTYPE'] = 'UTF-8'
        self.assertEqual(locale.getdefaultlocale(), (None, 'UTF-8'))
    finally:
        for k in orig_env:
            os.environ[k] = orig_env[k]
        if 'LC_CTYPE' not in orig_env:
            del os.environ['LC_CTYPE']
        if orig_getlocale is not None:
            _locale._getdefaultlocale = orig_getlocale
