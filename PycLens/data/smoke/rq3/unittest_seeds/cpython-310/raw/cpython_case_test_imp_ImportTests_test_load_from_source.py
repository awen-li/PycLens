# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ImportTests_test_load_from_source

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    orig_path = os.path
    orig_getenv = os.getenv
    with os_helper.EnvironmentVarGuard():
        x = imp.find_module('os')
        self.addCleanup(x[0].close)
        new_os = imp.load_module('os', *x)
        self.assertIs(os, new_os)
        self.assertIs(orig_path, new_os.path)
        self.assertIsNot(orig_getenv, new_os.getenv)
