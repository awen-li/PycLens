# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_getandroidapilevel

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    level = sys.getandroidapilevel()
    self.assertIsInstance(level, int)
    self.assertGreater(level, 0)
