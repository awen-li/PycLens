# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: MemoryTestMixin_test_overseek

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buf = self.buftype('1234567890')
    memio = self.ioclass(buf)
    self.assertEqual(memio.seek(len(buf) + 1), 11)
    self.assertEqual(memio.read(), self.EOF)
    self.assertEqual(memio.tell(), 11)
    self.assertEqual(memio.getvalue(), buf)
    memio.write(self.EOF)
    self.assertEqual(memio.getvalue(), buf)
    memio.write(buf)
    self.assertEqual(memio.getvalue(), buf + self.buftype('\x00') + buf)
