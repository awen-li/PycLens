# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestSet_test_inplace_on_self

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = self.s.copy()
    t |= t
    self.assertEqual(t, self.s)
    t &= t
    self.assertEqual(t, self.s)
    t -= t
    self.assertEqual(t, self.thetype())
    t = self.s.copy()
    t ^= t
    self.assertEqual(t, self.thetype())
