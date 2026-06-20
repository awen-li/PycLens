# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkgutil.py
# case: NestedNamespacePackageTest_test_nested

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pkgutil_boilerplate = 'import pkgutil; __path__ = pkgutil.extend_path(__path__, __name__)'
    self.create_module('a.pkg.__init__', pkgutil_boilerplate)
    self.create_module('b.pkg.__init__', pkgutil_boilerplate)
    self.create_module('a.pkg.subpkg.__init__', pkgutil_boilerplate)
    self.create_module('b.pkg.subpkg.__init__', pkgutil_boilerplate)
    self.create_module('a.pkg.subpkg.c', 'c = 1')
    self.create_module('b.pkg.subpkg.d', 'd = 2')
    sys.path.insert(0, os.path.join(self.basedir, 'a'))
    sys.path.insert(0, os.path.join(self.basedir, 'b'))
    import pkg
    self.addCleanup(unload, 'pkg')
    self.assertEqual(len(pkg.__path__), 2)
    import pkg.subpkg
    self.addCleanup(unload, 'pkg.subpkg')
    self.assertEqual(len(pkg.subpkg.__path__), 2)
    from pkg.subpkg.c import c
    from pkg.subpkg.d import d
    self.assertEqual(c, 1)
    self.assertEqual(d, 2)
