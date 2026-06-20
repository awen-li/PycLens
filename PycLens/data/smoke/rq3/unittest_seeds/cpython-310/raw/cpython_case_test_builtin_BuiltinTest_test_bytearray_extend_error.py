# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_bytearray_extend_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    array = bytearray()
    bad_iter = map(int, 'X')
    self.assertRaises(ValueError, array.extend, bad_iter)
