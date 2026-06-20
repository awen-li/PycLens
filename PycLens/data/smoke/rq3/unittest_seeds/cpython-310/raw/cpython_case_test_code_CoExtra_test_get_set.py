# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_code.py
# case: CoExtra_test_get_set

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.get_func()
    extra = ctypes.c_voidp()
    SetExtra(f.__code__, FREE_INDEX, ctypes.c_voidp(200))
    SetExtra(f.__code__, FREE_INDEX, ctypes.c_voidp(300))
    self.assertEqual(LAST_FREED, 200)
    extra = ctypes.c_voidp()
    GetExtra(f.__code__, FREE_INDEX, extra)
    self.assertEqual(extra.value, 300)
    del f
