# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: TestSubClassingCase_test_formatweek_head

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    header = self.cal.formatweekheader()
    for color in self.cal.cssclasses_weekday_head:
        self.assertIn('<th class="%s">' % color, header)
