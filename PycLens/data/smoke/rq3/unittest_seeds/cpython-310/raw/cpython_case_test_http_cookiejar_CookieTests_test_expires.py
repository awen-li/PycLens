# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_expires

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = CookieJar()
    future = time2netscape(time.time() + 3600)
    with warnings_helper.check_no_warnings(self):
        headers = [f'Set-Cookie: FOO=BAR; path=/; expires={future}']
        req = urllib.request.Request('http://www.coyote.com/')
        res = FakeResponse(headers, 'http://www.coyote.com/')
        cookies = c.make_cookies(res, req)
        self.assertEqual(len(cookies), 1)
        self.assertEqual(time2netscape(cookies[0].expires), future)
    interact_netscape(c, 'http://www.acme.com/', 'spam="bar"; expires=%s' % future)
    self.assertEqual(len(c), 1)
    now = time2netscape(time.time() - 1)
    interact_netscape(c, 'http://www.acme.com/', 'foo="eggs"; expires=%s' % now)
    h = interact_netscape(c, 'http://www.acme.com/')
    self.assertEqual(len(c), 1)
    self.assertIn('spam="bar"', h)
    self.assertNotIn('foo', h)
    interact_netscape(c, 'http://www.acme.com/', 'eggs="bar"; expires=%s' % future)
    interact_netscape(c, 'http://www.acme.com/', 'bar="bar"; expires=%s' % future)
    self.assertEqual(len(c), 3)
    interact_netscape(c, 'http://www.acme.com/', 'eggs="bar"; expires=%s; max-age=0' % future)
    interact_netscape(c, 'http://www.acme.com/', 'bar="bar"; max-age=0; expires=%s' % future)
    h = interact_netscape(c, 'http://www.acme.com/')
    self.assertEqual(len(c), 1)
    interact_netscape(c, 'http://www.rhubarb.net/', 'whum="fizz"')
    self.assertEqual(len(c), 2)
    c.clear_session_cookies()
    self.assertEqual(len(c), 1)
    self.assertIn('spam="bar"', h)
    cookie = Cookie(0, 'name', 'value', None, False, 'www.python.org', True, False, '/', False, False, '1444312383.018307', False, None, None, {})
    self.assertEqual(cookie.expires, 1444312383)
