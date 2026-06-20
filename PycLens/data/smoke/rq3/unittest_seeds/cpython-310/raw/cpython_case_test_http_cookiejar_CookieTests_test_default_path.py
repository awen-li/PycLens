# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_default_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pol = DefaultCookiePolicy(rfc2965=True)
    c = CookieJar(pol)
    interact_2965(c, 'http://www.acme.com/', 'spam="bar"; Version="1"')
    self.assertIn('/', c._cookies['www.acme.com'])
    c = CookieJar(pol)
    interact_2965(c, 'http://www.acme.com/blah', 'eggs="bar"; Version="1"')
    self.assertIn('/', c._cookies['www.acme.com'])
    c = CookieJar(pol)
    interact_2965(c, 'http://www.acme.com/blah/rhubarb', 'eggs="bar"; Version="1"')
    self.assertIn('/blah/', c._cookies['www.acme.com'])
    c = CookieJar(pol)
    interact_2965(c, 'http://www.acme.com/blah/rhubarb/', 'eggs="bar"; Version="1"')
    self.assertIn('/blah/rhubarb/', c._cookies['www.acme.com'])
    c = CookieJar()
    interact_netscape(c, 'http://www.acme.com/', 'spam="bar"')
    self.assertIn('/', c._cookies['www.acme.com'])
    c = CookieJar()
    interact_netscape(c, 'http://www.acme.com/blah', 'eggs="bar"')
    self.assertIn('/', c._cookies['www.acme.com'])
    c = CookieJar()
    interact_netscape(c, 'http://www.acme.com/blah/rhubarb', 'eggs="bar"')
    self.assertIn('/blah', c._cookies['www.acme.com'])
    c = CookieJar()
    interact_netscape(c, 'http://www.acme.com/blah/rhubarb/', 'eggs="bar"')
    self.assertIn('/blah/rhubarb', c._cookies['www.acme.com'])
