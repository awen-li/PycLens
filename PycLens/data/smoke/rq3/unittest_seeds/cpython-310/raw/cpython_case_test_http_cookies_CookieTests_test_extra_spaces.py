# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: CookieTests_test_extra_spaces

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    C = cookies.SimpleCookie()
    C.load('eggs  =  scrambled  ;  secure  ;  path  =  bar   ; foo=foo   ')
    self.assertEqual(C.output(), 'Set-Cookie: eggs=scrambled; Path=bar; Secure\r\nSet-Cookie: foo=foo')
