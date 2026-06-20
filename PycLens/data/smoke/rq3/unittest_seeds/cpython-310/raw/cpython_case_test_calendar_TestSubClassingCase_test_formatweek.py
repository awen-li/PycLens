# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: TestSubClassingCase_test_formatweek

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    weeks = self.cal.monthdays2calendar(2017, 5)
    self.assertIn('class="wed text-nowrap"', self.cal.formatweek(weeks[0]))
