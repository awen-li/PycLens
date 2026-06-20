# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CommandLineTestCase_test_option_width

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFailure('-w')
    self.assertFailure('--width')
    self.assertFailure('-w', 'spam')
    stdout = self.run_ok('--width', '3', '2004')
    self.assertIn(b'Mon Tue Wed Thu Fri Sat Sun', stdout)
