# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_recursive_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.AllowPickle():
        f = self.partial(capture)
        f.__setstate__((f, (), {}, {}))
        try:
            for proto in range(pickle.HIGHEST_PROTOCOL + 1):
                with self.assertRaises(RecursionError):
                    pickle.dumps(f, proto)
        finally:
            f.__setstate__((capture, (), {}, {}))
        f = self.partial(capture)
        f.__setstate__((capture, (f,), {}, {}))
        try:
            for proto in range(pickle.HIGHEST_PROTOCOL + 1):
                f_copy = pickle.loads(pickle.dumps(f, proto))
                try:
                    self.assertIs(f_copy.args[0], f_copy)
                finally:
                    f_copy.__setstate__((capture, (), {}, {}))
        finally:
            f.__setstate__((capture, (), {}, {}))
        f = self.partial(capture)
        f.__setstate__((capture, (), {'a': f}, {}))
        try:
            for proto in range(pickle.HIGHEST_PROTOCOL + 1):
                f_copy = pickle.loads(pickle.dumps(f, proto))
                try:
                    self.assertIs(f_copy.keywords['a'], f_copy)
                finally:
                    f_copy.__setstate__((capture, (), {}, {}))
        finally:
            f.__setstate__((capture, (), {}, {}))
