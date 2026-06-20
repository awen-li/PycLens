# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_gt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(self.abcde_weakset > self.ab_weakset)
    self.assertFalse(self.abcde_weakset > self.def_weakset)
    self.assertFalse(self.ab_weakset > self.ab_weakset)
    self.assertFalse(WeakSet() > WeakSet())
