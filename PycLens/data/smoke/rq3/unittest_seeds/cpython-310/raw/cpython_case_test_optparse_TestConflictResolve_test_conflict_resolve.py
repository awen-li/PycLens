# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestConflictResolve_test_conflict_resolve

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    v_opt = self.parser.get_option('-v')
    verbose_opt = self.parser.get_option('--verbose')
    version_opt = self.parser.get_option('--version')
    self.assertTrue(v_opt is version_opt)
    self.assertTrue(v_opt is not verbose_opt)
    self.assertEqual(v_opt._long_opts, ['--version'])
    self.assertEqual(version_opt._short_opts, ['-v'])
    self.assertEqual(version_opt._long_opts, ['--version'])
    self.assertEqual(verbose_opt._short_opts, [])
    self.assertEqual(verbose_opt._long_opts, ['--verbose'])
