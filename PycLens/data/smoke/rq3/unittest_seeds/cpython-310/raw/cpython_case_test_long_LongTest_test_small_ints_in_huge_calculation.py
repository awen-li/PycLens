# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_small_ints_in_huge_calculation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = 2 ** 100
    b = -a + 1
    c = a + 1
    self.assertIs(a + b, 1)
    self.assertIs(c - a, 1)
