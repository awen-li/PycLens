# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: EscapeDecodeTest_test_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(codecs.escape_decode(b''), (b'', 0))
    self.assertEqual(codecs.escape_decode(bytearray()), (b'', 0))
