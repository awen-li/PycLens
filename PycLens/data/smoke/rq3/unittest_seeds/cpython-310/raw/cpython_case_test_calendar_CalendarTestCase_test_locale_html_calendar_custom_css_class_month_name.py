# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CalendarTestCase_test_locale_html_calendar_custom_css_class_month_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        cal = calendar.LocaleHTMLCalendar(locale='')
        local_month = cal.formatmonthname(2010, 10, 10)
    except locale.Error:
        raise unittest.SkipTest('cannot set the system default locale')
    self.assertIn('class="month"', local_month)
    cal.cssclass_month_head = 'text-center month'
    local_month = cal.formatmonthname(2010, 10, 10)
    self.assertIn('class="text-center month"', local_month)
