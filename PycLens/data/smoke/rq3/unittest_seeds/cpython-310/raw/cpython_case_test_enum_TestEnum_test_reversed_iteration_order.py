# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_reversed_iteration_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(reversed(self.Season)), [self.Season.WINTER, self.Season.AUTUMN, self.Season.SUMMER, self.Season.SPRING])
