# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_strip_int_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, self.type2test(b' abc ').strip, 32)
    self.assertRaises(TypeError, self.type2test(b' abc ').lstrip, 32)
    self.assertRaises(TypeError, self.type2test(b' abc ').rstrip, 32)
