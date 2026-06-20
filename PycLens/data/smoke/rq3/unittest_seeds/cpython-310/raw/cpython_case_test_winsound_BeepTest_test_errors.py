# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winsound.py
# case: BeepTest_test_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, winsound.Beep)
    self.assertRaises(ValueError, winsound.Beep, 36, 75)
    self.assertRaises(ValueError, winsound.Beep, 32768, 75)
