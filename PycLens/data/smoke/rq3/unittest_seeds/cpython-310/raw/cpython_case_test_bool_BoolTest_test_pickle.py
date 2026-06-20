# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bool.py
# case: BoolTest_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import pickle
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        self.assertIs(pickle.loads(pickle.dumps(True, proto)), True)
        self.assertIs(pickle.loads(pickle.dumps(False, proto)), False)
