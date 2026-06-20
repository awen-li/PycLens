# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: SundayTestCase_test_february

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_weeks(2009, 2, (7, 7, 7, 7))
    self.check_weeks(1999, 2, (6, 7, 7, 7, 1))
    self.check_weeks(1997, 2, (1, 7, 7, 7, 6))
    self.check_weeks(2004, 2, (7, 7, 7, 7, 1))
    self.check_weeks(1960, 2, (6, 7, 7, 7, 2))
    self.check_weeks(1964, 2, (1, 7, 7, 7, 7))
