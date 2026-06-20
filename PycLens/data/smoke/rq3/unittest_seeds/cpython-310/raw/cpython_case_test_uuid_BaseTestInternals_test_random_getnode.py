# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uuid.py
# case: BaseTestInternals_test_random_getnode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    node = self.uuid._random_getnode()
    self.assertTrue(node & 1 << 40, '%012x' % node)
    self.check_node(node)
    node2 = self.uuid._random_getnode()
    self.assertNotEqual(node2, node, '%012x' % node)
