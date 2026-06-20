# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_runpy.py
# case: RunModuleTestCase_test_pkgutil_walk_packages

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import pkgutil
    max_depth = 4
    base_name = '__runpy_pkg__'
    package_suffixes = ['uncle', 'uncle.cousin']
    module_suffixes = ['uncle.cousin.nephew', base_name + '.sibling']
    expected_packages = set()
    expected_modules = set()
    for depth in range(1, max_depth):
        pkg_name = '.'.join([base_name] * depth)
        expected_packages.add(pkg_name)
        for name in package_suffixes:
            expected_packages.add(pkg_name + '.' + name)
        for name in module_suffixes:
            expected_modules.add(pkg_name + '.' + name)
    pkg_name = '.'.join([base_name] * max_depth)
    expected_packages.add(pkg_name)
    expected_modules.add(pkg_name + '.runpy_test')
    (pkg_dir, mod_fname, mod_name, mod_spec) = self._make_pkg('', max_depth)
    self.addCleanup(self._del_pkg, pkg_dir)
    for depth in range(2, max_depth + 1):
        self._add_relative_modules(pkg_dir, '', depth)
    for moduleinfo in pkgutil.walk_packages([pkg_dir]):
        self.assertIsInstance(moduleinfo, pkgutil.ModuleInfo)
        self.assertIsInstance(moduleinfo.module_finder, importlib.machinery.FileFinder)
        if moduleinfo.ispkg:
            expected_packages.remove(moduleinfo.name)
        else:
            expected_modules.remove(moduleinfo.name)
    self.assertEqual(len(expected_packages), 0, expected_packages)
    self.assertEqual(len(expected_modules), 0, expected_modules)
