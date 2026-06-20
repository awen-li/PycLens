# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dictviews.py
# case: DictSetTest_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {1: 10, 'a': 'ABC'}
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        self.assertRaises((TypeError, pickle.PicklingError), pickle.dumps, d.keys(), proto)
        self.assertRaises((TypeError, pickle.PicklingError), pickle.dumps, d.values(), proto)
        self.assertRaises((TypeError, pickle.PicklingError), pickle.dumps, d.items(), proto)
