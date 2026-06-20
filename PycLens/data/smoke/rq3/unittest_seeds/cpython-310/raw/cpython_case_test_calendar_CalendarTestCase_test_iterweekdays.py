# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CalendarTestCase_test_iterweekdays

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    week0 = list(range(7))
    for firstweekday in range(7):
        cal = calendar.Calendar(firstweekday)
        week = list(cal.iterweekdays())
        expected = week0[firstweekday:] + week0[:firstweekday]
        self.assertEqual(week, expected)
