# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementSlicingTest_test_getslice_negative_steps

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = self._make_elem_with_children(4)
    self.assertEqual(self._elem_tags(e[::-1]), ['a3', 'a2', 'a1', 'a0'])
    self.assertEqual(self._elem_tags(e[::-2]), ['a3', 'a1'])
    self.assertEqual(self._elem_tags(e[3::-sys.maxsize]), ['a3'])
    self.assertEqual(self._elem_tags(e[3::-sys.maxsize - 1]), ['a3'])
    self.assertEqual(self._elem_tags(e[3::-sys.maxsize << 64]), ['a3'])
