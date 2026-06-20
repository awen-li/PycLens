# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestSFpatches_test_make_file_usascii_charset_with_nonascii_input

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    html_diff = difflib.HtmlDiff()
    output = html_diff.make_file(patch914575_nonascii_from1.splitlines(), patch914575_nonascii_to1.splitlines(), charset='us-ascii')
    self.assertIn('content="text/html; charset=us-ascii"', output)
    self.assertIn('&#305;mpl&#305;c&#305;t', output)
