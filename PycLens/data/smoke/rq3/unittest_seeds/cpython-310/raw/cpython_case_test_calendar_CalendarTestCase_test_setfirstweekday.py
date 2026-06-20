# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CalendarTestCase_test_setfirstweekday

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, calendar.setfirstweekday, 'flabber')
    self.assertRaises(ValueError, calendar.setfirstweekday, -1)
    self.assertRaises(ValueError, calendar.setfirstweekday, 200)
    orig = calendar.firstweekday()
    calendar.setfirstweekday(calendar.SUNDAY)
    self.assertEqual(calendar.firstweekday(), calendar.SUNDAY)
    calendar.setfirstweekday(calendar.MONDAY)
    self.assertEqual(calendar.firstweekday(), calendar.MONDAY)
    calendar.setfirstweekday(orig)
