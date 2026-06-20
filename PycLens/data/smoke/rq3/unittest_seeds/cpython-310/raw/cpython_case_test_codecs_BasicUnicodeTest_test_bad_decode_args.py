# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: BasicUnicodeTest_test_bad_decode_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for encoding in all_unicode_encodings:
        decoder = codecs.getdecoder(encoding)
        self.assertRaises(TypeError, decoder)
        if encoding not in ('idna', 'punycode'):
            self.assertRaises(TypeError, decoder, 42)
