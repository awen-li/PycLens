# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: FileCookieJarTests_test_bad_magic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = os_helper.TESTFN
    for cookiejar_class in (LWPCookieJar, MozillaCookieJar):
        c = cookiejar_class()
        try:
            c.load(filename='for this test to work, a file with this filename should not exist')
        except OSError as exc:
            self.assertIsNot(exc.__class__, LoadError)
        else:
            self.fail('expected OSError for invalid filename')
    try:
        with open(filename, 'w') as f:
            f.write('oops\n')
            for cookiejar_class in (LWPCookieJar, MozillaCookieJar):
                c = cookiejar_class()
                self.assertRaises(LoadError, c.load, filename)
    finally:
        try:
            os.unlink(filename)
        except OSError:
            pass
