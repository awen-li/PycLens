# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CharmapTest_test_decode_with_string_map

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'strict', 'abc'), ('abc', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'strict', '\U0010ffffbc'), ('\U0010ffffbc', 3))
    self.assertRaises(UnicodeDecodeError, codecs.charmap_decode, b'\x00\x01\x02', 'strict', 'ab')
    self.assertRaises(UnicodeDecodeError, codecs.charmap_decode, b'\x00\x01\x02', 'strict', 'ab\ufffe')
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'replace', 'ab'), ('ab�', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'replace', 'ab\ufffe'), ('ab�', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'backslashreplace', 'ab'), ('ab\\x02', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'backslashreplace', 'ab\ufffe'), ('ab\\x02', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'ignore', 'ab'), ('ab', 3))
    self.assertEqual(codecs.charmap_decode(b'\x00\x01\x02', 'ignore', 'ab\ufffe'), ('ab', 3))
    allbytes = bytes(range(256))
    self.assertEqual(codecs.charmap_decode(allbytes, 'ignore', ''), ('', len(allbytes)))
