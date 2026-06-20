# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ensurepip.py
# case: TestUninstall_test_uninstall_skipped_with_warning_for_wrong_version

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with fake_pip('not a valid version'):
        with test.support.captured_stderr() as stderr:
            ensurepip._uninstall_helper()
    warning = stderr.getvalue().strip()
    self.assertIn('only uninstall a matching version', warning)
    self.assertFalse(self.run_pip.called)
