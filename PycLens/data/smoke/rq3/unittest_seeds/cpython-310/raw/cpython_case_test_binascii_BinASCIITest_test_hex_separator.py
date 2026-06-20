# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binascii.py
# case: BinASCIITest_test_hex_separator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = b'{s\x05\x00\x00\x00worldi\x02\x00\x00\x00s\x05\x00\x00\x00helloi\x01\x00\x00\x000'
    self.assertEqual(binascii.hexlify(self.type2test(s)), s.hex().encode('ascii'))
    expected8 = s.hex('.', 8).encode('ascii')
    self.assertEqual(binascii.hexlify(self.type2test(s), '.', 8), expected8)
    expected1 = s.hex(':').encode('ascii')
    self.assertEqual(binascii.b2a_hex(self.type2test(s), ':'), expected1)
