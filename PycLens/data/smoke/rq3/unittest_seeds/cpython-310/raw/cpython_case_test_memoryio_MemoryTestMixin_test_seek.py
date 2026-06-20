# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: MemoryTestMixin_test_seek

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buf = self.buftype('1234567890')
    memio = self.ioclass(buf)
    memio.read(5)
    self.assertRaises(ValueError, memio.seek, -1)
    self.assertRaises(ValueError, memio.seek, 1, -1)
    self.assertRaises(ValueError, memio.seek, 1, 3)
    self.assertEqual(memio.seek(0), 0)
    self.assertEqual(memio.seek(0, 0), 0)
    self.assertEqual(memio.read(), buf)
    self.assertEqual(memio.seek(3), 3)
    self.assertEqual(memio.seek(0, 1), 3)
    self.assertEqual(memio.read(), buf[3:])
    self.assertEqual(memio.seek(len(buf)), len(buf))
    self.assertEqual(memio.read(), self.EOF)
    memio.seek(len(buf) + 1)
    self.assertEqual(memio.read(), self.EOF)
    self.assertEqual(memio.seek(0, 2), len(buf))
    self.assertEqual(memio.read(), self.EOF)
    memio.close()
    self.assertRaises(ValueError, memio.seek, 0)
