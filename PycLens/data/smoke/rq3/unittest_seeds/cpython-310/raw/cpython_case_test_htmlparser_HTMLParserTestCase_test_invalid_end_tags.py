# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: HTMLParserTestCase_test_invalid_end_tags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    html = '<br></label</p><br></div end tmAd-leaderBoard><br></<h4><br></li class="unit"><br></li\r\n\t\t\t\t\t\t</ul><br></><br>'
    expected = [('starttag', 'br', []), ('endtag', 'label<'), ('starttag', 'br', []), ('endtag', 'div'), ('starttag', 'br', []), ('comment', '<h4'), ('starttag', 'br', []), ('endtag', 'li'), ('starttag', 'br', []), ('endtag', 'li'), ('starttag', 'br', []), ('starttag', 'br', [])]
    self._run_check(html, expected)
