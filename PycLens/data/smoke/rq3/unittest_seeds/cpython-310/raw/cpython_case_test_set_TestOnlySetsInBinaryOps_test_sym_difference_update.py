# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestOnlySetsInBinaryOps_test_sym_difference_update

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if self.otherIsIterable:
        self.set.symmetric_difference_update(self.other)
    else:
        self.assertRaises(TypeError, self.set.symmetric_difference_update, self.other)
