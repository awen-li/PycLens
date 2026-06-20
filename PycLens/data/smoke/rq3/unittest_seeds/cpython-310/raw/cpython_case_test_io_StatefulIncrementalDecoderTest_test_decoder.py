# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: StatefulIncrementalDecoderTest_test_decoder

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (input, eof, output) in self.test_cases:
        d = StatefulIncrementalDecoder()
        self.assertEqual(d.decode(input, eof), output)
    d = StatefulIncrementalDecoder()
    self.assertEqual(d.decode(b'oiabcd'), '')
    self.assertEqual(d.decode(b'', 1), 'abcd.')
