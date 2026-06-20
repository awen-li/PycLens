# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree_c.py
# case: MiscTests_test_del_attribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    element = cET.Element('tag')
    element.tag = 'TAG'
    with self.assertRaises(AttributeError):
        del element.tag
    self.assertEqual(element.tag, 'TAG')
    with self.assertRaises(AttributeError):
        del element.text
    self.assertIsNone(element.text)
    element.text = 'TEXT'
    with self.assertRaises(AttributeError):
        del element.text
    self.assertEqual(element.text, 'TEXT')
    with self.assertRaises(AttributeError):
        del element.tail
    self.assertIsNone(element.tail)
    element.tail = 'TAIL'
    with self.assertRaises(AttributeError):
        del element.tail
    self.assertEqual(element.tail, 'TAIL')
    with self.assertRaises(AttributeError):
        del element.attrib
    self.assertEqual(element.attrib, {})
    element.attrib = {'A': 'B', 'C': 'D'}
    with self.assertRaises(AttributeError):
        del element.attrib
    self.assertEqual(element.attrib, {'A': 'B', 'C': 'D'})
