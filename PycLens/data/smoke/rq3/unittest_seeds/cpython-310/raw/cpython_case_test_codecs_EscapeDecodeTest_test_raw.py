# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: EscapeDecodeTest_test_raw

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    decode = codecs.escape_decode
    for b in range(256):
        b = bytes([b])
        if b != b'\\':
            self.assertEqual(decode(b + b'0'), (b + b'0', 2))
