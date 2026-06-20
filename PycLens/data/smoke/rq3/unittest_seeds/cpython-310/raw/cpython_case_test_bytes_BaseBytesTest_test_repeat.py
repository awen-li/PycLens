# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_repeat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for b in (b'abc', self.type2test(b'abc')):
        self.assertEqual(b * 3, b'abcabcabc')
        self.assertEqual(b * 0, b'')
        self.assertEqual(b * -1, b'')
        self.assertRaises(TypeError, lambda : b * 3.14)
        self.assertRaises(TypeError, lambda : 3.14 * b)
        with self.assertRaises((OverflowError, MemoryError)):
            c = b * sys.maxsize
        with self.assertRaises((OverflowError, MemoryError)):
            b *= sys.maxsize
