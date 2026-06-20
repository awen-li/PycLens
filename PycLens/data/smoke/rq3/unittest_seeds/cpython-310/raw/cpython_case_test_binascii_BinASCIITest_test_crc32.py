# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binascii.py
# case: BinASCIITest_test_crc32

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    crc = binascii.crc32(self.type2test(b'Test the CRC-32 of'))
    crc = binascii.crc32(self.type2test(b' this string.'), crc)
    self.assertEqual(crc, 1571220330)
    self.assertRaises(TypeError, binascii.crc32)
