# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: MemoryTestMixin_test_getvalue

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buf = self.buftype('1234567890')
    memio = self.ioclass(buf)
    self.assertEqual(memio.getvalue(), buf)
    memio.read()
    self.assertEqual(memio.getvalue(), buf)
    self.assertEqual(type(memio.getvalue()), type(buf))
    memio = self.ioclass(buf * 1000)
    self.assertEqual(memio.getvalue()[-3:], self.buftype('890'))
    memio = self.ioclass(buf)
    memio.close()
    self.assertRaises(ValueError, memio.getvalue)
