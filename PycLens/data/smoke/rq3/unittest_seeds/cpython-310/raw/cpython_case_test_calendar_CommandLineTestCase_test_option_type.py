# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CommandLineTestCase_test_option_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFailure('-t')
    self.assertFailure('--type')
    self.assertFailure('-t', 'spam')
    stdout = self.run_ok('--type', 'text', '2004')
    self.assertEqual(stdout, conv(result_2004_text))
    stdout = self.run_ok('--type', 'html', '2004')
    self.assertEqual(stdout[:6], b'<?xml ')
    self.assertIn(b'<title>Calendar for 2004</title>', stdout)
