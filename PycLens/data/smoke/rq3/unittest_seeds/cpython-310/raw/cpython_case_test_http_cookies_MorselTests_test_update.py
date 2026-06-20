# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: MorselTests_test_update

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    attribs = {'expires': 1, 'Version': 2, 'DOMAIN': 'example.com'}
    morsel = cookies.Morsel()
    morsel.update(attribs)
    self.assertEqual(morsel['expires'], 1)
    self.assertEqual(morsel['version'], 2)
    self.assertEqual(morsel['domain'], 'example.com')
    morsel = cookies.Morsel()
    morsel.update(list(attribs.items()))
    self.assertEqual(morsel['expires'], 1)
    self.assertEqual(morsel['version'], 2)
    self.assertEqual(morsel['domain'], 'example.com')
    morsel = cookies.Morsel()
    morsel.update(((k, v) for (k, v) in attribs.items()))
    self.assertEqual(morsel['expires'], 1)
    self.assertEqual(morsel['version'], 2)
    self.assertEqual(morsel['domain'], 'example.com')
    with self.assertRaises(cookies.CookieError):
        morsel.update({'invalid': 'value'})
    self.assertNotIn('invalid', morsel)
    self.assertRaises(TypeError, morsel.update)
    self.assertRaises(TypeError, morsel.update, 0)
