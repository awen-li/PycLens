# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: MemoryTestMixin_test_truncate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buf = self.buftype('1234567890')
    memio = self.ioclass(buf)
    self.assertRaises(ValueError, memio.truncate, -1)
    self.assertRaises(ValueError, memio.truncate, IntLike(-1))
    memio.seek(6)
    self.assertEqual(memio.truncate(IntLike(8)), 8)
    self.assertEqual(memio.getvalue(), buf[:8])
    self.assertEqual(memio.truncate(), 6)
    self.assertEqual(memio.getvalue(), buf[:6])
    self.assertEqual(memio.truncate(4), 4)
    self.assertEqual(memio.getvalue(), buf[:4])
    self.assertEqual(memio.tell(), 6)
    memio.seek(0, 2)
    memio.write(buf)
    self.assertEqual(memio.getvalue(), buf[:4] + buf)
    pos = memio.tell()
    self.assertEqual(memio.truncate(None), pos)
    self.assertEqual(memio.tell(), pos)
    self.assertRaises(TypeError, memio.truncate, '0')
    memio.close()
    self.assertRaises(ValueError, memio.truncate, 0)
    self.assertRaises(ValueError, memio.truncate, IntLike(0))
