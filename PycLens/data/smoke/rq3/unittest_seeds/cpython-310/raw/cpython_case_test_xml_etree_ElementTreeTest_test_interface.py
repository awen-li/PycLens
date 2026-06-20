# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_interface

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check_element(element):
        self.assertTrue(ET.iselement(element), msg='not an element')
        direlem = dir(element)
        for attr in ('tag', 'attrib', 'text', 'tail'):
            self.assertTrue(hasattr(element, attr), msg='no %s member' % attr)
            self.assertIn(attr, direlem, msg='no %s visible by dir' % attr)
        self.assertIsInstance(element.tag, str)
        self.assertIsInstance(element.attrib, dict)
        if element.text is not None:
            self.assertIsInstance(element.text, str)
        if element.tail is not None:
            self.assertIsInstance(element.tail, str)
        for elem in element:
            check_element(elem)
    element = ET.Element('tag')
    check_element(element)
    tree = ET.ElementTree(element)
    check_element(tree.getroot())
    element = ET.Element('täg', key='value')
    tree = ET.ElementTree(element)
    self.assertRegex(repr(element), "^<Element 't\\xe4g' at 0x.*>$")
    element = ET.Element('tag', key='value')

    def check_method(method):
        self.assertTrue(hasattr(method, '__call__'), msg='%s not callable' % method)
    check_method(element.append)
    check_method(element.extend)
    check_method(element.insert)
    check_method(element.remove)
    check_method(element.find)
    check_method(element.iterfind)
    check_method(element.findall)
    check_method(element.findtext)
    check_method(element.clear)
    check_method(element.get)
    check_method(element.set)
    check_method(element.keys)
    check_method(element.items)
    check_method(element.iter)
    check_method(element.itertext)

    def check_iter(it):
        check_method(it.__next__)
    check_iter(element.iterfind('tag'))
    check_iter(element.iterfind('*'))
    check_iter(tree.iterfind('tag'))
    check_iter(tree.iterfind('*'))
    self.assertEqual(ET.XML, ET.fromstring)
    self.assertEqual(ET.PI, ET.ProcessingInstruction)
