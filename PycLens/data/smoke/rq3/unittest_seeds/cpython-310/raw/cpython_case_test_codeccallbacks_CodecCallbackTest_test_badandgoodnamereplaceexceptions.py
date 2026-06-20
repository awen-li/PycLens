# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_badandgoodnamereplaceexceptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, codecs.namereplace_errors, 42)
    self.assertRaises(TypeError, codecs.namereplace_errors, UnicodeError('ouch'))
    self.assertRaises(TypeError, codecs.namereplace_errors, UnicodeDecodeError('ascii', bytearray(b'\xff'), 0, 1, 'ouch'))
    self.assertRaises(TypeError, codecs.namereplace_errors, UnicodeTranslateError('あ', 0, 1, 'ouch'))
    tests = [('あ', '\\N{HIRAGANA LETTER A}'), ('\x00', '\\x00'), ('ﯹ', '\\N{ARABIC LIGATURE UIGHUR KIRGHIZ YEH WITH HAMZA ABOVE WITH ALEF MAKSURA ISOLATED FORM}'), ('\U000e007f', '\\N{CANCEL TAG}'), ('\U0010ffff', '\\U0010ffff'), ('\ud800', '\\ud800'), ('\udfff', '\\udfff'), ('\ud800\udfff', '\\ud800\\udfff')]
    for (s, r) in tests:
        with self.subTest(str=s):
            self.assertEqual(codecs.namereplace_errors(UnicodeEncodeError('ascii', 'a' + s + 'b', 1, 1 + len(s), 'ouch')), (r, 1 + len(s)))
