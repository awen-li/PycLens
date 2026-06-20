# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: PyBytesIOTest_test_bytes_array

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buf = b'1234567890'
    import array
    a = array.array('b', list(buf))
    memio = self.ioclass(a)
    self.assertEqual(memio.getvalue(), buf)
    self.assertEqual(memio.write(a), 10)
    self.assertEqual(memio.getvalue(), buf)
