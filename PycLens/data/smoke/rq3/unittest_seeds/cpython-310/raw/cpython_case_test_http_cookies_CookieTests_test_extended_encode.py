# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: CookieTests_test_extended_encode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    C = cookies.SimpleCookie()
    C['val'] = 'some,funky;stuff'
    self.assertEqual(C.output(['val']), 'Set-Cookie: val="some\\054funky\\073stuff"')
