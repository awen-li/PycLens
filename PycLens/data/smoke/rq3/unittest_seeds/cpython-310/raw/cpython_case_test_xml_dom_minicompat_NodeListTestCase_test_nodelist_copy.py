# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_dom_minicompat.py
# case: NodeListTestCase_test_nodelist_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    node_list = NodeList()
    copied = copy.copy(node_list)
    self.assertIsNot(copied, node_list)
    self.assertEqual(copied, node_list)
    node_list.append([1])
    node_list.append([2])
    copied = copy.copy(node_list)
    self.assertIsNot(copied, node_list)
    self.assertEqual(copied, node_list)
    for (x, y) in zip(copied, node_list):
        self.assertIs(x, y)
