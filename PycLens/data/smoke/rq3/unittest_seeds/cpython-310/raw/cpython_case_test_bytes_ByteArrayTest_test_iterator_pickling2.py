# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_iterator_pickling2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    orig = bytearray(b'abc')
    data = list(b'qwerty')
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        itorig = iter(orig)
        d = pickle.dumps((itorig, orig), proto)
        (it, b) = pickle.loads(d)
        b[:] = data
        self.assertEqual(type(it), type(itorig))
        self.assertEqual(list(it), data)
        next(itorig)
        d = pickle.dumps((itorig, orig), proto)
        (it, b) = pickle.loads(d)
        b[:] = data
        self.assertEqual(type(it), type(itorig))
        self.assertEqual(list(it), data[1:])
        for i in range(1, len(orig)):
            next(itorig)
        d = pickle.dumps((itorig, orig), proto)
        (it, b) = pickle.loads(d)
        b[:] = data
        self.assertEqual(type(it), type(itorig))
        self.assertEqual(list(it), data[len(orig):])
        self.assertRaises(StopIteration, next, itorig)
        d = pickle.dumps((itorig, orig), proto)
        (it, b) = pickle.loads(d)
        b[:] = data
        self.assertEqual(list(it), [])
