# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: OutputTestCase_test_output_textcalendar

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(calendar.TextCalendar().formatyear(2004), result_2004_text)
    self.assertEqual(calendar.TextCalendar().formatyear(0), result_0_text)
