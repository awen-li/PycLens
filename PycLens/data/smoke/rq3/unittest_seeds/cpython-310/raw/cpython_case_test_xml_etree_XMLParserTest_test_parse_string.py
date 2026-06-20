# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: XMLParserTest_test_parse_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ET.XMLParser(target=ET.TreeBuilder())
    parser.feed(self.sample3)
    e = parser.close()
    self.assertEqual(e.tag, 'money')
    self.assertEqual(e.attrib['value'], '$£€𐅻')
    self.assertEqual(e.text, '$£€𐅻')
