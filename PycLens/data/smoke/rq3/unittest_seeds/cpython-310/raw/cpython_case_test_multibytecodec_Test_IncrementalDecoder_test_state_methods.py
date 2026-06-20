# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_IncrementalDecoder_test_state_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    decoder = codecs.getincrementaldecoder('euc_jp')()
    self.assertEqual(decoder.decode(b'\xa4\xa6'), 'う')
    (pending1, _) = decoder.getstate()
    self.assertEqual(pending1, b'')
    self.assertEqual(decoder.decode(b'\xa4'), '')
    (pending2, flags2) = decoder.getstate()
    self.assertEqual(pending2, b'\xa4')
    self.assertEqual(decoder.decode(b'\xa6'), 'う')
    (pending3, _) = decoder.getstate()
    self.assertEqual(pending3, b'')
    decoder.setstate((pending2, flags2))
    self.assertEqual(decoder.decode(b'\xa6'), 'う')
    (pending4, _) = decoder.getstate()
    self.assertEqual(pending4, b'')
    decoder.setstate((b'abc', 123456789))
    self.assertEqual(decoder.getstate(), (b'abc', 123456789))
