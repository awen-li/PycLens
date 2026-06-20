# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: EscapeDecodeTest_test_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    decode = codecs.escape_decode
    self.assertRaises(ValueError, decode, b'\\x')
    self.assertRaises(ValueError, decode, b'[\\x]')
    self.assertEqual(decode(b'[\\x]\\x', 'ignore'), (b'[]', 6))
    self.assertEqual(decode(b'[\\x]\\x', 'replace'), (b'[?]?', 6))
    self.assertRaises(ValueError, decode, b'\\x0')
    self.assertRaises(ValueError, decode, b'[\\x0]')
    self.assertEqual(decode(b'[\\x0]\\x0', 'ignore'), (b'[]', 8))
    self.assertEqual(decode(b'[\\x0]\\x0', 'replace'), (b'[?]?', 8))
