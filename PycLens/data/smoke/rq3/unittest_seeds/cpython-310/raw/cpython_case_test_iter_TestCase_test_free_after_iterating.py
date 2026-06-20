# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_free_after_iterating

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    check_free_after_iterating(self, iter, SequenceClass, (0,))
