# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_IncrementalEncoder_test_stateful_keep_buffer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encoder = codecs.getincrementalencoder('jisx0213')()
    self.assertEqual(encoder.encode('æ'), b'')
    self.assertRaises(UnicodeEncodeError, encoder.encode, 'ģ')
    self.assertEqual(encoder.encode('̀æ'), b'\xab\xc4')
    self.assertRaises(UnicodeEncodeError, encoder.encode, 'ģ')
    self.assertEqual(encoder.reset(), None)
    self.assertEqual(encoder.encode('̀'), b'\xab\xdc')
    self.assertEqual(encoder.encode('æ'), b'')
    self.assertRaises(UnicodeEncodeError, encoder.encode, 'ģ')
    self.assertEqual(encoder.encode('', True), b'\xa9\xdc')
