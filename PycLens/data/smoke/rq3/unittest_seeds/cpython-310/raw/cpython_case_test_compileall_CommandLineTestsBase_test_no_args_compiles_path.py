# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_no_args_compiles_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bazfn = script_helper.make_script(self.directory, 'baz', '')
    with self.temporary_pycache_prefix() as env:
        self.assertRunOK(**env)
        self.assertCompiled(bazfn)
        self.assertNotCompiled(self.initfn)
        self.assertNotCompiled(self.barfn)
