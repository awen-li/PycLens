# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementSlicingTest_test_getslice_range

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = self._make_elem_with_children(6)
    self.assertEqual(self._elem_tags(e[3:]), ['a3', 'a4', 'a5'])
    self.assertEqual(self._elem_tags(e[3:6]), ['a3', 'a4', 'a5'])
    self.assertEqual(self._elem_tags(e[3:16]), ['a3', 'a4', 'a5'])
    self.assertEqual(self._elem_tags(e[3:5]), ['a3', 'a4'])
    self.assertEqual(self._elem_tags(e[3:-1]), ['a3', 'a4'])
    self.assertEqual(self._elem_tags(e[:2]), ['a0', 'a1'])
