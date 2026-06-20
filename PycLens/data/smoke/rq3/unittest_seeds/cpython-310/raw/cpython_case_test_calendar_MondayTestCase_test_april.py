# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: MondayTestCase_test_april

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_weeks(1935, 4, (7, 7, 7, 7, 2))
    self.check_weeks(1975, 4, (6, 7, 7, 7, 3))
    self.check_weeks(1945, 4, (1, 7, 7, 7, 7, 1))
    self.check_weeks(1995, 4, (2, 7, 7, 7, 7))
    self.check_weeks(1994, 4, (3, 7, 7, 7, 6))
