# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: UnionTests_test_union_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    orig = list[T] | int
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        s = pickle.dumps(orig, proto)
        loaded = pickle.loads(s)
        self.assertEqual(loaded, orig)
        self.assertEqual(loaded.__args__, orig.__args__)
        self.assertEqual(loaded.__parameters__, orig.__parameters__)
