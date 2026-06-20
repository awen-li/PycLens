# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_IncrementalEncoder_test_stateful

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encoder = codecs.getincrementalencoder('jisx0213')()
    self.assertEqual(encoder.encode('æ̀'), b'\xab\xc4')
    self.assertEqual(encoder.encode('æ'), b'')
    self.assertEqual(encoder.encode('̀'), b'\xab\xc4')
    self.assertEqual(encoder.encode('æ', True), b'\xa9\xdc')
    self.assertEqual(encoder.reset(), None)
    self.assertEqual(encoder.encode('̀'), b'\xab\xdc')
    self.assertEqual(encoder.encode('æ'), b'')
    self.assertEqual(encoder.encode('', True), b'\xa9\xdc')
    self.assertEqual(encoder.encode('', True), b'')
