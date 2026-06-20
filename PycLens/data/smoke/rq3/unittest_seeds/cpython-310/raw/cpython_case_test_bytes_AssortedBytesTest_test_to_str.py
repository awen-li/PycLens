# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: AssortedBytesTest_test_to_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(str(b''), "b''")
    self.assertEqual(str(b'x'), "b'x'")
    self.assertEqual(str(b'\x80'), "b'\\x80'")
    self.assertEqual(str(bytearray(b'')), "bytearray(b'')")
    self.assertEqual(str(bytearray(b'x')), "bytearray(b'x')")
    self.assertEqual(str(bytearray(b'\x80')), "bytearray(b'\\x80')")
