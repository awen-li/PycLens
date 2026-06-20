# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: ReadTest_test_incremental_surrogatepass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = '\ud901'.encode(self.encoding, 'surrogatepass')
    for i in range(1, len(data)):
        dec = codecs.getincrementaldecoder(self.encoding)('surrogatepass')
        self.assertEqual(dec.decode(data[:i]), '')
        self.assertEqual(dec.decode(data[i:], True), '\ud901')
    data = '\udc02'.encode(self.encoding, 'surrogatepass')
    for i in range(1, len(data)):
        dec = codecs.getincrementaldecoder(self.encoding)('surrogatepass')
        self.assertEqual(dec.decode(data[:i]), '')
        self.assertEqual(dec.decode(data[i:]), '\udc02')
