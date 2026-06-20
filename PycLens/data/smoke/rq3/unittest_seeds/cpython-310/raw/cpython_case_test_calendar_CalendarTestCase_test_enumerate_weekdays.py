# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CalendarTestCase_test_enumerate_weekdays

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(IndexError, calendar.day_abbr.__getitem__, -10)
    self.assertRaises(IndexError, calendar.day_name.__getitem__, 10)
    self.assertEqual(len([d for d in calendar.day_abbr]), 7)
