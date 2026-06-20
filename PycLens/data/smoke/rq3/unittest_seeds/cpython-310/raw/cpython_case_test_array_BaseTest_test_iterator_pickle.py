# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_iterator_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    orig = array.array(self.typecode, self.example)
    data = list(orig)
    data2 = data[::-1]
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        itorig = iter(orig)
        d = pickle.dumps((itorig, orig), proto)
        (it, a) = pickle.loads(d)
        a.fromlist(data2)
        self.assertEqual(type(it), type(itorig))
        self.assertEqual(list(it), data + data2)
        next(itorig)
        d = pickle.dumps((itorig, orig), proto)
        (it, a) = pickle.loads(d)
        a.fromlist(data2)
        self.assertEqual(type(it), type(itorig))
        self.assertEqual(list(it), data[1:] + data2)
        for i in range(1, len(data)):
            next(itorig)
        d = pickle.dumps((itorig, orig), proto)
        (it, a) = pickle.loads(d)
        a.fromlist(data2)
        self.assertEqual(type(it), type(itorig))
        self.assertEqual(list(it), data2)
        self.assertRaises(StopIteration, next, itorig)
        d = pickle.dumps((itorig, orig), proto)
        (it, a) = pickle.loads(d)
        a.fromlist(data2)
        self.assertEqual(list(it), [])
