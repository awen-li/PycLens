# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedReaderTest_test_readinto

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rawio = self.MockRawIO((b'abc', b'd', b'efg'))
    bufio = self.tp(rawio)
    b = bytearray(2)
    self.assertEqual(bufio.readinto(b), 2)
    self.assertEqual(b, b'ab')
    self.assertEqual(bufio.readinto(b), 2)
    self.assertEqual(b, b'cd')
    self.assertEqual(bufio.readinto(b), 2)
    self.assertEqual(b, b'ef')
    self.assertEqual(bufio.readinto(b), 1)
    self.assertEqual(b, b'gf')
    self.assertEqual(bufio.readinto(b), 0)
    self.assertEqual(b, b'gf')
    rawio = self.MockRawIO((b'abc', None))
    bufio = self.tp(rawio)
    self.assertEqual(bufio.readinto(b), 2)
    self.assertEqual(b, b'ab')
    self.assertEqual(bufio.readinto(b), 1)
    self.assertEqual(b, b'cb')
