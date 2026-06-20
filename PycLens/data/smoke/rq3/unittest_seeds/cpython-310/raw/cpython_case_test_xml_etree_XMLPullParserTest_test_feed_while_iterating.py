# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: XMLPullParserTest_test_feed_while_iterating

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ET.XMLPullParser()
    it = parser.read_events()
    self._feed(parser, "<root>\n  <element key='value'>text</element>\n")
    (action, elem) = next(it)
    self.assertEqual((action, elem.tag), ('end', 'element'))
    self._feed(parser, '</root>\n')
    (action, elem) = next(it)
    self.assertEqual((action, elem.tag), ('end', 'root'))
    with self.assertRaises(StopIteration):
        next(it)
