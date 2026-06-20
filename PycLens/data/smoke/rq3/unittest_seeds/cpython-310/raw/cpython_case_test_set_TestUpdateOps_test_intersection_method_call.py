# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestUpdateOps_test_intersection_method_call

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.set.intersection_update(set([3, 4, 5]))
    self.assertEqual(self.set, set([4]))
