# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_runpy.py
# case: RunModuleTestCase_test_submodule_imported_warning

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (pkg_dir, _, mod_name, _) = self._make_pkg('', 1)
    try:
        __import__(mod_name)
        with self.assertWarnsRegex(RuntimeWarning, 'found in sys\\.modules'):
            run_module(mod_name)
    finally:
        self._del_pkg(pkg_dir)
