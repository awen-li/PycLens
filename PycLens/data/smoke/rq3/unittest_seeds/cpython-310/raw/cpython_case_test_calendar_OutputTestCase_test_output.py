# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: OutputTestCase_test_output

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.normalize_calendar(calendar.calendar(2004)), self.normalize_calendar(result_2004_text))
    self.assertEqual(self.normalize_calendar(calendar.calendar(0)), self.normalize_calendar(result_0_text))
