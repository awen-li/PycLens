# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: TestSubClassingCase_test_format_year

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIn('<table border="0" cellpadding="0" cellspacing="0" class="%s">' % self.cal.cssclass_year, self.cal.formatyear(2017))
