# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_copied

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = bytearray(b'abc')
    self.assertIsNot(b, b.replace(b'abc', b'cde', 0))
    t = bytearray([i for i in range(256)])
    x = bytearray(b'')
    self.assertIsNot(x, x.translate(t))
