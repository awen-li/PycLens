# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementSlicingTest_test_setslice_range

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = self._make_elem_with_children(4)
    e[1:3] = [ET.Element('b%s' % i) for i in range(2)]
    self.assertEqual(self._subelem_tags(e), ['a0', 'b0', 'b1', 'a3'])
    e = self._make_elem_with_children(4)
    e[1:3] = [ET.Element('b')]
    self.assertEqual(self._subelem_tags(e), ['a0', 'b', 'a3'])
    e = self._make_elem_with_children(4)
    e[1:3] = [ET.Element('b%s' % i) for i in range(3)]
    self.assertEqual(self._subelem_tags(e), ['a0', 'b0', 'b1', 'b2', 'a3'])
