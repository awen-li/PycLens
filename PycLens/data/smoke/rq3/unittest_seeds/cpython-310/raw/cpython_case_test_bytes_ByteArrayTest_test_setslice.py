# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_setslice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = bytearray(range(10))
    self.assertEqual(list(b), list(range(10)))
    b[0:5] = bytearray([1, 1, 1, 1, 1])
    self.assertEqual(b, bytearray([1, 1, 1, 1, 1, 5, 6, 7, 8, 9]))
    del b[0:-5]
    self.assertEqual(b, bytearray([5, 6, 7, 8, 9]))
    b[0:0] = bytearray([0, 1, 2, 3, 4])
    self.assertEqual(b, bytearray(range(10)))
    b[-7:-3] = bytearray([100, 101])
    self.assertEqual(b, bytearray([0, 1, 2, 100, 101, 7, 8, 9]))
    b[3:5] = [3, 4, 5, 6]
    self.assertEqual(b, bytearray(range(10)))
    b[3:0] = [42, 42, 42]
    self.assertEqual(b, bytearray([0, 1, 2, 42, 42, 42, 3, 4, 5, 6, 7, 8, 9]))
    b[3:] = b'foo'
    self.assertEqual(b, bytearray([0, 1, 2, 102, 111, 111]))
    b[:3] = memoryview(b'foo')
    self.assertEqual(b, bytearray([102, 111, 111, 102, 111, 111]))
    b[3:4] = []
    self.assertEqual(b, bytearray([102, 111, 111, 111, 111]))
    for elem in [5, -5, 0, int(1e+21), 'str', 2.3, ['a', 'b'], [b'a', b'b'], [[]]]:
        with self.assertRaises(TypeError):
            b[3:4] = elem
    for elem in [[254, 255, 256], [-256, 9000]]:
        with self.assertRaises(ValueError):
            b[3:4] = elem
