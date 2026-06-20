# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: CookieTests_test_illegal_chars

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rawdata = 'a=b; c,d=e'
    C = cookies.SimpleCookie()
    with self.assertRaises(cookies.CookieError):
        C.load(rawdata)
