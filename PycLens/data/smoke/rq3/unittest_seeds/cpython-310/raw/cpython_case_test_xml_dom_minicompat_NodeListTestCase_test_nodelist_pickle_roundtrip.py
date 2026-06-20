# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_dom_minicompat.py
# case: NodeListTestCase_test_nodelist_pickle_roundtrip

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        node_list = NodeList()
        pickled = pickle.dumps(node_list, proto)
        unpickled = pickle.loads(pickled)
        self.assertIsNot(unpickled, node_list)
        self.assertEqual(unpickled, node_list)
        node_list.append(1)
        node_list.append(2)
        pickled = pickle.dumps(node_list, proto)
        unpickled = pickle.loads(pickled)
        self.assertIsNot(unpickled, node_list)
        self.assertEqual(unpickled, node_list)
