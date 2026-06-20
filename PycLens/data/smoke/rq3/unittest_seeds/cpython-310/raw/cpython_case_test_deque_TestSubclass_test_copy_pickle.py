# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestSubclass_test_copy_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = Deque('abc')
    e = d.__copy__()
    self.assertEqual(type(d), type(e))
    self.assertEqual(list(d), list(e))
    e = Deque(d)
    self.assertEqual(type(d), type(e))
    self.assertEqual(list(d), list(e))
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        s = pickle.dumps(d, proto)
        e = pickle.loads(s)
        self.assertNotEqual(id(d), id(e))
        self.assertEqual(type(d), type(e))
        self.assertEqual(list(d), list(e))
    d = Deque('abcde', maxlen=4)
    e = d.__copy__()
    self.assertEqual(type(d), type(e))
    self.assertEqual(list(d), list(e))
    e = Deque(d)
    self.assertEqual(type(d), type(e))
    self.assertEqual(list(d), list(e))
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        s = pickle.dumps(d, proto)
        e = pickle.loads(s)
        self.assertNotEqual(id(d), id(e))
        self.assertEqual(type(d), type(e))
        self.assertEqual(list(d), list(e))
