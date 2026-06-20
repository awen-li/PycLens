# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: CookieTests_test_samesite_attrs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    samesite_values = ['Strict', 'Lax', 'strict', 'lax']
    for val in samesite_values:
        with self.subTest(val=val):
            C = cookies.SimpleCookie('Customer="WILE_E_COYOTE"')
            C['Customer']['samesite'] = val
            self.assertEqual(C.output(), 'Set-Cookie: Customer="WILE_E_COYOTE"; SameSite=%s' % val)
            C = cookies.SimpleCookie()
            C.load('Customer="WILL_E_COYOTE"; SameSite=%s' % val)
            self.assertEqual(C['Customer']['samesite'], val)
