# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: RawUnicodeEscapeTest_test_raw_encode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encode = codecs.raw_unicode_escape_encode
    for b in range(256):
        self.assertEqual(encode(chr(b)), (bytes([b]), 1))
