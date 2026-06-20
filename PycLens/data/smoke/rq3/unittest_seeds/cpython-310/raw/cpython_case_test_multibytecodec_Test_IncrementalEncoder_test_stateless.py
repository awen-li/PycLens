# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_IncrementalEncoder_test_stateless

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encoder = codecs.getincrementalencoder('cp949')()
    self.assertEqual(encoder.encode('파이썬 마을'), b'\xc6\xc4\xc0\xcc\xbd\xe3 \xb8\xb6\xc0\xbb')
    self.assertEqual(encoder.reset(), None)
    self.assertEqual(encoder.encode('☆∼☆', True), b'\xa1\xd9\xa1\xad\xa1\xd9')
    self.assertEqual(encoder.reset(), None)
    self.assertEqual(encoder.encode('', True), b'')
    self.assertEqual(encoder.encode('', False), b'')
    self.assertEqual(encoder.reset(), None)
