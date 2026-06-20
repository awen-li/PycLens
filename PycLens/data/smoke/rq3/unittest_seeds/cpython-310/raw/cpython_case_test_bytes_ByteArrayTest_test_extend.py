# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_extend

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    orig = b'hello'
    a = bytearray(orig)
    a.extend(a)
    self.assertEqual(a, orig + orig)
    self.assertEqual(a[5:], orig)
    a = bytearray(b'')
    a.extend(map(int, orig * 25))
    a.extend((int(x) for x in orig * 25))
    self.assertEqual(a, orig * 50)
    self.assertEqual(a[-5:], orig)
    a = bytearray(b'')
    a.extend(iter(map(int, orig * 50)))
    self.assertEqual(a, orig * 50)
    self.assertEqual(a[-5:], orig)
    a = bytearray(b'')
    a.extend(list(map(int, orig * 50)))
    self.assertEqual(a, orig * 50)
    self.assertEqual(a[-5:], orig)
    a = bytearray(b'')
    self.assertRaises(ValueError, a.extend, [0, 1, 2, 256])
    self.assertRaises(ValueError, a.extend, [0, 1, 2, -1])
    self.assertEqual(len(a), 0)
    a = bytearray(b'')
    a.extend([Indexable(ord('a'))])
    self.assertEqual(a, b'a')
