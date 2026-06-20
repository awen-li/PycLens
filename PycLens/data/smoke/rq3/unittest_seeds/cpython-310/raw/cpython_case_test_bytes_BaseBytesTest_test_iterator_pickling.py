# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_iterator_pickling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        for b in (b'', b'a', b'abc', b'\xffab\x80', b'\x00\x00\xff\x00\x00'):
            it = itorg = iter(self.type2test(b))
            data = list(self.type2test(b))
            d = pickle.dumps(it, proto)
            it = pickle.loads(d)
            self.assertEqual(type(itorg), type(it))
            self.assertEqual(list(it), data)
            it = pickle.loads(d)
            if not b:
                continue
            next(it)
            d = pickle.dumps(it, proto)
            it = pickle.loads(d)
            self.assertEqual(list(it), data[1:])
