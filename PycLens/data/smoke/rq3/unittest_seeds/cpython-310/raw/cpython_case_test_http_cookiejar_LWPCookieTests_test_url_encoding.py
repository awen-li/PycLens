# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: LWPCookieTests_test_url_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = CookieJar(DefaultCookiePolicy(rfc2965=True))
    interact_2965(c, 'http://www.acme.com/foo%2f%25/%3c%3c%0Anew%C3%A5/%C3%A5', 'foo  =   bar; version    =   1')
    cookie = interact_2965(c, 'http://www.acme.com/foo%2f%25/<<%0anewå/æøå', 'bar=baz; path="/foo/"; version=1')
    version_re = re.compile('^\\$version=\\"?1\\"?', re.I)
    self.assertIn('foo=bar', cookie)
    self.assertRegex(cookie, version_re)
    cookie = interact_2965(c, 'http://www.acme.com/foo/%25/<<%0anewå/æøå')
    self.assertFalse(cookie)
    cookie = interact_2965(c, 'http://www.acme.com/ü')
