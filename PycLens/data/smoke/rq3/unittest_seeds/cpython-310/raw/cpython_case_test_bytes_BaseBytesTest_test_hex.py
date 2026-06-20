# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_hex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, self.type2test.hex)
    self.assertRaises(TypeError, self.type2test.hex, 1)
    self.assertEqual(self.type2test(b'').hex(), '')
    self.assertEqual(bytearray([26, 43, 48]).hex(), '1a2b30')
    self.assertEqual(self.type2test(b'\x1a+0').hex(), '1a2b30')
    self.assertEqual(memoryview(b'\x1a+0').hex(), '1a2b30')
