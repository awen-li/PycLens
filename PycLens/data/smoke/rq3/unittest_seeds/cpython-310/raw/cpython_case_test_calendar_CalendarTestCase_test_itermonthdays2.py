# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CalendarTestCase_test_itermonthdays2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for firstweekday in range(7):
        cal = calendar.Calendar(firstweekday)
        for (y, m) in [(1, 1), (9999, 12)]:
            days = list(cal.itermonthdays2(y, m))
            self.assertEqual(days[0][1], firstweekday)
            self.assertEqual(days[-1][1], (firstweekday - 1) % 7)
