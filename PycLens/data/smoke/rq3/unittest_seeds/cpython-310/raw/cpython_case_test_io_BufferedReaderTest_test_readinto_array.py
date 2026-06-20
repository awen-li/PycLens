# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedReaderTest_test_readinto_array

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buffer_size = 60
    data = b'a' * 26
    rawio = self.MockRawIO((data,))
    bufio = self.tp(rawio, buffer_size=buffer_size)
    b = array.array('i', b'x' * 32)
    assert len(b) != 16
    n = bufio.readinto(b)
    self.assertGreater(n, len(b))
    bm = memoryview(b).cast('B')
    self.assertLess(n, len(bm))
    self.assertEqual(bm[:n], data[:n])
    self.assertEqual(bm[n:], b'x' * len(bm[n:]))
