# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_runpy.py
# case: RunModuleTestCase_test_run_package_init_exceptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self._make_pkg('', 1, '__main__')
    (pkg_dir, _, mod_name, _) = result
    mod_name = mod_name.replace('.__main__', '')
    self.addCleanup(self._del_pkg, pkg_dir)
    init = os.path.join(pkg_dir, '__runpy_pkg__', '__init__.py')
    exceptions = (ImportError, AttributeError, TypeError, ValueError)
    for exception in exceptions:
        name = exception.__name__
        with self.subTest(name):
            source = "raise {0}('{0} in __init__.py.')".format(name)
            with open(init, 'wt', encoding='ascii') as mod_file:
                mod_file.write(source)
            try:
                run_module(mod_name)
            except exception as err:
                self.assertNotIn('finding spec', format(err))
            else:
                self.fail('Nothing raised; expected {}'.format(name))
            try:
                run_module(mod_name + '.submodule')
            except exception as err:
                self.assertNotIn('finding spec', format(err))
            else:
                self.fail('Nothing raised; expected {}'.format(name))
