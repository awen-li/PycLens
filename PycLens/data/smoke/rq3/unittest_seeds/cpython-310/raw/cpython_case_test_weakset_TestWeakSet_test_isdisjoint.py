# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_isdisjoint

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(self.s.isdisjoint(WeakSet(self.items2)))
    self.assertTrue(not self.s.isdisjoint(WeakSet(self.letters)))
