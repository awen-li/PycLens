# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uuid.py
# case: BaseTestUUID_test_uuid4

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    equal = self.assertEqual
    for u in [self.uuid.uuid4() for i in range(10)]:
        equal(u.variant, self.uuid.RFC_4122)
        equal(u.version, 4)
    uuids = {}
    for u in [self.uuid.uuid4() for i in range(1000)]:
        uuids[u] = 1
    equal(len(uuids.keys()), 1000)
