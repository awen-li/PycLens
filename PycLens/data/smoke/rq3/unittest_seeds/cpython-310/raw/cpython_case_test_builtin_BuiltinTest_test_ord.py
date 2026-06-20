# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_ord

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(ord(' '), 32)
    self.assertEqual(ord('A'), 65)
    self.assertEqual(ord('a'), 97)
    self.assertEqual(ord('\x80'), 128)
    self.assertEqual(ord('ÿ'), 255)
    self.assertEqual(ord(b' '), 32)
    self.assertEqual(ord(b'A'), 65)
    self.assertEqual(ord(b'a'), 97)
    self.assertEqual(ord(b'\x80'), 128)
    self.assertEqual(ord(b'\xff'), 255)
    self.assertEqual(ord(chr(sys.maxunicode)), sys.maxunicode)
    self.assertRaises(TypeError, ord, 42)
    self.assertEqual(ord(chr(1114111)), 1114111)
    self.assertEqual(ord('\uffff'), 65535)
    self.assertEqual(ord('𐀀'), 65536)
    self.assertEqual(ord('𐀁'), 65537)
    self.assertEqual(ord('\U000ffffe'), 1048574)
    self.assertEqual(ord('\U000fffff'), 1048575)
    self.assertEqual(ord('\U00100000'), 1048576)
    self.assertEqual(ord('\U00100001'), 1048577)
    self.assertEqual(ord('\U0010fffe'), 1114110)
    self.assertEqual(ord('\U0010ffff'), 1114111)
