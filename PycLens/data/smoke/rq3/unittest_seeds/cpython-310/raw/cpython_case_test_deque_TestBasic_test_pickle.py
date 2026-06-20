# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for d in (deque(range(200)), deque(range(200), 100)):
        for i in range(pickle.HIGHEST_PROTOCOL + 1):
            s = pickle.dumps(d, i)
            e = pickle.loads(s)
            self.assertNotEqual(id(e), id(d))
            self.assertEqual(list(e), list(d))
            self.assertEqual(e.maxlen, d.maxlen)
