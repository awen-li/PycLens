# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_strided_limits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = range(0, 101, 2)
    self.assertIn(0, r)
    self.assertNotIn(1, r)
    self.assertIn(2, r)
    self.assertNotIn(99, r)
    self.assertIn(100, r)
    self.assertNotIn(101, r)
    r = range(0, -20, -1)
    self.assertIn(0, r)
    self.assertIn(-1, r)
    self.assertIn(-19, r)
    self.assertNotIn(-20, r)
    r = range(0, -20, -2)
    self.assertIn(-18, r)
    self.assertNotIn(-19, r)
    self.assertNotIn(-20, r)
