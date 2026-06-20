# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericalias.py
# case: BaseTest_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    alias = GenericAlias(list, T)
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        s = pickle.dumps(alias, proto)
        loaded = pickle.loads(s)
        self.assertEqual(loaded.__origin__, alias.__origin__)
        self.assertEqual(loaded.__args__, alias.__args__)
        self.assertEqual(loaded.__parameters__, alias.__parameters__)
