# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_IncrementalEncoder_test_getstate_returns_expected_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buffer_state_encoder = codecs.getincrementalencoder('euc_jis_2004')()
    self.assertEqual(buffer_state_encoder.getstate(), 0)
    buffer_state_encoder.encode('æ')
    self.assertEqual(buffer_state_encoder.getstate(), int.from_bytes(b'\x02\xc3\xa6\x00\x00\x00\x00\x00\x00\x00\x00', 'little'))
    buffer_state_encoder.encode('̀')
    self.assertEqual(buffer_state_encoder.getstate(), 0)
    non_buffer_state_encoder = codecs.getincrementalencoder('iso2022_jp')()
    self.assertEqual(non_buffer_state_encoder.getstate(), int.from_bytes(b'\x00BB\x00\x00\x00\x00\x00\x00', 'little'))
    non_buffer_state_encoder.encode('あ')
    self.assertEqual(non_buffer_state_encoder.getstate(), int.from_bytes(b'\x00\xc2B\x00\x00\x00\x00\x00\x00', 'little'))
