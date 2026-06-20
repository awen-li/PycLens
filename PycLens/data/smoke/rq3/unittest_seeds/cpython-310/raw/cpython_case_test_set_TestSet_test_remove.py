# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestSet_test_remove

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.s.remove('a')
    self.assertNotIn('a', self.s)
    self.assertRaises(KeyError, self.s.remove, 'Q')
    self.assertRaises(TypeError, self.s.remove, [])
    s = self.thetype([frozenset(self.word)])
    self.assertIn(self.thetype(self.word), s)
    s.remove(self.thetype(self.word))
    self.assertNotIn(self.thetype(self.word), s)
    self.assertRaises(KeyError, self.s.remove, self.thetype(self.word))
