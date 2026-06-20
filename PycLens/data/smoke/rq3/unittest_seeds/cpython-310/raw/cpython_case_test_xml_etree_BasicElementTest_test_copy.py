# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BasicElementTest_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if 'copy' not in dir(ET.Element):
        raise unittest.SkipTest('Element.copy() not present')
    element_foo = ET.Element('foo', {'zix': 'wyp'})
    element_foo.append(ET.Element('bar', {'baz': 'qix'}))
    with self.assertWarns(DeprecationWarning):
        element_foo2 = element_foo.copy()
    self.assertIsNot(element_foo2, element_foo)
    self.assertEqual(element_foo2.tag, element_foo.tag)
    self.assertEqual(element_foo2.text, element_foo.text)
    self.assertEqual(element_foo2.tail, element_foo.tail)
    self.assertEqual(len(element_foo2), len(element_foo))
    for (child1, child2) in itertools.zip_longest(element_foo, element_foo2):
        self.assertIs(child1, child2)
    self.assertEqual(element_foo2.attrib, element_foo.attrib)
