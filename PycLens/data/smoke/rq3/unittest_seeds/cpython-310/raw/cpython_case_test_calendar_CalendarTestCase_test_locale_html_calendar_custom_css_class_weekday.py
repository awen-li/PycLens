# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CalendarTestCase_test_locale_html_calendar_custom_css_class_weekday

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        cal = calendar.LocaleHTMLCalendar(locale='')
        local_weekday = cal.formatweekday(6)
    except locale.Error:
        raise unittest.SkipTest('cannot set the system default locale')
    self.assertIn('class="sun"', local_weekday)
    cal.cssclasses_weekday_head = ['mon2', 'tue2', 'wed2', 'thu2', 'fri2', 'sat2', 'sun2']
    local_weekday = cal.formatweekday(6)
    self.assertIn('class="sun2"', local_weekday)
