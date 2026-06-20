# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_module.py
# case: ModuleTests_test_uninitialized_missing_getattr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    foo = ModuleType.__new__(ModuleType)
    self.assertRaisesRegex(AttributeError, "module has no attribute 'not_here'", getattr, foo, 'not_here')
