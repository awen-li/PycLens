# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: AssortedBytesTest_test_literal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = [(b'Wonderful spam', 'Wonderful spam'), (b'Wonderful spam too', 'Wonderful spam too'), (b'\xaa\x00\x00\x80', 'ª\x00\x00\x80'), (b'\\xaa\\x00\\000\\200', '\\xaa\\x00\\000\\200')]
    for (b, s) in tests:
        self.assertEqual(b, bytearray(s, 'latin-1'))
    for c in range(128, 256):
        self.assertRaises(SyntaxError, eval, 'b"%s"' % chr(c))
