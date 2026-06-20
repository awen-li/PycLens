# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CommandLineTestCase_test_option_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFailure('-e')
    self.assertFailure('--encoding')
    stdout = self.run_ok('--encoding', 'utf-16-le', '2004')
    self.assertEqual(stdout, result_2004_text.encode('utf-16-le'))
