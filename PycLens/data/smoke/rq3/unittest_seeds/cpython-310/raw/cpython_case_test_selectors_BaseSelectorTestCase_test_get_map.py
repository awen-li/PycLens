# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_selectors.py
# case: BaseSelectorTestCase_test_get_map

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.SELECTOR()
    self.addCleanup(s.close)
    (rd, wr) = self.make_socketpair()
    keys = s.get_map()
    self.assertFalse(keys)
    self.assertEqual(len(keys), 0)
    self.assertEqual(list(keys), [])
    key = s.register(rd, selectors.EVENT_READ, 'data')
    self.assertIn(rd, keys)
    self.assertEqual(key, keys[rd])
    self.assertEqual(len(keys), 1)
    self.assertEqual(list(keys), [rd.fileno()])
    self.assertEqual(list(keys.values()), [key])
    with self.assertRaises(KeyError):
        keys[999999]
    with self.assertRaises(TypeError):
        del keys[rd]
