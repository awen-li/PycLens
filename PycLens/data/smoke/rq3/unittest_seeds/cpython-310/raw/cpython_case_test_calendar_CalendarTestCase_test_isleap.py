# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CalendarTestCase_test_isleap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(calendar.isleap(2000), 1)
    self.assertEqual(calendar.isleap(2001), 0)
    self.assertEqual(calendar.isleap(2002), 0)
    self.assertEqual(calendar.isleap(2003), 0)
