# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: AttributesTestCase_test_with_unquoted_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    html = "<html><body bgcolor=d0ca90 text='181008'><table cellspacing=0 cellpadding=1 width=100% ><tr><td align=left><font size=-1>- <a href=/rabota/><span class=en> software-and-i</span></a>- <a href='/1/'><span class=en> library</span></a></table>"
    expected = [('starttag', 'html', []), ('starttag', 'body', [('bgcolor', 'd0ca90'), ('text', '181008')]), ('starttag', 'table', [('cellspacing', '0'), ('cellpadding', '1'), ('width', '100%')]), ('starttag', 'tr', []), ('starttag', 'td', [('align', 'left')]), ('starttag', 'font', [('size', '-1')]), ('data', '- '), ('starttag', 'a', [('href', '/rabota/')]), ('starttag', 'span', [('class', 'en')]), ('data', ' software-and-i'), ('endtag', 'span'), ('endtag', 'a'), ('data', '- '), ('starttag', 'a', [('href', '/1/')]), ('starttag', 'span', [('class', 'en')]), ('data', ' library'), ('endtag', 'span'), ('endtag', 'a'), ('endtag', 'table')]
    self._run_check(html, expected)
