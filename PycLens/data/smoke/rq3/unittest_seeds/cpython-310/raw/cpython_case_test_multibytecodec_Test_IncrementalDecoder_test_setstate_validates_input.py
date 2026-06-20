# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_IncrementalDecoder_test_setstate_validates_input

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    decoder = codecs.getincrementaldecoder('euc_jp')()
    self.assertRaises(TypeError, decoder.setstate, 123)
    self.assertRaises(TypeError, decoder.setstate, ('invalid', 0))
    self.assertRaises(TypeError, decoder.setstate, (b'1234', 'invalid'))
    self.assertRaises(UnicodeError, decoder.setstate, (b'123456789', 0))
