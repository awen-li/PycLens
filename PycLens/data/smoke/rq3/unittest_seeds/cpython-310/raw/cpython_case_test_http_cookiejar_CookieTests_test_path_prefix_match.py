# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_path_prefix_match

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pol = DefaultCookiePolicy()
    strict_ns_path_pol = DefaultCookiePolicy(strict_ns_set_path=True)
    c = CookieJar(pol)
    base_url = 'http://bar.com'
    interact_netscape(c, base_url, 'spam=eggs; Path=/foo')
    cookie = c._cookies['bar.com']['/foo']['spam']
    for (path, ok) in [('/foo', True), ('/foo/', True), ('/foo/bar', True), ('/', False), ('/foobad/foo', False)]:
        url = f'{base_url}{path}'
        req = urllib.request.Request(url)
        h = interact_netscape(c, url)
        if ok:
            self.assertIn('spam=eggs', h, f'cookie not set for {path}')
            self.assertTrue(strict_ns_path_pol.set_ok_path(cookie, req))
        else:
            self.assertNotIn('spam=eggs', h, f'cookie set for {path}')
            self.assertFalse(strict_ns_path_pol.set_ok_path(cookie, req))
