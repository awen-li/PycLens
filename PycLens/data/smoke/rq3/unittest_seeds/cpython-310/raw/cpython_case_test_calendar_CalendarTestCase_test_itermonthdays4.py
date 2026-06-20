# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CalendarTestCase_test_itermonthdays4

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cal = calendar.Calendar(firstweekday=3)
    days = list(cal.itermonthdays4(2001, 2))
    self.assertEqual(days[0], (2001, 2, 1, 3))
    self.assertEqual(days[-1], (2001, 2, 28, 2))
