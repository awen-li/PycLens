# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_two_component_domain_ns

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = CookieJar()
    interact_netscape(c, 'http://foo.net/', 'ns=bar')
    self.assertEqual(len(c), 1)
    self.assertEqual(c._cookies['foo.net']['/']['ns'].value, 'bar')
    self.assertEqual(interact_netscape(c, 'http://foo.net/'), 'ns=bar')
    self.assertEqual(interact_netscape(c, 'http://www.foo.net/'), 'ns=bar')
    pol = DefaultCookiePolicy(strict_ns_domain=DefaultCookiePolicy.DomainStrictNonDomain)
    c.set_policy(pol)
    self.assertEqual(interact_netscape(c, 'http://www.foo.net/'), '')
    interact_netscape(c, 'http://foo.net/foo/', 'spam1=eggs; domain=foo.net')
    interact_netscape(c, 'http://foo.net/foo/bar/', 'spam2=eggs; domain=.foo.net')
    self.assertEqual(len(c), 3)
    self.assertEqual(c._cookies['.foo.net']['/foo']['spam1'].value, 'eggs')
    self.assertEqual(c._cookies['.foo.net']['/foo/bar']['spam2'].value, 'eggs')
    self.assertEqual(interact_netscape(c, 'http://foo.net/foo/bar/'), 'spam2=eggs; spam1=eggs; ns=bar')
    interact_netscape(c, 'http://foo.net/', 'nini="ni"; domain=.net')
    self.assertEqual(len(c), 3)
    interact_netscape(c, 'http://foo.co.uk', 'nasty=trick; domain=.co.uk')
    self.assertEqual(len(c), 4)
