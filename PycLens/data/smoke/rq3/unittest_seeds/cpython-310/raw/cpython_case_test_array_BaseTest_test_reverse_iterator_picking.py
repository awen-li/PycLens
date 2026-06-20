# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_reverse_iterator_picking

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    orig = array.array(self.typecode, self.example)
    data = list(orig)
    data2 = [self.outside] + data
    rev_data = data[len(data) - 2::-1] + [self.outside]
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        itorig = reversed(orig)
        d = pickle.dumps((itorig, orig), proto)
        (it, a) = pickle.loads(d)
        a.insert(0, self.outside)
        self.assertEqual(type(it), type(itorig))
        self.assertEqual(list(it), rev_data)
        self.assertEqual(list(a), data2)
        next(itorig)
        d = pickle.dumps((itorig, orig), proto)
        (it, a) = pickle.loads(d)
        a.insert(0, self.outside)
        self.assertEqual(type(it), type(itorig))
        self.assertEqual(list(it), rev_data[1:])
        self.assertEqual(list(a), data2)
        for i in range(1, len(data)):
            next(itorig)
        d = pickle.dumps((itorig, orig), proto)
        (it, a) = pickle.loads(d)
        a.insert(0, self.outside)
        self.assertEqual(type(it), type(itorig))
        self.assertEqual(list(it), [])
        self.assertEqual(list(a), data2)
        self.assertRaises(StopIteration, next, itorig)
        d = pickle.dumps((itorig, orig), proto)
        (it, a) = pickle.loads(d)
        a.insert(0, self.outside)
        self.assertEqual(list(it), [])
        self.assertEqual(list(a), data2)
