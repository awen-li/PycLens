# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: CookieTests_test_secure_httponly_true_if_have_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    C = cookies.SimpleCookie()
    C.load('eggs=scrambled; httponly=foo; secure=bar; Path=/bacon')
    self.assertTrue(C['eggs']['httponly'])
    self.assertTrue(C['eggs']['secure'])
    self.assertEqual(C['eggs']['httponly'], 'foo')
    self.assertEqual(C['eggs']['secure'], 'bar')
