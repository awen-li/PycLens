# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_difference

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    i = self.s.difference(self.items2)
    for c in self.letters:
        self.assertEqual(c in i, c in self.d and c not in self.items2)
    self.assertEqual(self.s, WeakSet(self.items))
    self.assertEqual(type(i), WeakSet)
    self.assertRaises(TypeError, self.s.difference, [[]])
