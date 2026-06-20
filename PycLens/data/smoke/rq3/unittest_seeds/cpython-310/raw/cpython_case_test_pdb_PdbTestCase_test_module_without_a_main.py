# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pdb.py
# case: PdbTestCase_test_module_without_a_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    module_name = 't_main'
    os_helper.rmtree(module_name)
    init_file = module_name + '/__init__.py'
    os.mkdir(module_name)
    with open(init_file, 'w'):
        pass
    self.addCleanup(os_helper.rmtree, module_name)
    (stdout, stderr) = self._run_pdb(['-m', module_name], '')
    self.assertIn('ImportError: No module named t_main.__main__', stdout.splitlines())
