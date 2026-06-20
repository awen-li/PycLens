# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_module.py
# case: ModuleTests_test_module_getattr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import test.good_getattr as gga
    from test.good_getattr import test
    self.assertEqual(test, 'There is test')
    self.assertEqual(gga.x, 1)
    self.assertEqual(gga.y, 2)
    with self.assertRaisesRegex(AttributeError, 'Deprecated, use whatever instead'):
        gga.yolo
    self.assertEqual(gga.whatever, 'There is whatever')
    del sys.modules['test.good_getattr']
