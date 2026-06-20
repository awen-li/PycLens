# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_module.py
# case: ModuleTests_test_module_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import test.good_getattr as gga
    self.assertEqual(dir(gga), ['a', 'b', 'c'])
    del sys.modules['test.good_getattr']
