# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cls = self.__class__
    for f in (cls.cached_func[0], cls.cached_meth, cls.cached_staticmeth):
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            with self.subTest(proto=proto, func=f):
                f_copy = pickle.loads(pickle.dumps(f, proto))
                self.assertIs(f_copy, f)
