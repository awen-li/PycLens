# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_remove

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = bytearray(b'hello')
    b.remove(ord('l'))
    self.assertEqual(b, b'helo')
    b.remove(ord('l'))
    self.assertEqual(b, b'heo')
    self.assertRaises(ValueError, lambda : b.remove(ord('l')))
    self.assertRaises(ValueError, lambda : b.remove(400))
    self.assertRaises(TypeError, lambda : b.remove('e'))
    b.remove(ord('o'))
    b.remove(ord('h'))
    self.assertEqual(b, b'e')
    self.assertRaises(TypeError, lambda : b.remove(b'e'))
    b.remove(Indexable(ord('e')))
    self.assertEqual(b, b'')
    c = bytearray([126, 127, 128, 129])
    c.remove(127)
    self.assertEqual(c, bytes([126, 128, 129]))
    c.remove(129)
    self.assertEqual(c, bytes([126, 128]))
