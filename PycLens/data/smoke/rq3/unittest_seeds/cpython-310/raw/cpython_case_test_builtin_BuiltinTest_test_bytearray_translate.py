# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_bytearray_translate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = bytearray(b'abc')
    self.assertRaises(ValueError, x.translate, b'1', 1)
    self.assertRaises(TypeError, x.translate, b'1' * 256, 1)
