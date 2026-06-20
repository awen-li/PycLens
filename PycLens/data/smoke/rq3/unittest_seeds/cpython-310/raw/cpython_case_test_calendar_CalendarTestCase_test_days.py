# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CalendarTestCase_test_days

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for attr in ('day_name', 'day_abbr'):
        value = getattr(calendar, attr)
        self.assertEqual(len(value), 7)
        self.assertEqual(len(value[:]), 7)
        self.assertEqual(len(set(value)), 7)
        self.assertEqual(value[::-1], list(reversed(value)))
