# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_no_args_respects_quiet_flag

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script_helper.make_script(self.directory, 'baz', '')
    with self.temporary_pycache_prefix() as env:
        noisy = self.assertRunOK(**env)
    self.assertIn(b'Listing ', noisy)
    quiet = self.assertRunOK('-q', **env)
    self.assertNotIn(b'Listing ', quiet)
