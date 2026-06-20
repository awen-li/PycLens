# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_chr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(chr(32), ' ')
    self.assertEqual(chr(65), 'A')
    self.assertEqual(chr(97), 'a')
    self.assertEqual(chr(255), 'ÿ')
    self.assertRaises(ValueError, chr, 1 << 24)
    self.assertEqual(chr(sys.maxunicode), str('\\U0010ffff'.encode('ascii'), 'unicode-escape'))
    self.assertRaises(TypeError, chr)
    self.assertEqual(chr(65535), '\uffff')
    self.assertEqual(chr(65536), '𐀀')
    self.assertEqual(chr(65537), '𐀁')
    self.assertEqual(chr(1048574), '\U000ffffe')
    self.assertEqual(chr(1048575), '\U000fffff')
    self.assertEqual(chr(1048576), '\U00100000')
    self.assertEqual(chr(1048577), '\U00100001')
    self.assertEqual(chr(1114110), '\U0010fffe')
    self.assertEqual(chr(1114111), '\U0010ffff')
    self.assertRaises(ValueError, chr, -1)
    self.assertRaises(ValueError, chr, 1114112)
    self.assertRaises((OverflowError, ValueError), chr, 2 ** 32)
