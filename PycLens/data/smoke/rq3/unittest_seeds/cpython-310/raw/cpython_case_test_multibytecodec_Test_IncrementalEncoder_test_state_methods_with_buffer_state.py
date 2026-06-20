# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_IncrementalEncoder_test_state_methods_with_buffer_state

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encoder = codecs.getincrementalencoder('euc_jis_2004')()
    initial_state = encoder.getstate()
    self.assertEqual(encoder.encode('æ̀'), b'\xab\xc4')
    encoder.setstate(initial_state)
    self.assertEqual(encoder.encode('æ̀'), b'\xab\xc4')
    self.assertEqual(encoder.encode('æ'), b'')
    partial_state = encoder.getstate()
    self.assertEqual(encoder.encode('̀'), b'\xab\xc4')
    encoder.setstate(partial_state)
    self.assertEqual(encoder.encode('̀'), b'\xab\xc4')
