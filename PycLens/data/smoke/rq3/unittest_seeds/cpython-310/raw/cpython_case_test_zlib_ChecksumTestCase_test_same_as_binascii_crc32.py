# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: ChecksumTestCase_test_same_as_binascii_crc32

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    foo = b'abcdefghijklmnop'
    crc = 2486878355
    self.assertEqual(binascii.crc32(foo), crc)
    self.assertEqual(zlib.crc32(foo), crc)
    self.assertEqual(binascii.crc32(b'spam'), zlib.crc32(b'spam'))
