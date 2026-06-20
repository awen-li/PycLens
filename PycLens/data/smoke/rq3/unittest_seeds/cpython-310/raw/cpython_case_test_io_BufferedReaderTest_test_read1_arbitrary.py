# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedReaderTest_test_read1_arbitrary

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rawio = self.MockRawIO((b'abc', b'd', b'efg'))
    bufio = self.tp(rawio)
    self.assertEqual(b'a', bufio.read(1))
    self.assertEqual(b'bc', bufio.read1())
    self.assertEqual(b'd', bufio.read1())
    self.assertEqual(b'efg', bufio.read1(-1))
    self.assertEqual(rawio._reads, 3)
    self.assertEqual(b'', bufio.read1())
    self.assertEqual(rawio._reads, 4)
