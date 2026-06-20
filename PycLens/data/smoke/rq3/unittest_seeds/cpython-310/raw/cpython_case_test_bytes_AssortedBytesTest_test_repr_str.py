# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: AssortedBytesTest_test_repr_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for f in (str, repr):
        self.assertEqual(f(bytearray()), "bytearray(b'')")
        self.assertEqual(f(bytearray([0])), "bytearray(b'\\x00')")
        self.assertEqual(f(bytearray([0, 1, 254, 255])), "bytearray(b'\\x00\\x01\\xfe\\xff')")
        self.assertEqual(f(b'abc'), "b'abc'")
        self.assertEqual(f(b"'"), 'b"\'"')
        self.assertEqual(f(b'\'"'), 'b\'\\\'"\'')
