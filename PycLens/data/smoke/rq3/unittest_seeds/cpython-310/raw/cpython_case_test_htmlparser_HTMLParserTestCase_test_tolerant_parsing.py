# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: HTMLParserTestCase_test_tolerant_parsing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._run_check('<html <html>te>>xt&a<<bc</a></html>\n<img src="URL><//img></html</html>', [('starttag', 'html', [('<html', None)]), ('data', 'te>>xt'), ('entityref', 'a'), ('data', '<'), ('starttag', 'bc<', [('a', None)]), ('endtag', 'html'), ('data', '\n<img src="URL>'), ('comment', '/img'), ('endtag', 'html<')])
