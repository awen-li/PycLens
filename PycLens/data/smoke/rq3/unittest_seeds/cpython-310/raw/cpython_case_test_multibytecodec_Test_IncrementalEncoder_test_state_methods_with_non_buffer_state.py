# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_IncrementalEncoder_test_state_methods_with_non_buffer_state

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encoder = codecs.getincrementalencoder('iso2022_jp')()
    self.assertEqual(encoder.encode('z'), b'z')
    en_state = encoder.getstate()
    self.assertEqual(encoder.encode('あ'), b'\x1b$B$"')
    jp_state = encoder.getstate()
    self.assertEqual(encoder.encode('z'), b'\x1b(Bz')
    encoder.setstate(jp_state)
    self.assertEqual(encoder.encode('あ'), b'$"')
    encoder.setstate(en_state)
    self.assertEqual(encoder.encode('z'), b'z')
