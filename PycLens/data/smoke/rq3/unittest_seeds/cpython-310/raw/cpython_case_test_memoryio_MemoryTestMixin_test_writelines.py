# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: MemoryTestMixin_test_writelines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buf = self.buftype('1234567890')
    memio = self.ioclass()
    self.assertEqual(memio.writelines([buf] * 100), None)
    self.assertEqual(memio.getvalue(), buf * 100)
    memio.writelines([])
    self.assertEqual(memio.getvalue(), buf * 100)
    memio = self.ioclass()
    self.assertRaises(TypeError, memio.writelines, [buf] + [1])
    self.assertEqual(memio.getvalue(), buf)
    self.assertRaises(TypeError, memio.writelines, None)
    memio.close()
    self.assertRaises(ValueError, memio.writelines, [])
