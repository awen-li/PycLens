# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementSlicingTest_test_getslice_steps

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = self._make_elem_with_children(10)
    self.assertEqual(self._elem_tags(e[8:10:1]), ['a8', 'a9'])
    self.assertEqual(self._elem_tags(e[::3]), ['a0', 'a3', 'a6', 'a9'])
    self.assertEqual(self._elem_tags(e[::8]), ['a0', 'a8'])
    self.assertEqual(self._elem_tags(e[1::8]), ['a1', 'a9'])
    self.assertEqual(self._elem_tags(e[3::sys.maxsize]), ['a3'])
    self.assertEqual(self._elem_tags(e[3::sys.maxsize << 64]), ['a3'])
