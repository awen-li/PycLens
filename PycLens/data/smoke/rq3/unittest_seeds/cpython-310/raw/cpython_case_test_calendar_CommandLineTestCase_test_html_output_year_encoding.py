# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CommandLineTestCase_test_html_output_year_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stdout = self.run_ok('-t', 'html', '--encoding', 'ascii', '2004')
    self.assertEqual(stdout, result_2004_html.format(**default_format).encode('ascii'))
