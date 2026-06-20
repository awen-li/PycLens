# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: AssortedBytesTest_test_compare_bytes_to_bytearray

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(b'abc' == bytes(b'abc'), True)
    self.assertEqual(b'ab' != bytes(b'abc'), True)
    self.assertEqual(b'ab' <= bytes(b'abc'), True)
    self.assertEqual(b'ab' < bytes(b'abc'), True)
    self.assertEqual(b'abc' >= bytes(b'ab'), True)
    self.assertEqual(b'abc' > bytes(b'ab'), True)
    self.assertEqual(b'abc' != bytes(b'abc'), False)
    self.assertEqual(b'ab' == bytes(b'abc'), False)
    self.assertEqual(b'ab' > bytes(b'abc'), False)
    self.assertEqual(b'ab' >= bytes(b'abc'), False)
    self.assertEqual(b'abc' < bytes(b'ab'), False)
    self.assertEqual(b'abc' <= bytes(b'ab'), False)
    self.assertEqual(bytes(b'abc') == b'abc', True)
    self.assertEqual(bytes(b'ab') != b'abc', True)
    self.assertEqual(bytes(b'ab') <= b'abc', True)
    self.assertEqual(bytes(b'ab') < b'abc', True)
    self.assertEqual(bytes(b'abc') >= b'ab', True)
    self.assertEqual(bytes(b'abc') > b'ab', True)
    self.assertEqual(bytes(b'abc') != b'abc', False)
    self.assertEqual(bytes(b'ab') == b'abc', False)
    self.assertEqual(bytes(b'ab') > b'abc', False)
    self.assertEqual(bytes(b'ab') >= b'abc', False)
    self.assertEqual(bytes(b'abc') < b'ab', False)
    self.assertEqual(bytes(b'abc') <= b'ab', False)
