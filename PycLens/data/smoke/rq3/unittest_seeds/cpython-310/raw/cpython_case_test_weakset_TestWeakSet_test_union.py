# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_union

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    u = self.s.union(self.items2)
    for c in self.letters:
        self.assertEqual(c in u, c in self.d or c in self.items2)
    self.assertEqual(self.s, WeakSet(self.items))
    self.assertEqual(type(u), WeakSet)
    self.assertRaises(TypeError, self.s.union, [[]])
    for C in (set, frozenset, dict.fromkeys, list, tuple):
        x = WeakSet(self.items + self.items2)
        c = C(self.items2)
        self.assertEqual(self.s.union(c), x)
        del c
    self.assertEqual(len(u), len(self.items) + len(self.items2))
    self.items2.pop()
    gc.collect()
    self.assertEqual(len(u), len(self.items) + len(self.items2))
