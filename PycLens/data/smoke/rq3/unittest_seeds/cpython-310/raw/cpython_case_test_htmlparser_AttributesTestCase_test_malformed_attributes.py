# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: AttributesTestCase_test_malformed_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    html = "<a href=test'style='color:red;bad1'>test - bad1</a><a href=test'+style='color:red;ba2'>test - bad2</a><a href=test'&nbsp;style='color:red;bad3'>test - bad3</a><a href = test'&nbsp;style='color:red;bad4'  >test - bad4</a>"
    expected = [('starttag', 'a', [('href', "test'style='color:red;bad1'")]), ('data', 'test - bad1'), ('endtag', 'a'), ('starttag', 'a', [('href', "test'+style='color:red;ba2'")]), ('data', 'test - bad2'), ('endtag', 'a'), ('starttag', 'a', [('href', "test'\xa0style='color:red;bad3'")]), ('data', 'test - bad3'), ('endtag', 'a'), ('starttag', 'a', [('href', "test'\xa0style='color:red;bad4'")]), ('data', 'test - bad4'), ('endtag', 'a')]
    self._run_check(html, expected)
