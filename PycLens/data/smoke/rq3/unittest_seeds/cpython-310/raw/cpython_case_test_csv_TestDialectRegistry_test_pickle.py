# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: TestDialectRegistry_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for name in csv.list_dialects():
        dialect = csv.get_dialect(name)
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            self.assertRaises(TypeError, pickle.dumps, dialect, proto)
