# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_insert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = bytearray(b'msssspp')
    b.insert(1, ord('i'))
    b.insert(4, ord('i'))
    b.insert(-2, ord('i'))
    b.insert(1000, ord('i'))
    self.assertEqual(b, b'mississippi')
    self.assertRaises(TypeError, lambda : b.insert(0, b'1'))
    b = bytearray()
    b.insert(0, Indexable(ord('A')))
    self.assertEqual(b, b'A')
