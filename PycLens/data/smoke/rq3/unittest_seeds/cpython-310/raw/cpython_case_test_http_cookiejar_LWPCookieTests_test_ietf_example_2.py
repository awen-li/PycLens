# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: LWPCookieTests_test_ietf_example_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = CookieJar(DefaultCookiePolicy(rfc2965=True))
    interact_2965(c, 'http://www.acme.com/acme/ammo/specific', 'Part_Number="Rocket_Launcher_0001"; Version="1"; Path="/acme"', 'Part_Number="Riding_Rocket_0023"; Version="1"; Path="/acme/ammo"')
    cookie = interact_2965(c, 'http://www.acme.com/acme/ammo/...')
    self.assertRegex(cookie, 'Riding_Rocket_0023.*Rocket_Launcher_0001')
    cookie = interact_2965(c, 'http://www.acme.com/acme/parts/')
    self.assertIn('Rocket_Launcher_0001', cookie)
    self.assertNotIn('Riding_Rocket_0023', cookie)
