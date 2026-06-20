# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: MorselTests_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    morsel_a = cookies.Morsel()
    morsel_a.set('foo', 'bar', 'baz')
    morsel_a.update({'version': 2, 'comment': 'foo'})
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        with self.subTest(proto=proto):
            morsel_b = pickle.loads(pickle.dumps(morsel_a, proto))
            self.assertIsInstance(morsel_b, cookies.Morsel)
            self.assertEqual(morsel_b, morsel_a)
            self.assertEqual(str(morsel_b), str(morsel_a))
