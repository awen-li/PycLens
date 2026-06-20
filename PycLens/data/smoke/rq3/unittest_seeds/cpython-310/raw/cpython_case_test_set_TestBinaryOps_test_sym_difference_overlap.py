# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestBinaryOps_test_sym_difference_overlap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.set ^ set((3, 4, 5))
    self.assertEqual(result, set([2, 3, 5, 6]))
