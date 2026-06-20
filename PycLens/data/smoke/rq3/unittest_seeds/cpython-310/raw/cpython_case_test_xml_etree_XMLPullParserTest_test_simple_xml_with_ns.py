# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: XMLPullParserTest_test_simple_xml_with_ns

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ET.XMLPullParser()
    self.assert_event_tags(parser, [])
    self._feed(parser, '<!-- comment -->\n')
    self.assert_event_tags(parser, [])
    self._feed(parser, "<root xmlns='namespace'>\n")
    self.assert_event_tags(parser, [])
    self._feed(parser, "<element key='value'>text</element")
    self.assert_event_tags(parser, [])
    self._feed(parser, '>\n')
    self.assert_event_tags(parser, [('end', '{namespace}element')])
    self._feed(parser, '<element>text</element>tail\n')
    self._feed(parser, '<empty-element/>\n')
    self.assert_event_tags(parser, [('end', '{namespace}element'), ('end', '{namespace}empty-element')])
    self._feed(parser, '</root>\n')
    self.assert_event_tags(parser, [('end', '{namespace}root')])
    self.assertIsNone(parser.close())
