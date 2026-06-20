# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_ns_parser

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = CookieJar()
    interact_netscape(c, 'http://www.acme.com/', 'spam=eggs; DoMain=.acme.com; port; blArgh="feep"')
    interact_netscape(c, 'http://www.acme.com/', 'ni=ni; port=80,8080')
    interact_netscape(c, 'http://www.acme.com:80/', 'nini=ni')
    interact_netscape(c, 'http://www.acme.com:80/', 'foo=bar; expires=')
    interact_netscape(c, 'http://www.acme.com:80/', 'spam=eggs; expires="Foo Bar 25 33:22:11 3022"')
    interact_netscape(c, 'http://www.acme.com/', 'fortytwo=')
    interact_netscape(c, 'http://www.acme.com/', '=unladenswallow')
    interact_netscape(c, 'http://www.acme.com/', 'holyhandgrenade')
    cookie = c._cookies['.acme.com']['/']['spam']
    self.assertEqual(cookie.domain, '.acme.com')
    self.assertTrue(cookie.domain_specified)
    self.assertEqual(cookie.port, DEFAULT_HTTP_PORT)
    self.assertFalse(cookie.port_specified)
    self.assertTrue(cookie.has_nonstandard_attr('blArgh'))
    self.assertFalse(cookie.has_nonstandard_attr('blargh'))
    cookie = c._cookies['www.acme.com']['/']['ni']
    self.assertEqual(cookie.domain, 'www.acme.com')
    self.assertFalse(cookie.domain_specified)
    self.assertEqual(cookie.port, '80,8080')
    self.assertTrue(cookie.port_specified)
    cookie = c._cookies['www.acme.com']['/']['nini']
    self.assertIsNone(cookie.port)
    self.assertFalse(cookie.port_specified)
    foo = c._cookies['www.acme.com']['/']['foo']
    spam = c._cookies['www.acme.com']['/']['foo']
    self.assertIsNone(foo.expires)
    self.assertIsNone(spam.expires)
    cookie = c._cookies['www.acme.com']['/']['fortytwo']
    self.assertIsNotNone(cookie.value)
    self.assertEqual(cookie.value, '')
    cookie = c._cookies['www.acme.com']['/']['holyhandgrenade']
    self.assertIsNone(cookie.value)
