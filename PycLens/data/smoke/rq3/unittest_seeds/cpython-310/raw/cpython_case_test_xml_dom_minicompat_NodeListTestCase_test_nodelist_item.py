# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_dom_minicompat.py
# case: NodeListTestCase_test_nodelist_item

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    node_list = NodeList()
    self.assertIsNone(node_list.item(0))
    self.assertIsNone(node_list.item(-1))
    with self.assertRaises(IndexError):
        node_list[0]
    with self.assertRaises(IndexError):
        node_list[-1]
    node_list.append(111)
    node_list.append(999)
    self.assertEqual(node_list.item(0), 111)
    self.assertIsNone(node_list.item(-1))
    self.assertEqual(node_list[0], 111)
    self.assertEqual(node_list[-1], 999)
