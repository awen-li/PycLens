# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UnicodeEscapeTest_test_raw_decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    decode = codecs.unicode_escape_decode
    for b in range(256):
        if b != b'\\'[0]:
            self.assertEqual(decode(bytes([b]) + b'0'), (chr(b) + '0', 2))
