# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: LWPCookieTests_test_ietf_example_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = CookieJar(DefaultCookiePolicy(rfc2965=True))
    cookie = interact_2965(c, 'http://www.acme.com/acme/login', 'Customer="WILE_E_COYOTE"; Version="1"; Path="/acme"')
    self.assertFalse(cookie)
    cookie = interact_2965(c, 'http://www.acme.com/acme/pickitem', 'Part_Number="Rocket_Launcher_0001"; Version="1"; Path="/acme"')
    self.assertRegex(cookie, '^\\$Version="?1"?; Customer="?WILE_E_COYOTE"?; \\$Path="/acme"$')
    cookie = interact_2965(c, 'http://www.acme.com/acme/shipping', 'Shipping="FedEx"; Version="1"; Path="/acme"')
    self.assertRegex(cookie, '^\\$Version="?1"?;')
    self.assertRegex(cookie, 'Part_Number="?Rocket_Launcher_0001"?;\\s*\\$Path="\\/acme"')
    self.assertRegex(cookie, 'Customer="?WILE_E_COYOTE"?;\\s*\\$Path="\\/acme"')
    cookie = interact_2965(c, 'http://www.acme.com/acme/process')
    self.assertRegex(cookie, 'Shipping="?FedEx"?;\\s*\\$Path="\\/acme"')
    self.assertIn('WILE_E_COYOTE', cookie)
