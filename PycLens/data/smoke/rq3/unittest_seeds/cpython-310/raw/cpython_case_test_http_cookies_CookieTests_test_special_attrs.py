# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: CookieTests_test_special_attrs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    C = cookies.SimpleCookie('Customer="WILE_E_COYOTE"')
    C['Customer']['expires'] = 0
    self.assertTrue(C.output().endswith('GMT'))
    C = cookies.SimpleCookie()
    C.load('Customer="W"; expires=Wed, 01 Jan 2010 00:00:00 GMT')
    self.assertEqual(C['Customer']['expires'], 'Wed, 01 Jan 2010 00:00:00 GMT')
    C = cookies.SimpleCookie()
    C.load('Customer="W"; expires=Wed, 01 Jan 98 00:00:00 GMT')
    self.assertEqual(C['Customer']['expires'], 'Wed, 01 Jan 98 00:00:00 GMT')
    C = cookies.SimpleCookie('Customer="WILE_E_COYOTE"')
    C['Customer']['max-age'] = 10
    self.assertEqual(C.output(), 'Set-Cookie: Customer="WILE_E_COYOTE"; Max-Age=10')
