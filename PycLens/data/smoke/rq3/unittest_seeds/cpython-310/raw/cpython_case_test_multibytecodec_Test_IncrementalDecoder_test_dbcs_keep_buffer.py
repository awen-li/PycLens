# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_IncrementalDecoder_test_dbcs_keep_buffer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    decoder = codecs.getincrementaldecoder('cp949')()
    self.assertEqual(decoder.decode(b'\xc6\xc4\xc0'), '파')
    self.assertRaises(UnicodeDecodeError, decoder.decode, b'', True)
    self.assertEqual(decoder.decode(b'\xcc'), '이')
    self.assertEqual(decoder.decode(b'\xc6\xc4\xc0'), '파')
    self.assertRaises(UnicodeDecodeError, decoder.decode, b'\xcc\xbd', True)
    self.assertEqual(decoder.decode(b'\xcc'), '이')
