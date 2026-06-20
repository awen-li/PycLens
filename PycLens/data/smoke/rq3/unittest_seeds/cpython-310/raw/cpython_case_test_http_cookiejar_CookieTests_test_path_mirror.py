# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_path_mirror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pol = DefaultCookiePolicy(rfc2965=True)
    c = CookieJar(pol)
    url = 'http://foo.bar.com/'
    interact_2965(c, url, 'spam=eggs; Version=1')
    h = interact_2965(c, url)
    self.assertNotIn('Path', h, 'absent path returned with path present')
    c = CookieJar(pol)
    url = 'http://foo.bar.com/'
    interact_2965(c, url, 'spam=eggs; Version=1; Path=/')
    h = interact_2965(c, url)
    self.assertIn('$Path="/"', h, 'path not returned')
