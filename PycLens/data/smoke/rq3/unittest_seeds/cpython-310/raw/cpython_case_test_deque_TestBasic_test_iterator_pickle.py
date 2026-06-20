# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_iterator_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    orig = deque(range(200))
    data = [i * 1.01 for i in orig]
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        itorg = iter(orig)
        dump = pickle.dumps((itorg, orig), proto)
        (it, d) = pickle.loads(dump)
        for (i, x) in enumerate(data):
            d[i] = x
        self.assertEqual(type(it), type(itorg))
        self.assertEqual(list(it), data)
        next(itorg)
        dump = pickle.dumps((itorg, orig), proto)
        (it, d) = pickle.loads(dump)
        for (i, x) in enumerate(data):
            d[i] = x
        self.assertEqual(type(it), type(itorg))
        self.assertEqual(list(it), data[1:])
        for i in range(1, len(data)):
            next(itorg)
        dump = pickle.dumps((itorg, orig), proto)
        (it, d) = pickle.loads(dump)
        for (i, x) in enumerate(data):
            d[i] = x
        self.assertEqual(type(it), type(itorg))
        self.assertEqual(list(it), [])
        self.assertRaises(StopIteration, next, itorg)
        dump = pickle.dumps((itorg, orig), proto)
        (it, d) = pickle.loads(dump)
        for (i, x) in enumerate(data):
            d[i] = x
        self.assertEqual(type(it), type(itorg))
        self.assertEqual(list(it), [])
