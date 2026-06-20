# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: HTMLParserTestCase_test_slashes_in_starttag

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._run_check('<a foo="var"/>', [('startendtag', 'a', [('foo', 'var')])])
    html = '<img width=902 height=250px src="/sites/default/files/images/homepage/foo.jpg" /*what am I doing here*/ />'
    expected = [('startendtag', 'img', [('width', '902'), ('height', '250px'), ('src', '/sites/default/files/images/homepage/foo.jpg'), ('*what', None), ('am', None), ('i', None), ('doing', None), ('here*', None)])]
    self._run_check(html, expected)
    html = '<a / /foo/ / /=/ / /bar/ / /><a / /foo/ / /=/ / /bar/ / >'
    expected = [('startendtag', 'a', [('foo', None), ('=', None), ('bar', None)]), ('starttag', 'a', [('foo', None), ('=', None), ('bar', None)])]
    self._run_check(html, expected)
    html = '<meta><meta / ><meta // ><meta / / ><meta/><meta /><meta //><meta//>'
    expected = [('starttag', 'meta', []), ('starttag', 'meta', []), ('starttag', 'meta', []), ('starttag', 'meta', []), ('startendtag', 'meta', []), ('startendtag', 'meta', []), ('startendtag', 'meta', []), ('startendtag', 'meta', [])]
    self._run_check(html, expected)
