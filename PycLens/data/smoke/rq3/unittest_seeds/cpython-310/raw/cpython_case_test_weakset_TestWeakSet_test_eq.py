# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakset.py
# case: TestWeakSet_test_eq

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(self.s == self.s)
    self.assertTrue(self.s == WeakSet(self.items))
    self.assertFalse(self.s == set(self.items))
    self.assertFalse(self.s == list(self.items))
    self.assertFalse(self.s == tuple(self.items))
    self.assertFalse(self.s == WeakSet([Foo]))
    self.assertFalse(self.s == 1)
