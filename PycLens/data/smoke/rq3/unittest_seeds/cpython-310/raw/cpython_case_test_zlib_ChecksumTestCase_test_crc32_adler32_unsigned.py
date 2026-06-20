# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: ChecksumTestCase_test_crc32_adler32_unsigned

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    foo = b'abcdefghijklmnop'
    self.assertEqual(zlib.crc32(foo), 2486878355)
    self.assertEqual(zlib.crc32(b'spam'), 1138425661)
    self.assertEqual(zlib.adler32(foo + foo), 3573550353)
    self.assertEqual(zlib.adler32(b'spam'), 72286642)
