# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementIterTest_test_corners

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = ET.Element('a')
    self.assertEqual(self._ilist(a), ['a'])
    b = ET.SubElement(a, 'b')
    self.assertEqual(self._ilist(a), ['a', 'b'])
    c = ET.SubElement(b, 'c')
    self.assertEqual(self._ilist(a), ['a', 'b', 'c'])
    d = ET.SubElement(a, 'd')
    self.assertEqual(self._ilist(a), ['a', 'b', 'c', 'd'])
    a[0] = a[1]
    del a[1]
    self.assertEqual(self._ilist(a), ['a', 'd'])
