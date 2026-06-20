# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: HTMLParserTestCase_test_EOF_in_charref

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [('a&', [('data', 'a&')]), ('a&b', [('data', 'ab')]), ('a&b ', [('data', 'a'), ('entityref', 'b'), ('data', ' ')]), ('a&b;', [('data', 'a'), ('entityref', 'b')])]
    for (html, expected) in data:
        self._run_check(html, expected)
