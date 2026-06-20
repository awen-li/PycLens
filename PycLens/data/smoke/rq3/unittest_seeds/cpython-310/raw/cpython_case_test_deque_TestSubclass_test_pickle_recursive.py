# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestSubclass_test_pickle_recursive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        for d in (Deque('abc'), Deque('abc', 3)):
            d.append(d)
            e = pickle.loads(pickle.dumps(d, proto))
            self.assertNotEqual(id(e), id(d))
            self.assertEqual(type(e), type(d))
            self.assertEqual(e.maxlen, d.maxlen)
            dd = d.pop()
            ee = e.pop()
            self.assertEqual(id(ee), id(e))
            self.assertEqual(e, d)
            d.x = d
            e = pickle.loads(pickle.dumps(d, proto))
            self.assertEqual(id(e.x), id(e))
        for d in (DequeWithBadIter('abc'), DequeWithBadIter('abc', 2)):
            self.assertRaises(TypeError, pickle.dumps, d, proto)
