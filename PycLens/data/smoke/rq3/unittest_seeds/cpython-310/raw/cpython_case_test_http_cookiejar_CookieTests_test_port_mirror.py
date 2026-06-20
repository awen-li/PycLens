# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_port_mirror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pol = DefaultCookiePolicy(rfc2965=True)
    c = CookieJar(pol)
    url = 'http://foo.bar.com/'
    interact_2965(c, url, 'spam=eggs; Version=1')
    h = interact_2965(c, url)
    self.assertNotIn('Port', h, 'absent port returned with port present')
    c = CookieJar(pol)
    url = 'http://foo.bar.com/'
    interact_2965(c, url, 'spam=eggs; Version=1; Port')
    h = interact_2965(c, url)
    self.assertRegex(h, '\\$Port([^=]|$)', 'port with no value not returned with no value')
    c = CookieJar(pol)
    url = 'http://foo.bar.com/'
    interact_2965(c, url, 'spam=eggs; Version=1; Port="80"')
    h = interact_2965(c, url)
    self.assertIn('$Port="80"', h, 'port with single value not returned with single value')
    c = CookieJar(pol)
    url = 'http://foo.bar.com/'
    interact_2965(c, url, 'spam=eggs; Version=1; Port="80,8080"')
    h = interact_2965(c, url)
    self.assertIn('$Port="80,8080"', h, 'port with multiple values not returned with multiple values')
