# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: TestStateful_test_incrementalencoder

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encoder = codecs.getincrementalencoder(self.encoding)()
    output = b''.join((encoder.encode(char) for char in self.text))
    self.assertEqual(output, self.expected)
    self.assertEqual(encoder.encode('', final=True), self.reset)
    self.assertEqual(encoder.encode('', final=True), b'')
