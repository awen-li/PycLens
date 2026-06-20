# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: HTMLParserTestCase_test_broken_comments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    html = '<! not really a comment ><! not a comment either --><! -- close enough --><!><!<-- this was an empty comment><!!! another bogus comment !!!>'
    expected = [('comment', ' not really a comment '), ('comment', ' not a comment either --'), ('comment', ' -- close enough --'), ('comment', ''), ('comment', '<-- this was an empty comment'), ('comment', '!! another bogus comment !!!')]
    self._run_check(html, expected)
