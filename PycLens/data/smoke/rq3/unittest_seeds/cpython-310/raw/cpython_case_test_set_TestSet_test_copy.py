# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestSet_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dup = self.s.copy()
    self.assertEqual(self.s, dup)
    self.assertNotEqual(id(self.s), id(dup))
    self.assertEqual(type(dup), self.basetype)
