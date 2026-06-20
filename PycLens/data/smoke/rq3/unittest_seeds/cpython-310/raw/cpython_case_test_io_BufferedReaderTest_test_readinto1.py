# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedReaderTest_test_readinto1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buffer_size = 10
    rawio = self.MockRawIO((b'abc', b'de', b'fgh', b'jkl'))
    bufio = self.tp(rawio, buffer_size=buffer_size)
    b = bytearray(2)
    self.assertEqual(bufio.peek(3), b'abc')
    self.assertEqual(rawio._reads, 1)
    self.assertEqual(bufio.readinto1(b), 2)
    self.assertEqual(b, b'ab')
    self.assertEqual(rawio._reads, 1)
    self.assertEqual(bufio.readinto1(b), 1)
    self.assertEqual(b[:1], b'c')
    self.assertEqual(rawio._reads, 1)
    self.assertEqual(bufio.readinto1(b), 2)
    self.assertEqual(b, b'de')
    self.assertEqual(rawio._reads, 2)
    b = bytearray(2 * buffer_size)
    self.assertEqual(bufio.peek(3), b'fgh')
    self.assertEqual(rawio._reads, 3)
    self.assertEqual(bufio.readinto1(b), 6)
    self.assertEqual(b[:6], b'fghjkl')
    self.assertEqual(rawio._reads, 4)
