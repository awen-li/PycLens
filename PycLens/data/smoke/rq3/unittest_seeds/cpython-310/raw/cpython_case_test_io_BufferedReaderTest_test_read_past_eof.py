# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedReaderTest_test_read_past_eof

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rawio = self.MockRawIO((b'abc', b'd', b'efg'))
    bufio = self.tp(rawio)
    self.assertEqual(b'abcdefg', bufio.read(9000))
