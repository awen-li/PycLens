# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bisect.py
# case: TestBisect_test_negative_lo

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mod = self.module
    self.assertRaises(ValueError, mod.bisect_left, [1, 2, 3], 5, -1, 3)
    self.assertRaises(ValueError, mod.bisect_right, [1, 2, 3], 5, -1, 3)
    self.assertRaises(ValueError, mod.insort_left, [1, 2, 3], 5, -1, 3)
    self.assertRaises(ValueError, mod.insort_right, [1, 2, 3], 5, -1, 3)
