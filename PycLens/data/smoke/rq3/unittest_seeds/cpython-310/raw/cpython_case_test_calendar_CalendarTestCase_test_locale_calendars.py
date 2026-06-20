# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CalendarTestCase_test_locale_calendars

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    old_october = calendar.TextCalendar().formatmonthname(2010, 10, 10)
    try:
        cal = calendar.LocaleTextCalendar(locale='')
        local_weekday = cal.formatweekday(1, 10)
        local_month = cal.formatmonthname(2010, 10, 10)
    except locale.Error:
        raise unittest.SkipTest('cannot set the system default locale')
    self.assertIsInstance(local_weekday, str)
    self.assertIsInstance(local_month, str)
    self.assertEqual(len(local_weekday), 10)
    self.assertGreaterEqual(len(local_month), 10)
    cal = calendar.LocaleHTMLCalendar(locale='')
    local_weekday = cal.formatweekday(1)
    local_month = cal.formatmonthname(2010, 10)
    self.assertIsInstance(local_weekday, str)
    self.assertIsInstance(local_month, str)
    new_october = calendar.TextCalendar().formatmonthname(2010, 10, 10)
    self.assertEqual(old_october, new_october)
