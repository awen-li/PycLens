# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: HTMLParserTestCase_test_condcoms

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    html = "<!--[if IE & !(lte IE 8)]>aren't<![endif]--><!--[if IE 8]>condcoms<![endif]--><!--[if lte IE 7]>pretty?<![endif]-->"
    expected = [('comment', "[if IE & !(lte IE 8)]>aren't<![endif]"), ('comment', '[if IE 8]>condcoms<![endif]'), ('comment', '[if lte IE 7]>pretty?<![endif]')]
    self._run_check(html, expected)
