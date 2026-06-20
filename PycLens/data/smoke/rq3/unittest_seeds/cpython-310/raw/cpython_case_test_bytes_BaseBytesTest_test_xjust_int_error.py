# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_xjust_int_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, self.type2test(b'abc').center, 7, 32)
    self.assertRaises(TypeError, self.type2test(b'abc').ljust, 7, 32)
    self.assertRaises(TypeError, self.type2test(b'abc').rjust, 7, 32)
