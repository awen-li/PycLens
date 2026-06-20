# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: AssortedBytesTest_test_from_bytearray

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sample = bytes(b'Hello world\n\x80\x81\xfe\xff')
    buf = memoryview(sample)
    b = bytearray(buf)
    self.assertEqual(b, bytearray(sample))
