# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestUpdateOps_test_union_superset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.set |= set([2, 4, 6, 8])
    self.assertEqual(self.set, set([2, 4, 6, 8]))
