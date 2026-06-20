# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementSlicingTest_test_setslice_steps

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = self._make_elem_with_children(6)
    e[1:5:2] = [ET.Element('b%s' % i) for i in range(2)]
    self.assertEqual(self._subelem_tags(e), ['a0', 'b0', 'a2', 'b1', 'a4', 'a5'])
    e = self._make_elem_with_children(6)
    with self.assertRaises(ValueError):
        e[1:5:2] = [ET.Element('b')]
    with self.assertRaises(ValueError):
        e[1:5:2] = [ET.Element('b%s' % i) for i in range(3)]
    with self.assertRaises(ValueError):
        e[1:5:2] = []
    self.assertEqual(self._subelem_tags(e), ['a0', 'a1', 'a2', 'a3', 'a4', 'a5'])
    e = self._make_elem_with_children(4)
    e[1::sys.maxsize] = [ET.Element('b')]
    self.assertEqual(self._subelem_tags(e), ['a0', 'b', 'a2', 'a3'])
    e[1::sys.maxsize << 64] = [ET.Element('c')]
    self.assertEqual(self._subelem_tags(e), ['a0', 'c', 'a2', 'a3'])
