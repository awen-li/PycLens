# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: HTMLParserTestCase_test_convert_charrefs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    collector = lambda : EventCollectorCharrefs()
    self.assertTrue(collector().convert_charrefs)
    charrefs = ['&quot;', '&#34;', '&#x22;', '&quot', '&#34', '&#x22']
    expected = [('starttag', 'a', [('href', 'foo"zar')]), ('data', 'a"z'), ('endtag', 'a')]
    for charref in charrefs:
        self._run_check('<a href="foo{0}zar">a{0}z</a>'.format(charref), expected, collector=collector())
    expected = [('data', '"'), ('starttag', 'a', [('x', '"'), ('y', '"X'), ('z', 'X"')]), ('data', '"'), ('endtag', 'a'), ('data', '"')]
    for charref in charrefs:
        self._run_check('{0}<a x="{0}" y="{0}X" z="X{0}">{0}</a>{0}'.format(charref), expected, collector=collector())
    for charref in charrefs:
        text = 'X'.join([charref] * 3)
        expected = [('data', '"'), ('starttag', 'script', []), ('data', text), ('endtag', 'script'), ('data', '"'), ('starttag', 'style', []), ('data', text), ('endtag', 'style'), ('data', '"')]
        self._run_check('{1}<script>{0}</script>{1}<style>{0}</style>{1}'.format(text, charref), expected, collector=collector())
    html = '&quo &# &#x'
    for x in range(1, len(html)):
        self._run_check(html[:x], [('data', html[:x])], collector=collector())
    self._run_check('no charrefs here', [('data', 'no charrefs here')], collector=collector())
