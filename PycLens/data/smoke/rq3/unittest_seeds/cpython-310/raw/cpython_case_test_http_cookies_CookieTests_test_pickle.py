# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: CookieTests_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rawdata = 'Customer="WILE_E_COYOTE"; Path=/acme; Version=1'
    expected_output = 'Set-Cookie: %s' % rawdata
    C = cookies.SimpleCookie()
    C.load(rawdata)
    self.assertEqual(C.output(), expected_output)
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        with self.subTest(proto=proto):
            C1 = pickle.loads(pickle.dumps(C, protocol=proto))
            self.assertEqual(C1.output(), expected_output)
