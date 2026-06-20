# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CommandLineTestCase_test_html_output_current_year

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stdout = self.run_ok('--type', 'html')
    year = datetime.datetime.now().year
    self.assertIn(('<title>Calendar for %s</title>' % year).encode(), stdout)
    self.assertIn(b'<tr><th colspan="7" class="month">January</th></tr>', stdout)
