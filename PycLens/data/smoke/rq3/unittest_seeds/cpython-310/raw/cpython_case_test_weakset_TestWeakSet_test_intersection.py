# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_intersection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = WeakSet(self.letters)
    i = s.intersection(self.items2)
    for c in self.letters:
        self.assertEqual(c in i, c in self.items2 and c in self.letters)
    self.assertEqual(s, WeakSet(self.letters))
    self.assertEqual(type(i), WeakSet)
    for C in (set, frozenset, dict.fromkeys, list, tuple):
        x = WeakSet([])
        self.assertEqual(i.intersection(C(self.items)), x)
    self.assertEqual(len(i), len(self.items2))
    self.items2.pop()
    gc.collect()
    self.assertEqual(len(i), len(self.items2))
