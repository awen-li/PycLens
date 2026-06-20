# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UnicodeEscapeTest_test_raw_encode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encode = codecs.unicode_escape_encode
    for b in range(32, 127):
        if b != b'\\'[0]:
            self.assertEqual(encode(chr(b)), (bytes([b]), 1))
