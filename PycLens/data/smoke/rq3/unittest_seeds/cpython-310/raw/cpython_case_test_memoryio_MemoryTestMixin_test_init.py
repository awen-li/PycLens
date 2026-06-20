# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: MemoryTestMixin_test_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buf = self.buftype('1234567890')
    memio = self.ioclass(buf)
    self.assertEqual(memio.getvalue(), buf)
    memio = self.ioclass(None)
    self.assertEqual(memio.getvalue(), self.EOF)
    memio.__init__(buf * 2)
    self.assertEqual(memio.getvalue(), buf * 2)
    memio.__init__(buf)
    self.assertEqual(memio.getvalue(), buf)
    self.assertRaises(TypeError, memio.__init__, [])
