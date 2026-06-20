# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uuid.py
# case: BaseTestUUID_test_uuid1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    equal = self.assertEqual
    for u in [self.uuid.uuid1() for i in range(10)]:
        equal(u.variant, self.uuid.RFC_4122)
        equal(u.version, 1)
        self.assertIn(u.is_safe, {self.uuid.SafeUUID.safe, self.uuid.SafeUUID.unsafe, self.uuid.SafeUUID.unknown})
    uuids = {}
    for u in [self.uuid.uuid1() for i in range(1000)]:
        uuids[u] = 1
    equal(len(uuids.keys()), 1000)
    u = self.uuid.uuid1(0)
    equal(u.node, 0)
    u = self.uuid.uuid1(20015998343868)
    equal(u.node, 20015998343868)
    u = self.uuid.uuid1(281474976710655)
    equal(u.node, 281474976710655)
    u = self.uuid.uuid1(20015998343868, 0)
    equal(u.node, 20015998343868)
    equal((u.clock_seq_hi_variant & 63) << 8 | u.clock_seq_low, 0)
    u = self.uuid.uuid1(20015998343868, 4660)
    equal(u.node, 20015998343868)
    equal((u.clock_seq_hi_variant & 63) << 8 | u.clock_seq_low, 4660)
    u = self.uuid.uuid1(20015998343868, 16383)
    equal(u.node, 20015998343868)
    equal((u.clock_seq_hi_variant & 63) << 8 | u.clock_seq_low, 16383)
