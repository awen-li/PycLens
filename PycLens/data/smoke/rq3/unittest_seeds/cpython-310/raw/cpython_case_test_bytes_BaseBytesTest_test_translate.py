# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_translate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test(b'hello')
    rosetta = bytearray(range(256))
    rosetta[ord('o')] = ord('e')
    self.assertRaises(TypeError, b.translate)
    self.assertRaises(TypeError, b.translate, None, None)
    self.assertRaises(ValueError, b.translate, bytes(range(255)))
    c = b.translate(rosetta, b'hello')
    self.assertEqual(b, b'hello')
    self.assertIsInstance(c, self.type2test)
    c = b.translate(rosetta)
    d = b.translate(rosetta, b'')
    self.assertEqual(c, d)
    self.assertEqual(c, b'helle')
    c = b.translate(rosetta, b'l')
    self.assertEqual(c, b'hee')
    c = b.translate(None, b'e')
    self.assertEqual(c, b'hllo')
    c = b.translate(rosetta, delete=b'')
    self.assertEqual(c, b'helle')
    c = b.translate(rosetta, delete=b'l')
    self.assertEqual(c, b'hee')
    c = b.translate(None, delete=b'e')
    self.assertEqual(c, b'hllo')
