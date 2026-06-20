# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: LWPCookieTests_test_rejection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pol = DefaultCookiePolicy(rfc2965=True)
    c = LWPCookieJar(policy=pol)
    max_age = 'max-age=3600'
    cookie = interact_2965(c, 'http://www.acme.com', 'foo=bar; domain=".com"; version=1')
    self.assertFalse(c)
    cookie = interact_2965(c, 'http://www.acme.com', 'ping=pong; domain="acme.com"; version=1')
    self.assertEqual(len(c), 1)
    cookie = interact_2965(c, 'http://www.a.acme.com', 'whiz=bang; domain="acme.com"; version=1')
    self.assertEqual(len(c), 1)
    cookie = interact_2965(c, 'http://www.a.acme.com', 'wow=flutter; domain=".a.acme.com"; version=1')
    self.assertEqual(len(c), 2)
    cookie = interact_2965(c, 'http://125.125.125.125', 'zzzz=ping; domain="125.125.125"; version=1')
    self.assertEqual(len(c), 2)
    cookie = interact_2965(c, 'http://www.sol.no', 'blah=rhubarb; domain=".sol.no"; path="/foo"; version=1')
    self.assertEqual(len(c), 2)
    cookie = interact_2965(c, 'http://www.sol.no/foo/bar', 'bing=bong; domain=".sol.no"; path="/foo"; version=1')
    self.assertEqual(len(c), 3)
    cookie = interact_2965(c, 'http://www.sol.no', 'whiz=ffft; domain=".sol.no"; port="90,100"; version=1')
    self.assertEqual(len(c), 3)
    cookie = interact_2965(c, 'http://www.sol.no', 'bang=wallop; version=1; domain=".sol.no"; port="90,100, 80,8080"; max-age=100; Comment = "Just kidding! (\\"|\\\\\\\\) "')
    self.assertEqual(len(c), 4)
    cookie = interact_2965(c, 'http://www.sol.no', 'foo9=bar; version=1; domain=".sol.no"; port; max-age=100;')
    self.assertEqual(len(c), 5)
    cookie = interact_2965(c, 'http://www.sol.no/<oo/', 'foo8=bar; version=1; path="/%3coo"')
    self.assertEqual(len(c), 6)
    filename = os_helper.TESTFN
    try:
        c.save(filename, ignore_discard=True)
        old = repr(c)
        c = LWPCookieJar(policy=pol)
        c.load(filename, ignore_discard=True)
    finally:
        try:
            os.unlink(filename)
        except OSError:
            pass
    self.assertEqual(old, repr(c))
