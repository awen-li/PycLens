# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: OutputTestCase_test_formatweekheader_long

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(calendar.TextCalendar().formatweekheader(9), '  Monday   Tuesday  Wednesday  Thursday   Friday   Saturday   Sunday ')
