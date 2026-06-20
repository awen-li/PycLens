# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: SundayTestCase_test_december

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_weeks(2080, 12, (7, 7, 7, 7, 3))
    self.check_weeks(1941, 12, (6, 7, 7, 7, 4))
    self.check_weeks(1923, 12, (1, 7, 7, 7, 7, 2))
    self.check_weeks(1948, 12, (4, 7, 7, 7, 6))
    self.check_weeks(1927, 12, (3, 7, 7, 7, 7))
    self.check_weeks(1995, 12, (2, 7, 7, 7, 7, 1))
