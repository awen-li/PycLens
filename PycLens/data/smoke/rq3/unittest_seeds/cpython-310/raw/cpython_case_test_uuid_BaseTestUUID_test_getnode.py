# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uuid.py
# case: BaseTestUUID_test_getnode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    node1 = self.uuid.getnode()
    self.assertTrue(0 < node1 < 1 << 48, '%012x' % node1)
    node2 = self.uuid.getnode()
    self.assertEqual(node1, node2, '%012x != %012x' % (node1, node2))
