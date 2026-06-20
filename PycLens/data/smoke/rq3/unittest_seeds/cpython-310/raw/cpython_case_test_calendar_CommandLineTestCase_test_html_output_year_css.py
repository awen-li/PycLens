# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CommandLineTestCase_test_html_output_year_css

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFailure('-t', 'html', '-c')
    self.assertFailure('-t', 'html', '--css')
    stdout = self.run_ok('-t', 'html', '--css', 'custom.css', '2004')
    self.assertIn(b'<link rel="stylesheet" type="text/css" href="custom.css" />', stdout)
