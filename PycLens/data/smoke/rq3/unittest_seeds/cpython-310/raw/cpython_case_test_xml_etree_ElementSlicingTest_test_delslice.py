# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementSlicingTest_test_delslice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = self._make_elem_with_children(4)
    del e[0:2]
    self.assertEqual(self._subelem_tags(e), ['a2', 'a3'])
    e = self._make_elem_with_children(4)
    del e[0:]
    self.assertEqual(self._subelem_tags(e), [])
    e = self._make_elem_with_children(4)
    del e[::-1]
    self.assertEqual(self._subelem_tags(e), [])
    e = self._make_elem_with_children(4)
    del e[::-2]
    self.assertEqual(self._subelem_tags(e), ['a0', 'a2'])
    e = self._make_elem_with_children(4)
    del e[1::2]
    self.assertEqual(self._subelem_tags(e), ['a0', 'a2'])
    e = self._make_elem_with_children(2)
    del e[::2]
    self.assertEqual(self._subelem_tags(e), ['a1'])
