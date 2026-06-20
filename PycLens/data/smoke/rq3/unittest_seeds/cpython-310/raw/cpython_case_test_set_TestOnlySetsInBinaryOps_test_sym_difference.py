# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestOnlySetsInBinaryOps_test_sym_difference

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, lambda : self.set ^ self.other)
    self.assertRaises(TypeError, lambda : self.other ^ self.set)
    if self.otherIsIterable:
        self.set.symmetric_difference(self.other)
    else:
        self.assertRaises(TypeError, self.set.symmetric_difference, self.other)
