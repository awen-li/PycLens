# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_module.py
# case: ModuleTests_test_module_dir_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import test.bad_getattr as bga
    from test import bad_getattr2
    with self.assertRaises(TypeError):
        dir(bga)
    with self.assertRaises(TypeError):
        dir(bad_getattr2)
    del sys.modules['test.bad_getattr']
    if 'test.bad_getattr2' in sys.modules:
        del sys.modules['test.bad_getattr2']
