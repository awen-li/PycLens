# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_sub_and_super

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(self.ab_weakset <= self.abcde_weakset)
    self.assertTrue(self.abcde_weakset <= self.abcde_weakset)
    self.assertTrue(self.abcde_weakset >= self.ab_weakset)
    self.assertFalse(self.abcde_weakset <= self.def_weakset)
    self.assertFalse(self.abcde_weakset >= self.def_weakset)
    self.assertTrue(set('a').issubset('abc'))
    self.assertTrue(set('abc').issuperset('a'))
    self.assertFalse(set('a').issubset('cbs'))
    self.assertFalse(set('cbs').issuperset('a'))
