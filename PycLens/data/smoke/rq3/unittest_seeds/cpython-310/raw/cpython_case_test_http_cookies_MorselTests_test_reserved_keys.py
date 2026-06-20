# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: MorselTests_test_reserved_keys

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    M = cookies.Morsel()
    for i in M._reserved:
        self.assertTrue(M.isReservedKey(i))
        M[i] = '%s_value' % i
    for i in M._reserved:
        self.assertEqual(M[i], '%s_value' % i)
    for i in 'the holy hand grenade'.split():
        self.assertRaises(cookies.CookieError, M.__setitem__, i, '%s_value' % i)
