# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_code.py
# case: CoExtra_test_bad_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.get_func()
    self.assertRaises(SystemError, SetExtra, f.__code__, FREE_INDEX + 100, ctypes.c_voidp(100))
    self.assertEqual(GetExtra(f.__code__, FREE_INDEX + 100, ctypes.c_voidp(100)), 0)
