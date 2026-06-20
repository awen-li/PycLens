# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: OutputTestCase_test_formatmonthname_without_year

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(calendar.HTMLCalendar().formatmonthname(2004, 1, withyear=False), '<tr><th colspan="7" class="month">January</th></tr>')
