# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_append

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = bytearray(b'hell')
    b.append(ord('o'))
    self.assertEqual(b, b'hello')
    self.assertEqual(b.append(100), None)
    b = bytearray()
    b.append(ord('A'))
    self.assertEqual(len(b), 1)
    self.assertRaises(TypeError, lambda : b.append(b'o'))
    b = bytearray()
    b.append(Indexable(ord('A')))
    self.assertEqual(b, b'A')
