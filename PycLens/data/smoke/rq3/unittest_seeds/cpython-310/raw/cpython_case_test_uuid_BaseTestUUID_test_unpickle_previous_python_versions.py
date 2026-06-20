# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uuid.py
# case: BaseTestUUID_test_unpickle_previous_python_versions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(actual, expected):
        self.assertEqual(actual, expected)
        self.assertEqual(actual.is_safe, expected.is_safe)
    pickled_uuids = [b"ccopy_reg\n_reconstructor\n(cuuid\nUUID\nc__builtin__\nobject\nNtR(dS'int'\nL287307832597519156748809049798316161701L\nsb.", b'ccopy_reg\n_reconstructor\n(cuuid\nUUID\nc__builtin__\nobject\nNtR}U\x03intL287307832597519156748809049798316161701L\nsb.', b'\x80\x02cuuid\nUUID\n)\x81}U\x03int\x8a\x11\xa5z\xecz\nI\xdf}\xde\xa0Bf\xcey%\xd8\x00sb.', b'ccopy_reg\n_reconstructor\n(cuuid\nUUID\nc__builtin__\nobject\nNtR(dVint\nL287307832597519156748809049798316161701L\nsb.', b'ccopy_reg\n_reconstructor\n(cuuid\nUUID\nc__builtin__\nobject\nNtR}X\x03\x00\x00\x00intL287307832597519156748809049798316161701L\nsb.', b'\x80\x02cuuid\nUUID\n)\x81}X\x03\x00\x00\x00int\x8a\x11\xa5z\xecz\nI\xdf}\xde\xa0Bf\xcey%\xd8\x00sb.', b'\x80\x03cuuid\nUUID\n)\x81}X\x03\x00\x00\x00int\x8a\x11\xa5z\xecz\nI\xdf}\xde\xa0Bf\xcey%\xd8\x00sb.', b'\x80\x04\x95+\x00\x00\x00\x00\x00\x00\x00\x8c\x04uuid\x8c\x04UUID\x93)\x81}\x8c\x03int\x8a\x11\xa5z\xecz\nI\xdf}\xde\xa0Bf\xcey%\xd8\x00sb.', b'ccopy_reg\n_reconstructor\n(cuuid\nUUID\nc__builtin__\nobject\nNtR(dVint\nL287307832597519156748809049798316161701L\nsVis_safe\ncuuid\nSafeUUID\n(NtRsb.', b'ccopy_reg\n_reconstructor\n(cuuid\nUUID\nc__builtin__\nobject\nNtR}(X\x03\x00\x00\x00intL287307832597519156748809049798316161701L\nX\x07\x00\x00\x00is_safecuuid\nSafeUUID\n(NtRub.', b'\x80\x02cuuid\nUUID\n)\x81}(X\x03\x00\x00\x00int\x8a\x11\xa5z\xecz\nI\xdf}\xde\xa0Bf\xcey%\xd8\x00X\x07\x00\x00\x00is_safecuuid\nSafeUUID\nN\x85Rub.', b'\x80\x03cuuid\nUUID\n)\x81}(X\x03\x00\x00\x00int\x8a\x11\xa5z\xecz\nI\xdf}\xde\xa0Bf\xcey%\xd8\x00X\x07\x00\x00\x00is_safecuuid\nSafeUUID\nN\x85Rub.', b'\x80\x04\x95F\x00\x00\x00\x00\x00\x00\x00\x8c\x04uuid\x94\x8c\x04UUID\x93)\x81}(\x8c\x03int\x8a\x11\xa5z\xecz\nI\xdf}\xde\xa0Bf\xcey%\xd8\x00\x8c\x07is_safeh\x00\x8c\x08SafeUUID\x93N\x85Rub.']
    pickled_uuids_safe = [b'ccopy_reg\n_reconstructor\n(cuuid\nUUID\nc__builtin__\nobject\nNtR(dVint\nL287307832597519156748809049798316161701L\nsVis_safe\ncuuid\nSafeUUID\n(I0\ntRsb.', b'ccopy_reg\n_reconstructor\n(cuuid\nUUID\nc__builtin__\nobject\nNtR}(X\x03\x00\x00\x00intL287307832597519156748809049798316161701L\nX\x07\x00\x00\x00is_safecuuid\nSafeUUID\n(K\x00tRub.', b'\x80\x02cuuid\nUUID\n)\x81}(X\x03\x00\x00\x00int\x8a\x11\xa5z\xecz\nI\xdf}\xde\xa0Bf\xcey%\xd8\x00X\x07\x00\x00\x00is_safecuuid\nSafeUUID\nK\x00\x85Rub.', b'\x80\x03cuuid\nUUID\n)\x81}(X\x03\x00\x00\x00int\x8a\x11\xa5z\xecz\nI\xdf}\xde\xa0Bf\xcey%\xd8\x00X\x07\x00\x00\x00is_safecuuid\nSafeUUID\nK\x00\x85Rub.', b'\x80\x04\x95G\x00\x00\x00\x00\x00\x00\x00\x8c\x04uuid\x94\x8c\x04UUID\x93)\x81}(\x8c\x03int\x8a\x11\xa5z\xecz\nI\xdf}\xde\xa0Bf\xcey%\xd8\x00\x8c\x07is_safeh\x00\x8c\x08SafeUUID\x93K\x00\x85Rub.']
    pickled_uuids_unsafe = [b'ccopy_reg\n_reconstructor\n(cuuid\nUUID\nc__builtin__\nobject\nNtR(dVint\nL287307832597519156748809049798316161701L\nsVis_safe\ncuuid\nSafeUUID\n(I-1\ntRsb.', b'ccopy_reg\n_reconstructor\n(cuuid\nUUID\nc__builtin__\nobject\nNtR}(X\x03\x00\x00\x00intL287307832597519156748809049798316161701L\nX\x07\x00\x00\x00is_safecuuid\nSafeUUID\n(J\xff\xff\xff\xfftRub.', b'\x80\x02cuuid\nUUID\n)\x81}(X\x03\x00\x00\x00int\x8a\x11\xa5z\xecz\nI\xdf}\xde\xa0Bf\xcey%\xd8\x00X\x07\x00\x00\x00is_safecuuid\nSafeUUID\nJ\xff\xff\xff\xff\x85Rub.', b'\x80\x03cuuid\nUUID\n)\x81}(X\x03\x00\x00\x00int\x8a\x11\xa5z\xecz\nI\xdf}\xde\xa0Bf\xcey%\xd8\x00X\x07\x00\x00\x00is_safecuuid\nSafeUUID\nJ\xff\xff\xff\xff\x85Rub.', b'\x80\x04\x95J\x00\x00\x00\x00\x00\x00\x00\x8c\x04uuid\x94\x8c\x04UUID\x93)\x81}(\x8c\x03int\x8a\x11\xa5z\xecz\nI\xdf}\xde\xa0Bf\xcey%\xd8\x00\x8c\x07is_safeh\x00\x8c\x08SafeUUID\x93J\xff\xff\xff\xff\x85Rub.']
    u = self.uuid.UUID('d82579ce6642a0de7ddf490a7aec7aa5')
    u_safe = self.uuid.UUID('d82579ce6642a0de7ddf490a7aec7aa5', is_safe=self.uuid.SafeUUID.safe)
    u_unsafe = self.uuid.UUID('d82579ce6642a0de7ddf490a7aec7aa5', is_safe=self.uuid.SafeUUID.unsafe)
    with support.swap_item(sys.modules, 'uuid', self.uuid):
        for pickled in pickled_uuids:
            check(pickle.loads(pickled), u)
        for pickled in pickled_uuids_safe:
            check(pickle.loads(pickled), u_safe)
        for pickled in pickled_uuids_unsafe:
            check(pickle.loads(pickled), u_unsafe)
