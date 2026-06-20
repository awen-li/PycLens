# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: MemoryTestMixin_test_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buf = self.buftype('hello world\n')
    memio = self.ioclass(buf)
    self.write_ops(memio, self.buftype)
    self.assertEqual(memio.getvalue(), buf)
    memio = self.ioclass()
    self.write_ops(memio, self.buftype)
    self.assertEqual(memio.getvalue(), buf)
    self.assertRaises(TypeError, memio.write, None)
    memio.close()
    self.assertRaises(ValueError, memio.write, self.buftype(''))
