# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CharmapTest_test_decode_with_int2int_map

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = ord('a')
    b = ord('b')
    c = ord('c')
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'strict', {0: a, 1: b, 2: c}), ('abc', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'strict', {0: 1114111, 1: b, 2: c}), ('\U0010ffffbc', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'strict', {0: sys.maxunicode, 1: b, 2: c}), (chr(sys.maxunicode) + 'bc', 3))
    self.assertRaises(TypeError, codecs.charmap_decode, b'\x00\x01\x02', 'strict', {0: sys.maxunicode + 1, 1: b, 2: c})
    self.assertRaises(UnicodeDecodeError, codecs.charmap_decode, b'\x00\x01\x02', 'strict', {0: a, 1: b})
    self.assertRaises(UnicodeDecodeError, codecs.charmap_decode, b'\x00\x01\x02', 'strict', {0: a, 1: b, 2: 65534})
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'replace', {0: a, 1: b}), ('ab�', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'replace', {0: a, 1: b, 2: 65534}), ('ab�', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'backslashreplace', {0: a, 1: b}), ('ab\\x02', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'backslashreplace', {0: a, 1: b, 2: 65534}), ('ab\\x02', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'ignore', {0: a, 1: b}), ('ab', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'ignore', {0: a, 1: b, 2: 65534}), ('ab', 3))
