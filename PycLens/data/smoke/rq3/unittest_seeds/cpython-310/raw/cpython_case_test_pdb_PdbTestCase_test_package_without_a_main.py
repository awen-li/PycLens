# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_package_without_a_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pkg_name = 't_pkg'
    module_name = 't_main'
    os_helper.rmtree(pkg_name)
    modpath = pkg_name + '/' + module_name
    os.makedirs(modpath)
    with open(modpath + '/__init__.py', 'w'):
        pass
    self.addCleanup(os_helper.rmtree, pkg_name)
    (stdout, stderr) = self._run_pdb(['-m', modpath.replace('/', '.')], '')
    self.assertIn("'t_pkg.t_main' is a package and cannot be directly executed", stdout)
