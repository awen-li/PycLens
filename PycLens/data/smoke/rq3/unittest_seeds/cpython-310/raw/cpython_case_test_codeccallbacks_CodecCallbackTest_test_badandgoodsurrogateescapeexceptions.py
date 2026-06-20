# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_badandgoodsurrogateescapeexceptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    surrogateescape_errors = codecs.lookup_error('surrogateescape')
    self.assertRaises(TypeError, surrogateescape_errors, 42)
    self.assertRaises(TypeError, surrogateescape_errors, UnicodeError('ouch'))
    self.assertRaises(TypeError, surrogateescape_errors, UnicodeTranslateError('\udc80', 0, 1, 'ouch'))
    for s in ('a', '\udc7f', '\udd00'):
        with self.subTest(str=s):
            self.assertRaises(UnicodeEncodeError, surrogateescape_errors, UnicodeEncodeError('ascii', s, 0, 1, 'ouch'))
    self.assertEqual(surrogateescape_errors(UnicodeEncodeError('ascii', 'a\udc80b', 1, 2, 'ouch')), (b'\x80', 2))
    self.assertRaises(UnicodeDecodeError, surrogateescape_errors, UnicodeDecodeError('ascii', bytearray(b'a'), 0, 1, 'ouch'))
    self.assertEqual(surrogateescape_errors(UnicodeDecodeError('ascii', bytearray(b'a\x80b'), 1, 2, 'ouch')), ('\udc80', 2))
