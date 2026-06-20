# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BytesTest_test_bytes_blocking

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class IterationBlocked(list):
        __bytes__ = None
    i = [0, 1, 2, 3]
    self.assertEqual(bytes(i), b'\x00\x01\x02\x03')
    self.assertRaises(TypeError, bytes, IterationBlocked(i))

    class IntBlocked(int):
        __bytes__ = None
    self.assertEqual(bytes(3), b'\x00\x00\x00')
    self.assertRaises(TypeError, bytes, IntBlocked(3))

    class BytesSubclassBlocked(bytes):
        __bytes__ = None
    self.assertEqual(bytes(b'ab'), b'ab')
    self.assertRaises(TypeError, bytes, BytesSubclassBlocked(b'ab'))

    class BufferBlocked(bytearray):
        __bytes__ = None
    (ba, bb) = (bytearray(b'ab'), BufferBlocked(b'ab'))
    self.assertEqual(bytes(ba), b'ab')
    self.assertRaises(TypeError, bytes, bb)
