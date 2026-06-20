# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_getframe

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, sys._getframe, 42, 42)
    self.assertRaises(ValueError, sys._getframe, 2000000000)
    self.assertTrue(SysModuleTest.test_getframe.__code__ is sys._getframe().f_code)
