# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_two_component_domain_rfc2965

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pol = DefaultCookiePolicy(rfc2965=True)
    c = CookieJar(pol)
    interact_2965(c, 'http://foo.net/', 'foo=bar; Version="1"')
    self.assertEqual(len(c), 1)
    self.assertEqual(c._cookies['foo.net']['/']['foo'].value, 'bar')
    self.assertEqual(interact_2965(c, 'http://foo.net/'), '$Version=1; foo=bar')
    self.assertEqual(interact_2965(c, 'http://www.foo.net/'), '')
    interact_2965(c, 'http://foo.net/foo', 'spam=eggs; domain=foo.net; path=/foo; Version="1"')
    self.assertEqual(len(c), 1)
    self.assertEqual(interact_2965(c, 'http://foo.net/foo'), '$Version=1; foo=bar')
    interact_2965(c, 'http://www.foo.net/foo/', 'spam=eggs; domain=foo.net; Version="1"')
    self.assertEqual(c._cookies['.foo.net']['/foo/']['spam'].value, 'eggs')
    self.assertEqual(len(c), 2)
    self.assertEqual(interact_2965(c, 'http://foo.net/foo/'), '$Version=1; foo=bar')
    self.assertEqual(interact_2965(c, 'http://www.foo.net/foo/'), '$Version=1; spam=eggs; $Domain="foo.net"')
    interact_2965(c, 'http://foo.net/', 'ni="ni"; domain=".net"; Version="1"')
    self.assertEqual(len(c), 2)
    interact_2965(c, 'http://foo.co.uk/', 'nasty=trick; domain=.co.uk; Version="1"')
    self.assertEqual(len(c), 3)
