# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_module.py
# case: ModuleTests_test_module_getattr_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import test.bad_getattr as bga
    from test import bad_getattr2
    self.assertEqual(bga.x, 1)
    self.assertEqual(bad_getattr2.x, 1)
    with self.assertRaises(TypeError):
        bga.nope
    with self.assertRaises(TypeError):
        bad_getattr2.nope
    del sys.modules['test.bad_getattr']
    if 'test.bad_getattr2' in sys.modules:
        del sys.modules['test.bad_getattr2']
