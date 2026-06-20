# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_children

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(SIMPLE_XMLFILE, 'rb') as f:
        tree = ET.parse(f)
    self.assertEqual([summarize_list(elem) for elem in tree.getroot().iter()], [['element', 'element', 'empty-element'], [], [], []])
    self.assertEqual([summarize_list(elem) for elem in tree.iter()], [['element', 'element', 'empty-element'], [], [], []])
    elem = ET.XML(SAMPLE_XML)
    self.assertEqual(len(list(elem)), 3)
    self.assertEqual(len(list(elem[2])), 1)
    self.assertEqual(elem[:], list(elem))
    child1 = elem[0]
    child2 = elem[2]
    del elem[1:2]
    self.assertEqual(len(list(elem)), 2)
    self.assertEqual(child1, elem[0])
    self.assertEqual(child2, elem[1])
    elem[0:2] = [child2, child1]
    self.assertEqual(child2, elem[0])
    self.assertEqual(child1, elem[1])
    self.assertNotEqual(child1, elem[0])
    elem.clear()
    self.assertEqual(list(elem), [])
