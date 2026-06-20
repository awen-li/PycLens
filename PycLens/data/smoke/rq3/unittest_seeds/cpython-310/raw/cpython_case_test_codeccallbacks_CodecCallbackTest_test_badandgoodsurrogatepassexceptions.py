# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_badandgoodsurrogatepassexceptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    surrogatepass_errors = codecs.lookup_error('surrogatepass')
    self.assertRaises(TypeError, surrogatepass_errors, 42)
    self.assertRaises(TypeError, surrogatepass_errors, UnicodeError('ouch'))
    self.assertRaises(TypeError, surrogatepass_errors, UnicodeTranslateError('\ud800', 0, 1, 'ouch'))
    for enc in ('utf-8', 'utf-16le', 'utf-16be', 'utf-32le', 'utf-32be'):
        with self.subTest(encoding=enc):
            self.assertRaises(UnicodeEncodeError, surrogatepass_errors, UnicodeEncodeError(enc, 'a', 0, 1, 'ouch'))
            self.assertRaises(UnicodeDecodeError, surrogatepass_errors, UnicodeDecodeError(enc, 'a'.encode(enc), 0, 1, 'ouch'))
    for s in ('\ud800', '\udfff', '\ud800\udfff'):
        with self.subTest(str=s):
            self.assertRaises(UnicodeEncodeError, surrogatepass_errors, UnicodeEncodeError('ascii', s, 0, len(s), 'ouch'))
    tests = [('utf-8', '\ud800', b'\xed\xa0\x80', 3), ('utf-16le', '\ud800', b'\x00\xd8', 2), ('utf-16be', '\ud800', b'\xd8\x00', 2), ('utf-32le', '\ud800', b'\x00\xd8\x00\x00', 4), ('utf-32be', '\ud800', b'\x00\x00\xd8\x00', 4), ('utf-8', '\udfff', b'\xed\xbf\xbf', 3), ('utf-16le', '\udfff', b'\xff\xdf', 2), ('utf-16be', '\udfff', b'\xdf\xff', 2), ('utf-32le', '\udfff', b'\xff\xdf\x00\x00', 4), ('utf-32be', '\udfff', b'\x00\x00\xdf\xff', 4), ('utf-8', '\ud800\udfff', b'\xed\xa0\x80\xed\xbf\xbf', 3), ('utf-16le', '\ud800\udfff', b'\x00\xd8\xff\xdf', 2), ('utf-16be', '\ud800\udfff', b'\xd8\x00\xdf\xff', 2), ('utf-32le', '\ud800\udfff', b'\x00\xd8\x00\x00\xff\xdf\x00\x00', 4), ('utf-32be', '\ud800\udfff', b'\x00\x00\xd8\x00\x00\x00\xdf\xff', 4)]
    for (enc, s, b, n) in tests:
        with self.subTest(encoding=enc, str=s, bytes=b):
            self.assertEqual(surrogatepass_errors(UnicodeEncodeError(enc, 'a' + s + 'b', 1, 1 + len(s), 'ouch')), (b, 1 + len(s)))
            self.assertEqual(surrogatepass_errors(UnicodeDecodeError(enc, bytearray(b'a' + b[:n] + b'b'), 1, 1 + n, 'ouch')), (s[:1], 1 + n))
