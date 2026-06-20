# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: BasicUnicodeTest_test_bad_encode_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for encoding in all_unicode_encodings:
        encoder = codecs.getencoder(encoding)
        self.assertRaises(TypeError, encoder)
