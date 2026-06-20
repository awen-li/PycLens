# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: PyBytesIOTest_test_unicode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    memio = self.ioclass()
    self.assertRaises(TypeError, self.ioclass, '1234567890')
    self.assertRaises(TypeError, memio.write, '1234567890')
    self.assertRaises(TypeError, memio.writelines, ['1234567890'])
