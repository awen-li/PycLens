# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_dom_minicompat.py
# case: EmptyNodeListTestCase_test_emptynodelist_length

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    node_list = EmptyNodeList()
    self.assertEqual(node_list.length, 0)
    with self.assertRaises(xml.dom.NoModificationAllowedErr):
        node_list.length = 111
