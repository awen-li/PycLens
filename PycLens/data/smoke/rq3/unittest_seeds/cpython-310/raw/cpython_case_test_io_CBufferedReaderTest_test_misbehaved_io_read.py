# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CBufferedReaderTest_test_misbehaved_io_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rawio = self.MisbehavedRawIO((b'abc', b'd', b'efg'))
    bufio = self.tp(rawio)
    self.assertRaises(OSError, bufio.read, 10)
