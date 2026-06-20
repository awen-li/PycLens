# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_entity

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = ET.XML("<document title='&#x8230;'>test</document>")
    self.assertEqual(serialize(e, encoding='us-ascii'), b'<document title="&#33328;">test</document>')
    self.serialize_check(e, '<document title="舰">test</document>')
    with self.assertRaises(ET.ParseError) as cm:
        ET.XML('<document>&entity;</document>')
    self.assertEqual(str(cm.exception), 'undefined entity: line 1, column 10')
    with self.assertRaises(ET.ParseError) as cm:
        ET.XML(ENTITY_XML)
    self.assertEqual(str(cm.exception), 'undefined entity &entity;: line 5, column 10')
    parser = ET.XMLParser()
    parser.entity['entity'] = 'text'
    parser.feed(ENTITY_XML)
    root = parser.close()
    self.serialize_check(root, '<document>text</document>')
    with self.assertRaises(ET.ParseError) as cm:
        ET.XML(EXTERNAL_ENTITY_XML)
    self.assertEqual(str(cm.exception), 'undefined entity &entity;: line 4, column 10')
