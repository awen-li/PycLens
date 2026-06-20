# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_richcmp.py
# case: ListTest_test_coverage

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = [42]
    self.assertIs(x < x, False)
    self.assertIs(x <= x, True)
    self.assertIs(x == x, True)
    self.assertIs(x != x, False)
    self.assertIs(x > x, False)
    self.assertIs(x >= x, True)
    y = [42, 42]
    self.assertIs(x < y, True)
    self.assertIs(x <= y, True)
    self.assertIs(x == y, False)
    self.assertIs(x != y, True)
    self.assertIs(x > y, False)
    self.assertIs(x >= y, False)
