# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CommandLineTestCase_test_output_month

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stdout = self.run_ok('2004', '1')
    self.assertEqual(stdout, conv(result_2004_01_text))
