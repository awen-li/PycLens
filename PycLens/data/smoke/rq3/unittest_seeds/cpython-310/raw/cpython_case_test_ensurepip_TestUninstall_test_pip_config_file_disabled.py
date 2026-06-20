# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ensurepip.py
# case: TestUninstall_test_pip_config_file_disabled

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with fake_pip():
        ensurepip._uninstall_helper()
    self.assertEqual(self.os_environ['PIP_CONFIG_FILE'], os.devnull)
