# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_default_path_with_query

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cj = CookieJar()
    uri = 'http://example.com/?spam/eggs'
    value = 'eggs="bar"'
    interact_netscape(cj, uri, value)
    self.assertIn('/', cj._cookies['example.com'])
    self.assertEqual(interact_netscape(cj, uri), value)
