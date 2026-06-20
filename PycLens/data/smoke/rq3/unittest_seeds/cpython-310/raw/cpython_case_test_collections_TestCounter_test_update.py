# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCounter_test_update

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = Counter()
    c.update(self=42)
    self.assertEqual(list(c.items()), [('self', 42)])
    c = Counter()
    c.update(iterable=42)
    self.assertEqual(list(c.items()), [('iterable', 42)])
    c = Counter()
    c.update(iterable=None)
    self.assertEqual(list(c.items()), [('iterable', None)])
    self.assertRaises(TypeError, Counter().update, 42)
    self.assertRaises(TypeError, Counter().update, {}, {})
    self.assertRaises(TypeError, Counter.update)
