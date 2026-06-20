# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_badandgoodbackslashreplaceexceptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, codecs.backslashreplace_errors, 42)
    self.assertRaises(TypeError, codecs.backslashreplace_errors, UnicodeError('ouch'))
    tests = [('あ', '\\u3042'), ('\n', '\\x0a'), ('a', '\\x61'), ('\x00', '\\x00'), ('ÿ', '\\xff'), ('Ā', '\\u0100'), ('\uffff', '\\uffff'), ('𐀀', '\\U00010000'), ('\U0010ffff', '\\U0010ffff'), ('\ud800', '\\ud800'), ('\udfff', '\\udfff'), ('\ud800\udfff', '\\ud800\\udfff')]
    for (s, r) in tests:
        with self.subTest(str=s):
            self.assertEqual(codecs.backslashreplace_errors(UnicodeEncodeError('ascii', 'a' + s + 'b', 1, 1 + len(s), 'ouch')), (r, 1 + len(s)))
            self.assertEqual(codecs.backslashreplace_errors(UnicodeTranslateError('a' + s + 'b', 1, 1 + len(s), 'ouch')), (r, 1 + len(s)))
    tests = [(b'a', '\\x61'), (b'\n', '\\x0a'), (b'\x00', '\\x00'), (b'\xff', '\\xff')]
    for (b, r) in tests:
        with self.subTest(bytes=b):
            self.assertEqual(codecs.backslashreplace_errors(UnicodeDecodeError('ascii', bytearray(b'a' + b + b'b'), 1, 2, 'ouch')), (r, 2))
