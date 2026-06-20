# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_or

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    i = self.s.union(self.items2)
    self.assertEqual(self.s | set(self.items2), i)
    self.assertEqual(self.s | frozenset(self.items2), i)
