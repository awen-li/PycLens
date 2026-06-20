# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CalendarTestCase_test_locale_calendar_formatweekday

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        cal = calendar.LocaleTextCalendar(locale='en_US')
        self.assertEqual(cal.formatweekday(0, 1), 'M')
        self.assertEqual(cal.formatweekday(0, 2), 'Mo')
        self.assertEqual(cal.formatweekday(0, 3), 'Mon')
        self.assertEqual(cal.formatweekday(0, 5), ' Mon ')
        self.assertEqual(cal.formatweekday(0, 8), '  Mon   ')
        self.assertEqual(cal.formatweekday(0, 9), '  Monday ')
        self.assertEqual(cal.formatweekday(0, 10), '  Monday  ')
    except locale.Error:
        raise unittest.SkipTest('cannot set the en_US locale')
