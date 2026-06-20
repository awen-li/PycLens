# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_list.py
# case: ListTest_test_iterator_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    orig = self.type2test([4, 5, 6, 7])
    data = [10, 11, 12, 13, 14, 15]
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        itorig = iter(orig)
        d = pickle.dumps((itorig, orig), proto)
        (it, a) = pickle.loads(d)
        a[:] = data
        self.assertEqual(type(it), type(itorig))
        self.assertEqual(list(it), data)
        next(itorig)
        d = pickle.dumps((itorig, orig), proto)
        (it, a) = pickle.loads(d)
        a[:] = data
        self.assertEqual(type(it), type(itorig))
        self.assertEqual(list(it), data[1:])
        for i in range(1, len(orig)):
            next(itorig)
        d = pickle.dumps((itorig, orig), proto)
        (it, a) = pickle.loads(d)
        a[:] = data
        self.assertEqual(type(it), type(itorig))
        self.assertEqual(list(it), data[len(orig):])
        self.assertRaises(StopIteration, next, itorig)
        d = pickle.dumps((itorig, orig), proto)
        (it, a) = pickle.loads(d)
        a[:] = data
        self.assertEqual(list(it), [])
