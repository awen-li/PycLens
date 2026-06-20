# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_runpy.py
# case: RunModuleTestCase_test_package_imported_no_warning

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (pkg_dir, _, mod_name, _) = self._make_pkg('', 1, '__main__')
    self.addCleanup(self._del_pkg, pkg_dir)
    package = mod_name.replace('.__main__', '')
    __import__(package)
    self.assertIn(package, sys.modules)
    with warnings.catch_warnings():
        warnings.simplefilter('error', RuntimeWarning)
        run_module(package)
    __import__(mod_name)
    with self.assertWarnsRegex(RuntimeWarning, 'found in sys\\.modules'):
        run_module(package)
