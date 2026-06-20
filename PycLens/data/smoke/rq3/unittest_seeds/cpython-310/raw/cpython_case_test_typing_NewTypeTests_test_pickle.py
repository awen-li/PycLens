# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: NewTypeTests_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    UserAge = NewType('UserAge', float)
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        with self.subTest(proto=proto):
            pickled = pickle.dumps(UserId, proto)
            loaded = pickle.loads(pickled)
            self.assertIs(loaded, UserId)
            pickled = pickle.dumps(self.UserName, proto)
            loaded = pickle.loads(pickled)
            self.assertIs(loaded, self.UserName)
            with self.assertRaises(pickle.PicklingError):
                pickle.dumps(UserAge, proto)
