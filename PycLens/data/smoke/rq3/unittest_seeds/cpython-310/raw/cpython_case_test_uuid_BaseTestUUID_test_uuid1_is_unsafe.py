# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uuid.py
# case: BaseTestUUID_test_uuid1_is_unsafe

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.mock_generate_time_safe(-1):
        u = self.uuid.uuid1()
        self.assertEqual(u.is_safe, self.uuid.SafeUUID.unsafe)
