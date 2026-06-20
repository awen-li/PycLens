# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedReaderTest_test_truncate_on_read_only

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rawio = self.MockFileIO(b'abc')
    bufio = self.tp(rawio)
    self.assertFalse(bufio.writable())
    self.assertRaises(self.UnsupportedOperation, bufio.truncate)
    self.assertRaises(self.UnsupportedOperation, bufio.truncate, 0)
