# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: FileCookieJarTests_test_lwp_valueless_cookie

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = os_helper.TESTFN
    c = LWPCookieJar()
    interact_netscape(c, 'http://www.acme.com/', 'boo')
    self.assertEqual(c._cookies['www.acme.com']['/']['boo'].value, None)
    try:
        c.save(filename, ignore_discard=True)
        c = LWPCookieJar()
        c.load(filename, ignore_discard=True)
    finally:
        try:
            os.unlink(filename)
        except OSError:
            pass
    self.assertEqual(c._cookies['www.acme.com']['/']['boo'].value, None)
