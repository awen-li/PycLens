# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: MorselTests_test_setitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    morsel = cookies.Morsel()
    morsel['expires'] = 0
    self.assertEqual(morsel['expires'], 0)
    morsel['Version'] = 2
    self.assertEqual(morsel['version'], 2)
    morsel['DOMAIN'] = 'example.com'
    self.assertEqual(morsel['domain'], 'example.com')
    with self.assertRaises(cookies.CookieError):
        morsel['invalid'] = 'value'
    self.assertNotIn('invalid', morsel)
