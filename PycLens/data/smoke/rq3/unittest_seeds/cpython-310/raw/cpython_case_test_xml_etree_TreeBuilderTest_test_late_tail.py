# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: TreeBuilderTest_test_late_tail

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TreeBuilderSubclass(ET.TreeBuilder):
        pass
    xml = '<a>text<!-- comment -->tail</a>'
    a = ET.fromstring(xml)
    self.assertEqual(a.text, 'texttail')
    parser = ET.XMLParser(target=TreeBuilderSubclass())
    parser.feed(xml)
    a = parser.close()
    self.assertEqual(a.text, 'texttail')
    xml = '<a>text<?pi data?>tail</a>'
    a = ET.fromstring(xml)
    self.assertEqual(a.text, 'texttail')
    xml = '<a>text<?pi data?>tail</a>'
    parser = ET.XMLParser(target=TreeBuilderSubclass())
    parser.feed(xml)
    a = parser.close()
    self.assertEqual(a.text, 'texttail')
