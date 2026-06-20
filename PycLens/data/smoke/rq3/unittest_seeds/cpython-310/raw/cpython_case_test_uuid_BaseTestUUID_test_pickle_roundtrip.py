# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uuid.py
# case: BaseTestUUID_test_pickle_roundtrip

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(actual, expected):
        self.assertEqual(actual, expected)
        self.assertEqual(actual.is_safe, expected.is_safe)
    with support.swap_item(sys.modules, 'uuid', self.uuid):
        for is_safe in self.uuid.SafeUUID:
            u = self.uuid.UUID('d82579ce6642a0de7ddf490a7aec7aa5', is_safe=is_safe)
            check(copy.copy(u), u)
            check(copy.deepcopy(u), u)
            for proto in range(pickle.HIGHEST_PROTOCOL + 1):
                with self.subTest(protocol=proto):
                    check(pickle.loads(pickle.dumps(u, proto)), u)
