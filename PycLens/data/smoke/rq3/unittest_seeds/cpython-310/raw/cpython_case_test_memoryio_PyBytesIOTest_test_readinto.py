# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: PyBytesIOTest_test_readinto

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buf = self.buftype('1234567890')
    memio = self.ioclass(buf)
    b = bytearray(b'hello')
    self.assertEqual(memio.readinto(b), 5)
    self.assertEqual(b, b'12345')
    self.assertEqual(memio.readinto(b), 5)
    self.assertEqual(b, b'67890')
    self.assertEqual(memio.readinto(b), 0)
    self.assertEqual(b, b'67890')
    b = bytearray(b'hello world')
    memio.seek(0)
    self.assertEqual(memio.readinto(b), 10)
    self.assertEqual(b, b'1234567890d')
    b = bytearray(b'')
    memio.seek(0)
    self.assertEqual(memio.readinto(b), 0)
    self.assertEqual(b, b'')
    self.assertRaises(TypeError, memio.readinto, '')
    import array
    a = array.array('b', b'hello world')
    memio = self.ioclass(buf)
    memio.readinto(a)
    self.assertEqual(a.tobytes(), b'1234567890d')
    memio.close()
    self.assertRaises(ValueError, memio.readinto, b)
    memio = self.ioclass(b'123')
    b = bytearray()
    memio.seek(42)
    memio.readinto(b)
    self.assertEqual(b, b'')
