# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binascii.py
# case: BinASCIITest_test_hex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = b'{s\x05\x00\x00\x00worldi\x02\x00\x00\x00s\x05\x00\x00\x00helloi\x01\x00\x00\x000'
    t = binascii.b2a_hex(self.type2test(s))
    u = binascii.a2b_hex(self.type2test(t))
    self.assertEqual(s, u)
    self.assertRaises(binascii.Error, binascii.a2b_hex, t[:-1])
    self.assertRaises(binascii.Error, binascii.a2b_hex, t[:-1] + b'q')
    self.assertRaises(binascii.Error, binascii.a2b_hex, bytes([255, 255]))
    self.assertRaises(binascii.Error, binascii.a2b_hex, b'0G')
    self.assertRaises(binascii.Error, binascii.a2b_hex, b'0g')
    self.assertRaises(binascii.Error, binascii.a2b_hex, b'G0')
    self.assertRaises(binascii.Error, binascii.a2b_hex, b'g0')
    self.assertEqual(binascii.hexlify(self.type2test(s)), t)
    self.assertEqual(binascii.unhexlify(self.type2test(t)), u)
