# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: TestSubClassingCase_test_format_year_head

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIn('<tr><th colspan="%d" class="%s">%s</th></tr>' % (3, self.cal.cssclass_year_head, 2017), self.cal.formatyear(2017))
