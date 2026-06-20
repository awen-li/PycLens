# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: OutputTestCase_test_prweek

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.captured_stdout() as out:
        week = [(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6)]
        calendar.TextCalendar().prweek(week, 1)
        self.assertEqual(out.getvalue(), ' 1  2  3  4  5  6  7')
