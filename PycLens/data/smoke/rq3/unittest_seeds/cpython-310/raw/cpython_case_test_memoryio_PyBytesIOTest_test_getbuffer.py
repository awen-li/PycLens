# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: PyBytesIOTest_test_getbuffer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    memio = self.ioclass(b'1234567890')
    buf = memio.getbuffer()
    self.assertEqual(bytes(buf), b'1234567890')
    memio.seek(5)
    buf = memio.getbuffer()
    self.assertEqual(bytes(buf), b'1234567890')
    self.assertRaises(BufferError, memio.write, b'x' * 100)
    self.assertRaises(BufferError, memio.truncate)
    self.assertRaises(BufferError, memio.close)
    self.assertFalse(memio.closed)
    buf[3:6] = b'abc'
    self.assertEqual(bytes(buf), b'123abc7890')
    self.assertEqual(memio.getvalue(), b'123abc7890')
    del buf
    support.gc_collect()
    memio.truncate()
    memio.close()
    self.assertRaises(ValueError, memio.getbuffer)
