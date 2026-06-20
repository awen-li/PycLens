# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_init_alloc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = bytearray()

    def g():
        for i in range(1, 100):
            yield i
            a = list(b)
            self.assertEqual(a, list(range(1, len(a) + 1)))
            self.assertEqual(len(b), len(a))
            self.assertLessEqual(len(b), i)
            alloc = b.__alloc__()
            self.assertGreater(alloc, len(b))
    b.__init__(g())
    self.assertEqual(list(b), list(range(1, 100)))
    self.assertEqual(len(b), 99)
    alloc = b.__alloc__()
    self.assertGreater(alloc, len(b))
