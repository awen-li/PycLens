# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_constructor_value_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(ValueError, self.type2test, [-1])
    self.assertRaises(ValueError, self.type2test, [-sys.maxsize])
    self.assertRaises(ValueError, self.type2test, [-sys.maxsize - 1])
    self.assertRaises(ValueError, self.type2test, [-sys.maxsize - 2])
    self.assertRaises(ValueError, self.type2test, [-10 ** 100])
    self.assertRaises(ValueError, self.type2test, [256])
    self.assertRaises(ValueError, self.type2test, [257])
    self.assertRaises(ValueError, self.type2test, [sys.maxsize])
    self.assertRaises(ValueError, self.type2test, [sys.maxsize + 1])
    self.assertRaises(ValueError, self.type2test, [10 ** 100])
