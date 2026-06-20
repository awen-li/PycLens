# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_change_cwd__non_existent_dir__quiet_true

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    original_cwd = os.getcwd()
    with os_helper.temp_dir() as parent_dir:
        bad_dir = os.path.join(parent_dir, 'does_not_exist')
        with warnings_helper.check_warnings() as recorder:
            with os_helper.change_cwd(bad_dir, quiet=True) as new_cwd:
                self.assertEqual(new_cwd, original_cwd)
                self.assertEqual(os.getcwd(), new_cwd)
            warnings = [str(w.message) for w in recorder.warnings]
    self.assertEqual(len(warnings), 1, warnings)
    warn = warnings[0]
    self.assertTrue(warn.startswith(f'tests may fail, unable to change the current working directory to {bad_dir!r}: '), warn)
