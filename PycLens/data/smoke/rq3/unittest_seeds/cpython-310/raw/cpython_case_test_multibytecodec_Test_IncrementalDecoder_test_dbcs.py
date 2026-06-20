# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_IncrementalDecoder_test_dbcs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    decoder = codecs.getincrementaldecoder('cp949')()
    self.assertEqual(decoder.decode(b'\xc6\xc4\xc0\xcc\xbd'), '파이')
    self.assertEqual(decoder.decode(b'\xe3 \xb8\xb6\xc0\xbb'), '썬 마을')
    self.assertEqual(decoder.decode(b''), '')
