# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_badandgoodxmlcharrefreplaceexceptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, codecs.xmlcharrefreplace_errors, 42)
    self.assertRaises(TypeError, codecs.xmlcharrefreplace_errors, UnicodeError('ouch'))
    self.assertRaises(TypeError, codecs.xmlcharrefreplace_errors, UnicodeDecodeError('ascii', bytearray(b'\xff'), 0, 1, 'ouch'))
    self.assertRaises(TypeError, codecs.xmlcharrefreplace_errors, UnicodeTranslateError('あ', 0, 1, 'ouch'))
    cs = (0, 1, 9, 10, 99, 100, 999, 1000, 9999, 10000, 99999, 100000, 999999, 1000000)
    cs += (55296, 57343)
    s = ''.join((chr(c) for c in cs))
    self.assertEqual(codecs.xmlcharrefreplace_errors(UnicodeEncodeError('ascii', 'a' + s + 'b', 1, 1 + len(s), 'ouch')), (''.join(('&#%d;' % c for c in cs)), 1 + len(s)))
