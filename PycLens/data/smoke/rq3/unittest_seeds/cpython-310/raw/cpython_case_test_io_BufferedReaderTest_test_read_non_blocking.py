# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedReaderTest_test_read_non_blocking

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rawio = self.MockRawIO((b'abc', b'd', None, b'efg', None, None, None))
    bufio = self.tp(rawio)
    self.assertEqual(b'abcd', bufio.read(6))
    self.assertEqual(b'e', bufio.read(1))
    self.assertEqual(b'fg', bufio.read())
    self.assertEqual(b'', bufio.peek(1))
    self.assertIsNone(bufio.read())
    self.assertEqual(b'', bufio.read())
    rawio = self.MockRawIO((b'a', None, None))
    self.assertEqual(b'a', rawio.readall())
    self.assertIsNone(rawio.readall())
