# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_dom_minicompat.py
# case: NodeListTestCase_test_nodelist___radd__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    node_list = [1, 2] + NodeList([3, 4])
    self.assertEqual(node_list, NodeList([1, 2, 3, 4]))
