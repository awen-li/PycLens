# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_code.py
# case: CoExtra_test_free_called

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.get_func()
    SetExtra(f.__code__, FREE_INDEX, ctypes.c_voidp(100))
    del f
    self.assertEqual(LAST_FREED, 100)
