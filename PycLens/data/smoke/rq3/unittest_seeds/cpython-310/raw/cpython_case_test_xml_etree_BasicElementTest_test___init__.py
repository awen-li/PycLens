# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BasicElementTest_test___init__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tag = 'foo'
    attrib = {'zix': 'wyp'}
    element_foo = ET.Element(tag, attrib)
    self.assertIsInstance(element_foo, ET.Element)
    self.assertIn('tag', dir(element_foo))
    self.assertIn('attrib', dir(element_foo))
    self.assertIn('text', dir(element_foo))
    self.assertIn('tail', dir(element_foo))
    self.assertEqual(element_foo.tag, tag)
    self.assertIsNone(element_foo.text)
    self.assertIsNone(element_foo.tail)
    self.assertIsNot(element_foo.attrib, attrib)
    self.assertEqual(element_foo.attrib, attrib)
    attrib['bar'] = 'baz'
    self.assertIsNot(element_foo.attrib, attrib)
    self.assertNotEqual(element_foo.attrib, attrib)
