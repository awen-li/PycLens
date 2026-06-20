# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_fromhex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, self.type2test.fromhex)
    self.assertRaises(TypeError, self.type2test.fromhex, 1)
    self.assertEqual(self.type2test.fromhex(''), self.type2test())
    b = bytearray([26, 43, 48])
    self.assertEqual(self.type2test.fromhex('1a2B30'), b)
    self.assertEqual(self.type2test.fromhex('  1A 2B  30   '), b)
    self.assertEqual(self.type2test.fromhex(' 1A\n2B\t30\x0b'), b)
    for c in '\t\n\x0b\x0c\r ':
        self.assertEqual(self.type2test.fromhex(c), self.type2test())
    for c in '\x1c\x1d\x1e\x1f\x85\xa0\u2000\u2002\u2028':
        self.assertRaises(ValueError, self.type2test.fromhex, c)
    self.assertEqual(self.type2test.fromhex('0000'), b'\x00\x00')
    self.assertRaises(TypeError, self.type2test.fromhex, b'1B')
    self.assertRaises(ValueError, self.type2test.fromhex, 'a')
    self.assertRaises(ValueError, self.type2test.fromhex, 'rt')
    self.assertRaises(ValueError, self.type2test.fromhex, '1a b cd')
    self.assertRaises(ValueError, self.type2test.fromhex, '\x00')
    self.assertRaises(ValueError, self.type2test.fromhex, '12   \x00   34')
    for (data, pos) in (('12 x4 56', 3), ('12 3x 56', 4), ('12 xy 56', 3), ('12 3ÿ 56', 4)):
        with self.assertRaises(ValueError) as cm:
            self.type2test.fromhex(data)
        self.assertIn('at position %s' % pos, str(cm.exception))
