# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_from_ssize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.type2test(0), b'')
    self.assertEqual(self.type2test(1), b'\x00')
    self.assertEqual(self.type2test(5), b'\x00\x00\x00\x00\x00')
    self.assertRaises(ValueError, self.type2test, -1)
    self.assertEqual(self.type2test('0', 'ascii'), b'0')
    self.assertEqual(self.type2test(b'0'), b'0')
    self.assertRaises(OverflowError, self.type2test, sys.maxsize + 1)
