# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: CookieTests_test_set_secure_httponly_attrs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    C = cookies.SimpleCookie('Customer="WILE_E_COYOTE"')
    C['Customer']['secure'] = True
    C['Customer']['httponly'] = True
    self.assertEqual(C.output(), 'Set-Cookie: Customer="WILE_E_COYOTE"; HttpOnly; Secure')
