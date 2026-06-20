# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_module.py
# case: ModuleTests_test_module_getattr_tricky

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from test import bad_getattr3
    with self.assertRaises(AttributeError):
        bad_getattr3.one
    with self.assertRaises(AttributeError):
        bad_getattr3.delgetattr
    if 'test.bad_getattr3' in sys.modules:
        del sys.modules['test.bad_getattr3']
