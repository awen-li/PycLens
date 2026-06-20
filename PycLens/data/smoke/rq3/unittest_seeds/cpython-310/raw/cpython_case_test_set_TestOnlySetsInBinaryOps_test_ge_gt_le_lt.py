# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestOnlySetsInBinaryOps_test_ge_gt_le_lt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, lambda : self.set < self.other)
    self.assertRaises(TypeError, lambda : self.set <= self.other)
    self.assertRaises(TypeError, lambda : self.set > self.other)
    self.assertRaises(TypeError, lambda : self.set >= self.other)
    self.assertRaises(TypeError, lambda : self.other < self.set)
    self.assertRaises(TypeError, lambda : self.other <= self.set)
    self.assertRaises(TypeError, lambda : self.other > self.set)
    self.assertRaises(TypeError, lambda : self.other >= self.set)
