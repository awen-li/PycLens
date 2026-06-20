# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = range(0)
    self.assertNotIn(0, r)
    self.assertNotIn(1, r)
    r = range(0, -10)
    self.assertNotIn(0, r)
    self.assertNotIn(-1, r)
    self.assertNotIn(1, r)
