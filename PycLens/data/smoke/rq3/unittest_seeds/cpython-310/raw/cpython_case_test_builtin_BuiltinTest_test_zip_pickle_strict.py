# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_zip_pickle_strict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = (1, 2, 3)
    b = (4, 5, 6)
    t = [(1, 4), (2, 5), (3, 6)]
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        z1 = zip(a, b, strict=True)
        self.check_iter_pickle(z1, t, proto)
