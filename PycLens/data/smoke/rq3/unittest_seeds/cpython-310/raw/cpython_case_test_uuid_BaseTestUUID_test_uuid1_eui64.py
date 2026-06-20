# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uuid.py
# case: BaseTestUUID_test_uuid1_eui64

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    too_large_getter = lambda : 1 << 48
    with mock.patch.multiple(self.uuid, _node=None, _GETTERS=[too_large_getter]):
        node = self.uuid.getnode()
    self.assertTrue(0 < node < 1 << 48, '%012x' % node)
    try:
        self.uuid.uuid1(node=node)
    except ValueError:
        self.fail('uuid1 was given an invalid node ID')
