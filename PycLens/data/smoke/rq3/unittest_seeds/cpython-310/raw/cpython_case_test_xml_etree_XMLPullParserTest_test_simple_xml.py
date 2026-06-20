# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: XMLPullParserTest_test_simple_xml

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for chunk_size in (None, 1, 5):
        with self.subTest(chunk_size=chunk_size):
            parser = ET.XMLPullParser()
            self.assert_event_tags(parser, [])
            self._feed(parser, '<!-- comment -->\n', chunk_size)
            self.assert_event_tags(parser, [])
            self._feed(parser, "<root>\n  <element key='value'>text</element", chunk_size)
            self.assert_event_tags(parser, [])
            self._feed(parser, '>\n', chunk_size)
            self.assert_event_tags(parser, [('end', 'element')])
            self._feed(parser, '<element>text</element>tail\n', chunk_size)
            self._feed(parser, '<empty-element/>\n', chunk_size)
            self.assert_event_tags(parser, [('end', 'element'), ('end', 'empty-element')])
            self._feed(parser, '</root>\n', chunk_size)
            self.assert_event_tags(parser, [('end', 'root')])
            self.assertIsNone(parser.close())
