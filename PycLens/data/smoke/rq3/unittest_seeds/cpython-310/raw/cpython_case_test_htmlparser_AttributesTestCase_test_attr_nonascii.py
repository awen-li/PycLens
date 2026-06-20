# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: AttributesTestCase_test_attr_nonascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._run_check('<img src=/foo/bar.png alt=中文>', [('starttag', 'img', [('src', '/foo/bar.png'), ('alt', '中文')])])
    self._run_check("<a title='テスト' href='テスト.html'>", [('starttag', 'a', [('title', 'テスト'), ('href', 'テスト.html')])])
    self._run_check('<a title="テスト" href="テスト.html">', [('starttag', 'a', [('title', 'テスト'), ('href', 'テスト.html')])])
