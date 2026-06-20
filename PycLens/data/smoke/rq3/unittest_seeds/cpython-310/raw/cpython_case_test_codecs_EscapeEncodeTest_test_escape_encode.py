# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: EscapeEncodeTest_test_escape_encode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = [(b'', (b'', 0)), (b'foobar', (b'foobar', 6)), (b'spam\x00eggs', (b'spam\\x00eggs', 9)), (b"a'b", (b"a\\'b", 3)), (b'b\\c', (b'b\\\\c', 3)), (b'c\nd', (b'c\\nd', 3)), (b'd\re', (b'd\\re', 3)), (b'f\x7fg', (b'f\\x7fg', 3))]
    for (data, output) in tests:
        with self.subTest(data=data):
            self.assertEqual(codecs.escape_encode(data), output)
    self.assertRaises(TypeError, codecs.escape_encode, 'spam')
    self.assertRaises(TypeError, codecs.escape_encode, bytearray(b'spam'))
