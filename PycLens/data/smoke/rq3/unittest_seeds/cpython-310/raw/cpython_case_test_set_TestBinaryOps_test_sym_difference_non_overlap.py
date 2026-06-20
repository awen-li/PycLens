# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestBinaryOps_test_sym_difference_non_overlap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.set ^ set([8])
    self.assertEqual(result, set([2, 4, 6, 8]))
