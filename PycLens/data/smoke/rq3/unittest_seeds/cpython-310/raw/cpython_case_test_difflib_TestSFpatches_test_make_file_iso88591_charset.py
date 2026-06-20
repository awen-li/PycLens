# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestSFpatches_test_make_file_iso88591_charset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    html_diff = difflib.HtmlDiff()
    output = html_diff.make_file(patch914575_from1.splitlines(), patch914575_to1.splitlines(), charset='iso-8859-1')
    self.assertIn('content="text/html; charset=iso-8859-1"', output)
