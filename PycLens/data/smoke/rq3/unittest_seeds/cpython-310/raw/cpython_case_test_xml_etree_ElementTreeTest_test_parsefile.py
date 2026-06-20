# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_parsefile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tree = ET.parse(SIMPLE_XMLFILE)
    stream = io.StringIO()
    tree.write(stream, encoding='unicode')
    self.assertEqual(stream.getvalue(), '<root>\n   <element key="value">text</element>\n   <element>text</element>tail\n   <empty-element />\n</root>')
    tree = ET.parse(SIMPLE_NS_XMLFILE)
    stream = io.StringIO()
    tree.write(stream, encoding='unicode')
    self.assertEqual(stream.getvalue(), '<ns0:root xmlns:ns0="namespace">\n   <ns0:element key="value">text</ns0:element>\n   <ns0:element>text</ns0:element>tail\n   <ns0:empty-element />\n</ns0:root>')
    with open(SIMPLE_XMLFILE) as f:
        data = f.read()
    parser = ET.XMLParser()
    self.assertRegex(parser.version, '^Expat ')
    parser.feed(data)
    self.serialize_check(parser.close(), '<root>\n   <element key="value">text</element>\n   <element>text</element>tail\n   <empty-element />\n</root>')
    target = ET.TreeBuilder()
    parser = ET.XMLParser(target=target)
    parser.feed(data)
    self.serialize_check(parser.close(), '<root>\n   <element key="value">text</element>\n   <element>text</element>tail\n   <empty-element />\n</root>')
