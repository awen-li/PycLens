# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ensurepip.py
# case: TestUninstall_test_uninstall

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with fake_pip():
        ensurepip._uninstall_helper()
    self.run_pip.assert_called_once_with(['uninstall', '-y', '--disable-pip-version-check', 'pip', 'setuptools'])
