# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementSlicingTest_test_getslice_single_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = self._make_elem_with_children(10)
    self.assertEqual(e[1].tag, 'a1')
    self.assertEqual(e[-2].tag, 'a8')
    self.assertRaises(IndexError, lambda : e[12])
    self.assertRaises(IndexError, lambda : e[-12])
