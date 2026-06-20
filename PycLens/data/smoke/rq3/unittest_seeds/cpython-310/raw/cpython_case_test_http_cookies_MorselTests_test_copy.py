# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: MorselTests_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    morsel_a = cookies.Morsel()
    morsel_a.set('foo', 'bar', 'baz')
    morsel_a.update({'version': 2, 'comment': 'foo'})
    morsel_b = morsel_a.copy()
    self.assertIsInstance(morsel_b, cookies.Morsel)
    self.assertIsNot(morsel_a, morsel_b)
    self.assertEqual(morsel_a, morsel_b)
    morsel_b = copy.copy(morsel_a)
    self.assertIsInstance(morsel_b, cookies.Morsel)
    self.assertIsNot(morsel_a, morsel_b)
    self.assertEqual(morsel_a, morsel_b)
