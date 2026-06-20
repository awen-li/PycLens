# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestUpdateOps_test_union_overlap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.set |= set([3, 4, 5])
    self.assertEqual(self.set, set([2, 3, 4, 5, 6]))
