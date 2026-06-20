# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestConflictOverride_test_conflict_override_opts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    opt = self.parser.get_option('--dry-run')
    self.assertEqual(opt._short_opts, ['-n'])
    self.assertEqual(opt._long_opts, ['--dry-run'])
