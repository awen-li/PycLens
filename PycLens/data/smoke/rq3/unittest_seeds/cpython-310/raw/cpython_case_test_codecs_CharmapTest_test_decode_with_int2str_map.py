# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CharmapTest_test_decode_with_int2str_map

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'strict', {0: 'a', 1: 'b', 2: 'c'}), ('abc', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'strict', {0: 'Aa', 1: 'Bb', 2: 'Cc'}), ('AaBbCc', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'strict', {0: '\U0010ffff', 1: 'b', 2: 'c'}), ('\U0010ffffbc', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'strict', {0: 'a', 1: 'b', 2: ''}), ('ab', 3))
    self.assertRaises(UnicodeDecodeError, codecs.charmap_decode, b'\x00\x01\x02', 'strict', {0: 'a', 1: 'b'})
    self.assertRaises(UnicodeDecodeError, codecs.charmap_decode, b'\x00\x01\x02', 'strict', {0: 'a', 1: 'b', 2: None})
    self.assertRaises(UnicodeDecodeError, codecs.charmap_decode, b'\x00\x01\x02', 'strict', {0: 'a', 1: 'b', 2: '\ufffe'})
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'replace', {0: 'a', 1: 'b'}), ('ab�', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'replace', {0: 'a', 1: 'b', 2: None}), ('ab�', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'replace', {0: 'a', 1: 'b', 2: '\ufffe'}), ('ab�', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'backslashreplace', {0: 'a', 1: 'b'}), ('ab\\x02', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'backslashreplace', {0: 'a', 1: 'b', 2: None}), ('ab\\x02', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'backslashreplace', {0: 'a', 1: 'b', 2: '\ufffe'}), ('ab\\x02', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'ignore', {0: 'a', 1: 'b'}), ('ab', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'ignore', {0: 'a', 1: 'b', 2: None}), ('ab', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'ignore', {0: 'a', 1: 'b', 2: '\ufffe'}), ('ab', 3))
    allbytes = bytes(range(256))
    self.assertEqual(codecs.charmap_decode(allbytes, 'ignore', {}), ('', len(allbytes)))
    self.assertRaisesRegex(TypeError, 'character mapping must be in range\\(0x110000\\)', codecs.charmap_decode, b'\x00\x01\x02', 'strict', {0: 'A', 1: 'Bb', 2: -2})
    self.assertRaisesRegex(TypeError, 'character mapping must be in range\\(0x110000\\)', codecs.charmap_decode, b'\x00\x01\x02', 'strict', {0: 'A', 1: 'Bb', 2: 999999999})
