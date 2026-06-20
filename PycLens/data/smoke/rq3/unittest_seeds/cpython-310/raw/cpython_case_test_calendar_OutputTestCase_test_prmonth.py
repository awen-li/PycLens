# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: OutputTestCase_test_prmonth

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.captured_stdout() as out:
        calendar.TextCalendar().prmonth(2004, 1)
        self.assertEqual(out.getvalue(), result_2004_01_text)
