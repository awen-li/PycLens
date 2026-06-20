# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementSlicingTest_test_setslice_negative_steps

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = self._make_elem_with_children(4)
    e[2:0:-1] = [ET.Element('b%s' % i) for i in range(2)]
    self.assertEqual(self._subelem_tags(e), ['a0', 'b1', 'b0', 'a3'])
    e = self._make_elem_with_children(4)
    with self.assertRaises(ValueError):
        e[2:0:-1] = [ET.Element('b')]
    with self.assertRaises(ValueError):
        e[2:0:-1] = [ET.Element('b%s' % i) for i in range(3)]
    with self.assertRaises(ValueError):
        e[2:0:-1] = []
    self.assertEqual(self._subelem_tags(e), ['a0', 'a1', 'a2', 'a3'])
    e = self._make_elem_with_children(4)
    e[1::-sys.maxsize] = [ET.Element('b')]
    self.assertEqual(self._subelem_tags(e), ['a0', 'b', 'a2', 'a3'])
    e[1::-sys.maxsize - 1] = [ET.Element('c')]
    self.assertEqual(self._subelem_tags(e), ['a0', 'c', 'a2', 'a3'])
    e[1::-sys.maxsize << 64] = [ET.Element('d')]
    self.assertEqual(self._subelem_tags(e), ['a0', 'd', 'a2', 'a3'])
