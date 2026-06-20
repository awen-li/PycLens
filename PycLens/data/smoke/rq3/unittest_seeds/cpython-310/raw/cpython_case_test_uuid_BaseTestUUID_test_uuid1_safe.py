# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uuid.py
# case: BaseTestUUID_test_uuid1_safe

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not self.uuid._has_uuid_generate_time_safe:
        self.skipTest('requires uuid_generate_time_safe(3)')
    u = self.uuid.uuid1()
    self.assertNotEqual(u.is_safe, self.uuid.SafeUUID.unknown)
