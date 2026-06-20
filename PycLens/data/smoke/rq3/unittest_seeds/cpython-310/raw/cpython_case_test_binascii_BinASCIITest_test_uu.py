# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binascii.py
# case: BinASCIITest_test_uu

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    MAX_UU = 45
    for backtick in (True, False):
        lines = []
        for i in range(0, len(self.data), MAX_UU):
            b = self.type2test(self.rawdata[i:i + MAX_UU])
            a = binascii.b2a_uu(b, backtick=backtick)
            lines.append(a)
        res = bytes()
        for line in lines:
            a = self.type2test(line)
            b = binascii.a2b_uu(a)
            res += b
        self.assertEqual(res, self.rawdata)
    self.assertEqual(binascii.a2b_uu(b'\x7f'), b'\x00' * 31)
    self.assertEqual(binascii.a2b_uu(b'\x80'), b'\x00' * 32)
    self.assertEqual(binascii.a2b_uu(b'\xff'), b'\x00' * 31)
    self.assertRaises(binascii.Error, binascii.a2b_uu, b'\xff\x00')
    self.assertRaises(binascii.Error, binascii.a2b_uu, b'!!!!')
    self.assertRaises(binascii.Error, binascii.b2a_uu, 46 * b'!')
    self.assertEqual(binascii.b2a_uu(b'x'), b'!>   \n')
    self.assertEqual(binascii.b2a_uu(b''), b' \n')
    self.assertEqual(binascii.b2a_uu(b'', backtick=True), b'`\n')
    self.assertEqual(binascii.a2b_uu(b' \n'), b'')
    self.assertEqual(binascii.a2b_uu(b'`\n'), b'')
    self.assertEqual(binascii.b2a_uu(b'\x00Cat'), b'$ $-A=   \n')
    self.assertEqual(binascii.b2a_uu(b'\x00Cat', backtick=True), b'$`$-A=```\n')
    self.assertEqual(binascii.a2b_uu(b'$`$-A=```\n'), binascii.a2b_uu(b'$ $-A=   \n'))
    with self.assertRaises(TypeError):
        binascii.b2a_uu(b'', True)
