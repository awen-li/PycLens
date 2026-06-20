# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IncrementalNewlineDecoderTest_test_newline_decoder

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encodings = (None, 'utf-8', 'latin-1', 'utf-16', 'utf-16-le', 'utf-16-be', 'utf-32', 'utf-32-le', 'utf-32-be')
    for enc in encodings:
        decoder = enc and codecs.getincrementaldecoder(enc)()
        decoder = self.IncrementalNewlineDecoder(decoder, translate=True)
        self.check_newline_decoding(decoder, enc)
    decoder = codecs.getincrementaldecoder('utf-8')()
    decoder = self.IncrementalNewlineDecoder(decoder, translate=True)
    self.check_newline_decoding_utf8(decoder)
    self.assertRaises(TypeError, decoder.setstate, 42)
