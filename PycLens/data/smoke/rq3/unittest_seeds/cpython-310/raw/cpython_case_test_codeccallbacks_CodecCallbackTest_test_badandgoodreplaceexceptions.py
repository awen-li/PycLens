# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_badandgoodreplaceexceptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, codecs.replace_errors, 42)
    self.assertRaises(TypeError, codecs.replace_errors, UnicodeError('ouch'))
    self.assertRaises(TypeError, codecs.replace_errors, BadObjectUnicodeEncodeError())
    self.assertRaises(TypeError, codecs.replace_errors, BadObjectUnicodeDecodeError())
    self.assertEqual(codecs.replace_errors(UnicodeEncodeError('ascii', 'aあb', 1, 2, 'ouch')), ('?', 2))
    self.assertEqual(codecs.replace_errors(UnicodeDecodeError('ascii', bytearray(b'a\xffb'), 1, 2, 'ouch')), ('�', 2))
    self.assertEqual(codecs.replace_errors(UnicodeTranslateError('aあb', 1, 2, 'ouch')), ('�', 2))
