# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CommandLineTestCase_test_help

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stdout = self.run_ok('-h')
    self.assertIn(b'usage:', stdout)
    self.assertIn(b'calendar.py', stdout)
    self.assertIn(b'--help', stdout)
