# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: CookieTests_test_secure_httponly_false_if_not_present

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    C = cookies.SimpleCookie()
    C.load('eggs=scrambled; Path=/bacon')
    self.assertFalse(C['eggs']['httponly'])
    self.assertFalse(C['eggs']['secure'])
