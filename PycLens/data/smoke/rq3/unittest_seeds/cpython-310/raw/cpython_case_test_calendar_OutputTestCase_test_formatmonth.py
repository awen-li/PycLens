# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: OutputTestCase_test_formatmonth

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(calendar.TextCalendar().formatmonth(2004, 1), result_2004_01_text)
    self.assertEqual(calendar.TextCalendar().formatmonth(0, 2), result_0_02_text)
