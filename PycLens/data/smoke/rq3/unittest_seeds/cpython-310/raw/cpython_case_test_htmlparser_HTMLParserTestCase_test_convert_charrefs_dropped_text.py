# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: HTMLParserTestCase_test_convert_charrefs_dropped_text

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = EventCollector(convert_charrefs=True)
    parser.feed('foo <a>link</a> bar &amp; baz')
    self.assertEqual(parser.get_events(), [('data', 'foo '), ('starttag', 'a', []), ('data', 'link'), ('endtag', 'a'), ('data', ' bar & baz')])
