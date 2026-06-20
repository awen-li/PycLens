# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_reverse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = bytearray(b'hello')
    self.assertEqual(b.reverse(), None)
    self.assertEqual(b, b'olleh')
    b = bytearray(b'hello1')
    b.reverse()
    self.assertEqual(b, b'1olleh')
    b = bytearray()
    b.reverse()
    self.assertFalse(b)
