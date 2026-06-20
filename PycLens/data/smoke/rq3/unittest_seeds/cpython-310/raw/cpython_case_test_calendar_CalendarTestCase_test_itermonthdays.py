# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CalendarTestCase_test_itermonthdays

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for firstweekday in range(7):
        cal = calendar.Calendar(firstweekday)
        for (y, m) in [(1, 1), (9999, 12)]:
            days = list(cal.itermonthdays(y, m))
            self.assertIn(len(days), (35, 42))
    cal = calendar.Calendar(firstweekday=3)
    days = list(cal.itermonthdays(2001, 2))
    self.assertEqual(days, list(range(1, 29)))
