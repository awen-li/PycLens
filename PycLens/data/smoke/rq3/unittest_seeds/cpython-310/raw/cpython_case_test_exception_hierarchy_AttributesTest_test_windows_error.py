# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exception_hierarchy.py
# case: AttributesTest_test_windows_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if os.name == 'nt':
        self.assertIn('winerror', dir(OSError))
    else:
        self.assertNotIn('winerror', dir(OSError))
