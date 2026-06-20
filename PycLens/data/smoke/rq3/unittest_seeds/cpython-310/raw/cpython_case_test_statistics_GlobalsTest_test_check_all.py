# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: GlobalsTest_test_check_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    module = self.module
    for name in module.__all__:
        self.assertFalse(name.startswith('_'), 'private name "%s" in __all__' % name)
        self.assertTrue(hasattr(module, name), 'missing name "%s" in __all__' % name)
