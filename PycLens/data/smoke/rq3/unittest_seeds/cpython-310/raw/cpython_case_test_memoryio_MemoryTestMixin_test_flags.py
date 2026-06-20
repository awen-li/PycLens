# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: MemoryTestMixin_test_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    memio = self.ioclass()
    self.assertEqual(memio.writable(), True)
    self.assertEqual(memio.readable(), True)
    self.assertEqual(memio.seekable(), True)
    self.assertEqual(memio.isatty(), False)
    self.assertEqual(memio.closed, False)
    memio.close()
    self.assertRaises(ValueError, memio.writable)
    self.assertRaises(ValueError, memio.readable)
    self.assertRaises(ValueError, memio.seekable)
    self.assertRaises(ValueError, memio.isatty)
    self.assertEqual(memio.closed, True)
