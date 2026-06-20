# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CommandLineTestCase_test_option_spacing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFailure('-s')
    self.assertFailure('--spacing')
    self.assertFailure('-s', 'spam')
    stdout = self.run_ok('--spacing', '8', '2004')
    self.assertIn(b'Su        Mo', stdout)
