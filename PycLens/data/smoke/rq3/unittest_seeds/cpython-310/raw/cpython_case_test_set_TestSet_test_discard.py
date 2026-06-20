# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestSet_test_discard

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.s.discard('a')
    self.assertNotIn('a', self.s)
    self.s.discard('Q')
    self.assertRaises(TypeError, self.s.discard, [])
    s = self.thetype([frozenset(self.word)])
    self.assertIn(self.thetype(self.word), s)
    s.discard(self.thetype(self.word))
    self.assertNotIn(self.thetype(self.word), s)
    s.discard(self.thetype(self.word))
