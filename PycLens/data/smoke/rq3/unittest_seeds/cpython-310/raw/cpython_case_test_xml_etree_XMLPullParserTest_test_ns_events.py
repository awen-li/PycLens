# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: XMLPullParserTest_test_ns_events

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ET.XMLPullParser(events=('start-ns', 'end-ns'))
    self._feed(parser, '<!-- comment -->\n')
    self._feed(parser, "<root xmlns='namespace'>\n")
    self.assertEqual(list(parser.read_events()), [('start-ns', ('', 'namespace'))])
    self._feed(parser, "<element key='value'>text</element")
    self._feed(parser, '>\n')
    self._feed(parser, '<element>text</element>tail\n')
    self._feed(parser, '<empty-element/>\n')
    self._feed(parser, '</root>\n')
    self.assertEqual(list(parser.read_events()), [('end-ns', None)])
    self.assertIsNone(parser.close())
