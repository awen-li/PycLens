# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assert_attrs(range(0), 0, 0, 1)
    self.assert_attrs(range(10), 0, 10, 1)
    self.assert_attrs(range(-10), 0, -10, 1)
    self.assert_attrs(range(0, 10, 1), 0, 10, 1)
    self.assert_attrs(range(0, 10, 3), 0, 10, 3)
    self.assert_attrs(range(10, 0, -1), 10, 0, -1)
    self.assert_attrs(range(10, 0, -3), 10, 0, -3)
    self.assert_attrs(range(True), 0, 1, 1)
    self.assert_attrs(range(False, True), 0, 1, 1)
    self.assert_attrs(range(False, True, True), 0, 1, 1)
