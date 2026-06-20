# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: FileCookieJarTests_test_constructor_with_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = os_helper.TESTFN
    c = LWPCookieJar(filename)
    self.assertEqual(c.filename, filename)
