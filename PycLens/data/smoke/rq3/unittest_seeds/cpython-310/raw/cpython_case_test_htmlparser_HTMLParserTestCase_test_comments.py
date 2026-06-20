# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: HTMLParserTestCase_test_comments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    html = "<!-- I'm a valid comment --><!--me too!--><!------><!----><!----I have many hyphens----><!-- I have a > in the middle --><!-- and I have -- in the middle! -->"
    expected = [('comment', " I'm a valid comment "), ('comment', 'me too!'), ('comment', '--'), ('comment', ''), ('comment', '--I have many hyphens--'), ('comment', ' I have a > in the middle '), ('comment', ' and I have -- in the middle! ')]
    self._run_check(html, expected)
