# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_default_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    old_environ = dict(os.environ)
    try:
        for key in ('LC_ALL', 'LANG', 'LC_CTYPE'):
            if key in os.environ:
                del os.environ[key]
        current_locale_encoding = locale.getpreferredencoding(False)
        b = self.BytesIO()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', EncodingWarning)
            t = self.TextIOWrapper(b)
        self.assertEqual(t.encoding, current_locale_encoding)
    finally:
        os.environ.clear()
        os.environ.update(old_environ)
