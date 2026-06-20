# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_resize_forbidden

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = bytearray(range(10))
    v = memoryview(b)

    def resize(n):
        b[1:-1] = range(n + 1, 2 * n - 1)
    resize(10)
    orig = b[:]
    self.assertRaises(BufferError, resize, 11)
    self.assertEqual(b, orig)
    self.assertRaises(BufferError, resize, 9)
    self.assertEqual(b, orig)
    self.assertRaises(BufferError, resize, 0)
    self.assertEqual(b, orig)
    self.assertRaises(BufferError, b.pop, 0)
    self.assertEqual(b, orig)
    self.assertRaises(BufferError, b.remove, b[1])
    self.assertEqual(b, orig)

    def delitem():
        del b[1]
    self.assertRaises(BufferError, delitem)
    self.assertEqual(b, orig)

    def delslice():
        b[1:-1:2] = b''
    self.assertRaises(BufferError, delslice)
    self.assertEqual(b, orig)
