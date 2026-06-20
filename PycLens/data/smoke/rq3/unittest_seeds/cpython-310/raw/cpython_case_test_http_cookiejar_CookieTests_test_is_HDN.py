# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_is_HDN

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(is_HDN('foo.bar.com'))
    self.assertTrue(is_HDN('1foo2.3bar4.5com'))
    self.assertFalse(is_HDN('192.168.1.1'))
    self.assertFalse(is_HDN(''))
    self.assertFalse(is_HDN('.'))
    self.assertFalse(is_HDN('.foo.bar.com'))
    self.assertFalse(is_HDN('..foo'))
    self.assertFalse(is_HDN('foo.'))
