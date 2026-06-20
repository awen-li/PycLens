# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_partition_bytearray_doesnt_share_nullstring

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (a, b, c) = bytearray(b'x').partition(b'y')
    self.assertEqual(b, b'')
    self.assertEqual(c, b'')
    self.assertIsNot(b, c)
    b += b'!'
    self.assertEqual(c, b'')
    (a, b, c) = bytearray(b'x').partition(b'y')
    self.assertEqual(b, b'')
    self.assertEqual(c, b'')
    (b, c, a) = bytearray(b'x').rpartition(b'y')
    self.assertEqual(b, b'')
    self.assertEqual(c, b'')
    self.assertIsNot(b, c)
    b += b'!'
    self.assertEqual(c, b'')
    (c, b, a) = bytearray(b'x').rpartition(b'y')
    self.assertEqual(b, b'')
    self.assertEqual(c, b'')
