# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CBufferedReaderTest_test_initialization

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rawio = self.MockRawIO([b'abc'])
    bufio = self.tp(rawio)
    self.assertRaises(ValueError, bufio.__init__, rawio, buffer_size=0)
    self.assertRaises(ValueError, bufio.read)
    self.assertRaises(ValueError, bufio.__init__, rawio, buffer_size=-16)
    self.assertRaises(ValueError, bufio.read)
    self.assertRaises(ValueError, bufio.__init__, rawio, buffer_size=-1)
    self.assertRaises(ValueError, bufio.read)
