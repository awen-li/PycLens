# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: TestStateful_test_incrementalencoder_final

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encoder = codecs.getincrementalencoder(self.encoding)()
    last_index = len(self.text) - 1
    output = b''.join((encoder.encode(char, index == last_index) for (index, char) in enumerate(self.text)))
    self.assertEqual(output, self.expected_reset)
    self.assertEqual(encoder.encode('', final=True), b'')
