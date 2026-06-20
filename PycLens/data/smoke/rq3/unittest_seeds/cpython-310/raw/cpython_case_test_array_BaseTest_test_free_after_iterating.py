# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_free_after_iterating

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    support.check_free_after_iterating(self, iter, array.array, (self.typecode,))
    support.check_free_after_iterating(self, reversed, array.array, (self.typecode,))
