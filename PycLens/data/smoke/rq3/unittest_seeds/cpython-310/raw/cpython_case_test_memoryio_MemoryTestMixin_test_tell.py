# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: MemoryTestMixin_test_tell

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buf = self.buftype('1234567890')
    memio = self.ioclass(buf)
    self.assertEqual(memio.tell(), 0)
    memio.seek(5)
    self.assertEqual(memio.tell(), 5)
    memio.seek(10000)
    self.assertEqual(memio.tell(), 10000)
    memio.close()
    self.assertRaises(ValueError, memio.tell)
