# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_badandgoodstrictexceptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, codecs.strict_errors, 42)
    self.assertRaises(Exception, codecs.strict_errors, Exception('ouch'))
    self.assertRaises(UnicodeEncodeError, codecs.strict_errors, UnicodeEncodeError('ascii', 'あ', 0, 1, 'ouch'))
    self.assertRaises(UnicodeDecodeError, codecs.strict_errors, UnicodeDecodeError('ascii', bytearray(b'\xff'), 0, 1, 'ouch'))
    self.assertRaises(UnicodeTranslateError, codecs.strict_errors, UnicodeTranslateError('あ', 0, 1, 'ouch'))
