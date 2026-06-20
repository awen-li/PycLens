# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: TypesTest_test_unicode_escape

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(codecs.unicode_escape_decode('\\u1234'), ('ሴ', 6))
    self.assertEqual(codecs.unicode_escape_decode(b'\\u1234'), ('ሴ', 6))
    self.assertEqual(codecs.raw_unicode_escape_decode('\\u1234'), ('ሴ', 6))
    self.assertEqual(codecs.raw_unicode_escape_decode(b'\\u1234'), ('ሴ', 6))
    self.assertRaises(UnicodeDecodeError, codecs.unicode_escape_decode, b'\\U00110000')
    self.assertEqual(codecs.unicode_escape_decode('\\U00110000', 'replace'), ('�', 10))
    self.assertEqual(codecs.unicode_escape_decode('\\U00110000', 'backslashreplace'), ('\\x5c\\x55\\x30\\x30\\x31\\x31\\x30\\x30\\x30\\x30', 10))
    self.assertRaises(UnicodeDecodeError, codecs.raw_unicode_escape_decode, b'\\U00110000')
    self.assertEqual(codecs.raw_unicode_escape_decode('\\U00110000', 'replace'), ('�', 10))
    self.assertEqual(codecs.raw_unicode_escape_decode('\\U00110000', 'backslashreplace'), ('\\x5c\\x55\\x30\\x30\\x31\\x31\\x30\\x30\\x30\\x30', 10))
