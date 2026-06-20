# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ensurepip.py
# case: TestUninstallationMainFunction_test_uninstall_version

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with test.support.captured_stdout() as stdout:
        with self.assertRaises(SystemExit):
            ensurepip._uninstall._main(['--version'])
    result = stdout.getvalue().strip()
    self.assertEqual(result, EXPECTED_VERSION_OUTPUT)
    self.assertFalse(self.run_pip.called)
