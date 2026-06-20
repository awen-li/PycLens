# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: PyBytesIOTest_test_relative_seek

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buf = self.buftype('1234567890')
    memio = self.ioclass(buf)
    self.assertEqual(memio.seek(-1, 1), 0)
    self.assertEqual(memio.seek(3, 1), 3)
    self.assertEqual(memio.seek(-4, 1), 0)
    self.assertEqual(memio.seek(-1, 2), 9)
    self.assertEqual(memio.seek(1, 1), 10)
    self.assertEqual(memio.seek(1, 2), 11)
    memio.seek(-3, 2)
    self.assertEqual(memio.read(), buf[-3:])
    memio.seek(0)
    memio.seek(1, 1)
    self.assertEqual(memio.read(), buf[1:])
