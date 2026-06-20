# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CommandLineTestCase_test_option_lines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFailure('-l')
    self.assertFailure('--lines')
    self.assertFailure('-l', 'spam')
    stdout = self.run_ok('--lines', '2', '2004')
    self.assertIn(conv('December\n\nMo Tu We'), stdout)
