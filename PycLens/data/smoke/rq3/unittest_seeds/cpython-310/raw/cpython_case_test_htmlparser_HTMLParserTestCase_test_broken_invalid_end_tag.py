# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: HTMLParserTestCase_test_broken_invalid_end_tag

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    html = '<b>This</b attr=">"> confuses the parser'
    expected = [('starttag', 'b', []), ('data', 'This'), ('endtag', 'b'), ('data', '"> confuses the parser')]
    self._run_check(html, expected)
