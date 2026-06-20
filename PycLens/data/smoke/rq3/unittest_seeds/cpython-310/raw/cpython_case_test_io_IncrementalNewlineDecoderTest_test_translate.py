# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IncrementalNewlineDecoderTest_test_translate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for translate in (-2, -1, 1, 2):
        decoder = codecs.getincrementaldecoder('utf-8')()
        decoder = self.IncrementalNewlineDecoder(decoder, translate)
        self.check_newline_decoding_utf8(decoder)
    decoder = codecs.getincrementaldecoder('utf-8')()
    decoder = self.IncrementalNewlineDecoder(decoder, translate=0)
    self.assertEqual(decoder.decode(b'\r\r\n'), '\r\r\n')
