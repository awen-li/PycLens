# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: PyBytesIOTest_test_read1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buf = self.buftype('1234567890')
    self.assertEqual(self.ioclass(buf).read1(), buf)
    self.assertEqual(self.ioclass(buf).read1(-1), buf)
