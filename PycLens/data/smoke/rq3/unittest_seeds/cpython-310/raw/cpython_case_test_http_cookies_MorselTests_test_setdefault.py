# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: MorselTests_test_setdefault

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    morsel = cookies.Morsel()
    morsel.update({'domain': 'example.com', 'version': 2})
    self.assertEqual(morsel.setdefault('expires', 'value'), '')
    self.assertEqual(morsel['expires'], '')
    self.assertEqual(morsel.setdefault('Version', 1), 2)
    self.assertEqual(morsel['version'], 2)
    self.assertEqual(morsel.setdefault('DOMAIN', 'value'), 'example.com')
    self.assertEqual(morsel['domain'], 'example.com')
    with self.assertRaises(cookies.CookieError):
        morsel.setdefault('invalid', 'value')
    self.assertNotIn('invalid', morsel)
