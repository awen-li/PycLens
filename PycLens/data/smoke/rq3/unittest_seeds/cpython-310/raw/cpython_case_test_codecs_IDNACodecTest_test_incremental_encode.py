# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: IDNACodecTest_test_incremental_encode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(b''.join(codecs.iterencode('python.org', 'idna')), b'python.org')
    self.assertEqual(b''.join(codecs.iterencode('python.org.', 'idna')), b'python.org.')
    self.assertEqual(b''.join(codecs.iterencode('pythön.org.', 'idna')), b'xn--pythn-mua.org.')
    self.assertEqual(b''.join(codecs.iterencode('pythön.org.', 'idna')), b'xn--pythn-mua.org.')
    encoder = codecs.getincrementalencoder('idna')()
    self.assertEqual(encoder.encode('äx'), b'')
    self.assertEqual(encoder.encode('ample.org'), b'xn--xample-9ta.')
    self.assertEqual(encoder.encode('', True), b'org')
    encoder.reset()
    self.assertEqual(encoder.encode('äx'), b'')
    self.assertEqual(encoder.encode('ample.org.'), b'xn--xample-9ta.org.')
    self.assertEqual(encoder.encode('', True), b'')
