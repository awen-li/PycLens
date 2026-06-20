# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_format_enum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Season = self.Season
    self.assertEqual('{}'.format(Season.SPRING), '{}'.format(str(Season.SPRING)))
    self.assertEqual('{:}'.format(Season.SPRING), '{:}'.format(str(Season.SPRING)))
    self.assertEqual('{:20}'.format(Season.SPRING), '{:20}'.format(str(Season.SPRING)))
    self.assertEqual('{:^20}'.format(Season.SPRING), '{:^20}'.format(str(Season.SPRING)))
    self.assertEqual('{:>20}'.format(Season.SPRING), '{:>20}'.format(str(Season.SPRING)))
    self.assertEqual('{:<20}'.format(Season.SPRING), '{:<20}'.format(str(Season.SPRING)))
