# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_empty_sequence

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test()
    self.assertEqual(len(b), 0)
    self.assertRaises(IndexError, lambda : b[0])
    self.assertRaises(IndexError, lambda : b[1])
    self.assertRaises(IndexError, lambda : b[sys.maxsize])
    self.assertRaises(IndexError, lambda : b[sys.maxsize + 1])
    self.assertRaises(IndexError, lambda : b[10 ** 100])
    self.assertRaises(IndexError, lambda : b[-1])
    self.assertRaises(IndexError, lambda : b[-2])
    self.assertRaises(IndexError, lambda : b[-sys.maxsize])
    self.assertRaises(IndexError, lambda : b[-sys.maxsize - 1])
    self.assertRaises(IndexError, lambda : b[-sys.maxsize - 2])
    self.assertRaises(IndexError, lambda : b[-10 ** 100])
