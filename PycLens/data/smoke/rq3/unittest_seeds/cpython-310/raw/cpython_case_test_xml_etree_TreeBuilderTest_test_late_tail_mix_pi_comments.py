# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: TreeBuilderTest_test_late_tail_mix_pi_comments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TreeBuilderSubclass(ET.TreeBuilder):
        pass
    xml = '<a>text<?pi1?> <!-- comment -->\n<?pi2?>tail</a>'
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    parser.feed(xml)
    a = parser.close()
    self.assertEqual(a[0].text, ' comment ')
    self.assertEqual(a[0].tail, '\ntail')
    self.assertEqual(a.text, 'text ')
    parser = ET.XMLParser(target=TreeBuilderSubclass(insert_comments=True))
    parser.feed(xml)
    a = parser.close()
    self.assertEqual(a[0].text, ' comment ')
    self.assertEqual(a[0].tail, '\ntail')
    self.assertEqual(a.text, 'text ')
    xml = '<a>text<!-- comment -->\n<?pi data?>tail</a>'
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_pis=True))
    parser.feed(xml)
    a = parser.close()
    self.assertEqual(a[0].text, 'pi data')
    self.assertEqual(a[0].tail, 'tail')
    self.assertEqual(a.text, 'text\n')
    parser = ET.XMLParser(target=TreeBuilderSubclass(insert_pis=True))
    parser.feed(xml)
    a = parser.close()
    self.assertEqual(a[0].text, 'pi data')
    self.assertEqual(a[0].tail, 'tail')
    self.assertEqual(a.text, 'text\n')
