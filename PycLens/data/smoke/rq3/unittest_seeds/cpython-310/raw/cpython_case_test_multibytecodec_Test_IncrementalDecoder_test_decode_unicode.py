# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_IncrementalDecoder_test_decode_unicode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for enc in ALL_CJKENCODINGS:
        decoder = codecs.getincrementaldecoder(enc)()
        self.assertRaises(TypeError, decoder.decode, '')
