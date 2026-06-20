# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: HamtTest_test_hamt_basics_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = hamt()
    self.assertEqual(len(h), 0)
    h2 = h.set('a', 'b')
    self.assertIsNot(h, h2)
    self.assertEqual(len(h), 0)
    self.assertEqual(len(h2), 1)
    self.assertIsNone(h.get('a'))
    self.assertEqual(h.get('a', 42), 42)
    self.assertEqual(h2.get('a'), 'b')
    h3 = h2.set('b', 10)
    self.assertIsNot(h2, h3)
    self.assertEqual(len(h), 0)
    self.assertEqual(len(h2), 1)
    self.assertEqual(len(h3), 2)
    self.assertEqual(h3.get('a'), 'b')
    self.assertEqual(h3.get('b'), 10)
    self.assertIsNone(h.get('b'))
    self.assertIsNone(h2.get('b'))
    self.assertIsNone(h.get('a'))
    self.assertEqual(h2.get('a'), 'b')
    h = h2 = h3 = None
