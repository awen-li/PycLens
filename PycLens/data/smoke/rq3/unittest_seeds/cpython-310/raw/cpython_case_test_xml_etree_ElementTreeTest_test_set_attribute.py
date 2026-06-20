# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_set_attribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    element = ET.Element('tag')
    self.assertEqual(element.tag, 'tag')
    element.tag = 'Tag'
    self.assertEqual(element.tag, 'Tag')
    element.tag = 'TAG'
    self.assertEqual(element.tag, 'TAG')
    self.assertIsNone(element.text)
    element.text = 'Text'
    self.assertEqual(element.text, 'Text')
    element.text = 'TEXT'
    self.assertEqual(element.text, 'TEXT')
    self.assertIsNone(element.tail)
    element.tail = 'Tail'
    self.assertEqual(element.tail, 'Tail')
    element.tail = 'TAIL'
    self.assertEqual(element.tail, 'TAIL')
    self.assertEqual(element.attrib, {})
    element.attrib = {'a': 'b', 'c': 'd'}
    self.assertEqual(element.attrib, {'a': 'b', 'c': 'd'})
    element.attrib = {'A': 'B', 'C': 'D'}
    self.assertEqual(element.attrib, {'A': 'B', 'C': 'D'})
