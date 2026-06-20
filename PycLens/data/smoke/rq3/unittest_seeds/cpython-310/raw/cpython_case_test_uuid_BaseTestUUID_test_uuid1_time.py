# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uuid.py
# case: BaseTestUUID_test_uuid1_time

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with mock.patch.object(self.uuid, '_has_uuid_generate_time_safe', False), mock.patch.object(self.uuid, '_generate_time_safe', None), mock.patch.object(self.uuid, '_last_timestamp', None), mock.patch.object(self.uuid, 'getnode', return_value=93328246233727), mock.patch('time.time_ns', return_value=1545052026752910643), mock.patch('random.getrandbits', return_value=5317):
        u = self.uuid.uuid1()
        self.assertEqual(u, self.uuid.UUID('a7a55b92-01fc-11e9-94c5-54e1acf6da7f'))
    with mock.patch.object(self.uuid, '_has_uuid_generate_time_safe', False), mock.patch.object(self.uuid, '_generate_time_safe', None), mock.patch.object(self.uuid, '_last_timestamp', None), mock.patch('time.time_ns', return_value=1545052026752910643):
        u = self.uuid.uuid1(node=93328246233727, clock_seq=5317)
        self.assertEqual(u, self.uuid.UUID('a7a55b92-01fc-11e9-94c5-54e1acf6da7f'))
