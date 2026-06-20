# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CommandLineTestCase_test_output_current_year

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stdout = self.run_ok()
    year = datetime.datetime.now().year
    self.assertIn((' %s' % year).encode(), stdout)
    self.assertIn(b'January', stdout)
    self.assertIn(b'Mo Tu We Th Fr Sa Su', stdout)
