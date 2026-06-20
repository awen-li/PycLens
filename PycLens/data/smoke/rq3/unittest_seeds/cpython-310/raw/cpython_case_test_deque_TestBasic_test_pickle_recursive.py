# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_pickle_recursive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for d in (deque('abc'), deque('abc', 3)):
        d.append(d)
        for i in range(pickle.HIGHEST_PROTOCOL + 1):
            e = pickle.loads(pickle.dumps(d, i))
            self.assertNotEqual(id(e), id(d))
            self.assertEqual(id(e[-1]), id(e))
            self.assertEqual(e.maxlen, d.maxlen)
