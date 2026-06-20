# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binascii.py
# case: BinASCIITest_test_crc_hqx

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    crc = binascii.crc_hqx(self.type2test(b'Test the CRC-32 of'), 0)
    crc = binascii.crc_hqx(self.type2test(b' this string.'), crc)
    self.assertEqual(crc, 14290)
    self.assertRaises(TypeError, binascii.crc_hqx)
    self.assertRaises(TypeError, binascii.crc_hqx, self.type2test(b''))
    for crc in (0, 1, 4660, 74565, 305419896, -1):
        self.assertEqual(binascii.crc_hqx(self.type2test(b''), crc), crc & 65535)
