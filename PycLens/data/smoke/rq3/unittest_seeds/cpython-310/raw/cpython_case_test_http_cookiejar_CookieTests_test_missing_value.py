# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_missing_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = os_helper.TESTFN
    c = MozillaCookieJar(filename)
    interact_netscape(c, 'http://www.acme.com/', 'eggs')
    interact_netscape(c, 'http://www.acme.com/', '"spam"; path=/foo/')
    cookie = c._cookies['www.acme.com']['/']['eggs']
    self.assertIsNone(cookie.value)
    self.assertEqual(cookie.name, 'eggs')
    cookie = c._cookies['www.acme.com']['/foo/']['"spam"']
    self.assertIsNone(cookie.value)
    self.assertEqual(cookie.name, '"spam"')
    self.assertEqual(lwp_cookie_str(cookie), '"spam"; path="/foo/"; domain="www.acme.com"; path_spec; discard; version=0')
    old_str = repr(c)
    c.save(ignore_expires=True, ignore_discard=True)
    try:
        c = MozillaCookieJar(filename)
        c.revert(ignore_expires=True, ignore_discard=True)
    finally:
        os.unlink(c.filename)
    self.assertEqual(repr(c), re.sub('path_specified=%s' % True, 'path_specified=%s' % False, old_str))
    self.assertEqual(interact_netscape(c, 'http://www.acme.com/foo/'), '"spam"; eggs')
