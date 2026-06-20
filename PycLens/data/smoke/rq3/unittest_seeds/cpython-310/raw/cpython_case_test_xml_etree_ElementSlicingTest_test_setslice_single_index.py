# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementSlicingTest_test_setslice_single_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = self._make_elem_with_children(4)
    e[1] = ET.Element('b')
    self.assertEqual(self._subelem_tags(e), ['a0', 'b', 'a2', 'a3'])
    e[-2] = ET.Element('c')
    self.assertEqual(self._subelem_tags(e), ['a0', 'b', 'c', 'a3'])
    with self.assertRaises(IndexError):
        e[5] = ET.Element('d')
    with self.assertRaises(IndexError):
        e[-5] = ET.Element('d')
    self.assertEqual(self._subelem_tags(e), ['a0', 'b', 'c', 'a3'])
