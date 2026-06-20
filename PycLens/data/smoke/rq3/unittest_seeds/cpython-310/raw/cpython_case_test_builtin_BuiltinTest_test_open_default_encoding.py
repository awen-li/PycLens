# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_open_default_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    old_environ = dict(os.environ)
    try:
        for key in ('LC_ALL', 'LANG', 'LC_CTYPE'):
            if key in os.environ:
                del os.environ[key]
        self.write_testfile()
        current_locale_encoding = locale.getpreferredencoding(False)
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', EncodingWarning)
            fp = open(TESTFN, 'w')
        with fp:
            self.assertEqual(fp.encoding, current_locale_encoding)
    finally:
        os.environ.clear()
        os.environ.update(old_environ)
