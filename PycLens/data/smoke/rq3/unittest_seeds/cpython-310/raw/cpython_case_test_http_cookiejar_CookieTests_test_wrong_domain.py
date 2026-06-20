# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: CookieTests_test_wrong_domain

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = CookieJar()
    interact_2965(c, 'http://www.nasty.com/', 'foo=bar; domain=friendly.org; Version="1"')
    self.assertEqual(len(c), 0)
