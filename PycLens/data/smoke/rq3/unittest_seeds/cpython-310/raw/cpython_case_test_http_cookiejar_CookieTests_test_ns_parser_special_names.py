# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_ns_parser_special_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = CookieJar()
    interact_netscape(c, 'http://www.acme.com/', 'expires=eggs')
    interact_netscape(c, 'http://www.acme.com/', 'version=eggs; spam=eggs')
    cookies = c._cookies['www.acme.com']['/']
    self.assertIn('expires', cookies)
    self.assertIn('version', cookies)
