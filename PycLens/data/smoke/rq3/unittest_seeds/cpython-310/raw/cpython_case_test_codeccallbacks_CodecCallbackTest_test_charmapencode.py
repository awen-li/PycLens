# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_charmapencode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    charmap = dict(((ord(c), bytes(2 * c.upper(), 'ascii')) for c in 'abcdefgh'))
    sin = 'abc'
    sout = b'AABBCC'
    self.assertEqual(codecs.charmap_encode(sin, 'strict', charmap)[0], sout)
    sin = 'abcA'
    self.assertRaises(UnicodeError, codecs.charmap_encode, sin, 'strict', charmap)
    charmap[ord('?')] = b'XYZ'
    sin = 'abcDEF'
    sout = b'AABBCCXYZXYZXYZ'
    self.assertEqual(codecs.charmap_encode(sin, 'replace', charmap)[0], sout)
    charmap[ord('?')] = 'XYZ'
    self.assertRaises(TypeError, codecs.charmap_encode, sin, 'replace', charmap)
