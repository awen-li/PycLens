# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: BaseCallableTests_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    global T_pickle, P_pickle
    Callable = self.Callable
    T_pickle = TypeVar('T_pickle')
    P_pickle = ParamSpec('P_pickle')
    samples = [Callable[[int, str], float], Callable[P_pickle, int], Callable[P_pickle, T_pickle], Callable[Concatenate[int, P_pickle], int]]
    for alias in samples:
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            with self.subTest(alias=alias, proto=proto):
                s = pickle.dumps(alias, proto)
                loaded = pickle.loads(s)
                self.assertEqual(alias.__origin__, loaded.__origin__)
                self.assertEqual(alias.__args__, loaded.__args__)
                self.assertEqual(alias.__parameters__, loaded.__parameters__)
    del T_pickle, P_pickle
