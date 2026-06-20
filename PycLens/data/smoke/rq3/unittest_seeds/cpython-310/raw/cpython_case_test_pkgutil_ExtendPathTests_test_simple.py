# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkgutil.py
# case: ExtendPathTests_test_simple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pkgname = 'foo'
    dirname_0 = self.create_init(pkgname)
    dirname_1 = self.create_init(pkgname)
    self.create_submodule(dirname_0, pkgname, 'bar', 0)
    self.create_submodule(dirname_1, pkgname, 'baz', 1)
    import foo.bar
    import foo.baz
    self.assertEqual(foo.bar.value, 0)
    self.assertEqual(foo.baz.value, 1)
    self.assertEqual(sorted(foo.__path__), sorted([os.path.join(dirname_0, pkgname), os.path.join(dirname_1, pkgname)]))
    shutil.rmtree(dirname_0)
    shutil.rmtree(dirname_1)
    del sys.path[0]
    del sys.path[0]
    del sys.modules['foo']
    del sys.modules['foo.bar']
    del sys.modules['foo.baz']
