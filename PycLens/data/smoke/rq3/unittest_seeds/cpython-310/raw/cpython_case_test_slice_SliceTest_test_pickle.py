# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_slice.py
# case: SliceTest_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import pickle
    s = slice(10, 20, 3)
    for protocol in range(pickle.HIGHEST_PROTOCOL + 1):
        t = loads(dumps(s, protocol))
        self.assertEqual(s, t)
        self.assertEqual(s.indices(15), t.indices(15))
        self.assertNotEqual(id(s), id(t))
