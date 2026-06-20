# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_dom_minicompat.py
# case: EmptyNodeListTestCase_test_emptynodelist___radd__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    node_list = [1, 2] + EmptyNodeList()
    self.assertEqual(node_list, [1, 2])
