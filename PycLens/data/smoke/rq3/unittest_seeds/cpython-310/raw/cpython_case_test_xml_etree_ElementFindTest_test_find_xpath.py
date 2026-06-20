# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementFindTest_test_find_xpath

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    LINEAR_XML = "\n        <body>\n            <tag class='a'/>\n            <tag class='b'/>\n            <tag class='c'/>\n            <tag class='d'/>\n        </body>"
    e = ET.XML(LINEAR_XML)
    self.assertEqual(e.find('./tag[1]').attrib['class'], 'a')
    self.assertEqual(e.find('./tag[2]').attrib['class'], 'b')
    self.assertEqual(e.find('./tag[last()]').attrib['class'], 'd')
    self.assertEqual(e.find('./tag[last()-1]').attrib['class'], 'c')
    self.assertEqual(e.find('./tag[last()-2]').attrib['class'], 'b')
    self.assertRaisesRegex(SyntaxError, 'XPath', e.find, './tag[0]')
    self.assertRaisesRegex(SyntaxError, 'XPath', e.find, './tag[-1]')
    self.assertRaisesRegex(SyntaxError, 'XPath', e.find, './tag[last()-0]')
    self.assertRaisesRegex(SyntaxError, 'XPath', e.find, './tag[last()+1]')
