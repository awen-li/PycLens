# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ensurepip.py
# case: TestUninstall_test_pip_environment_variables_removed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.os_environ['PIP_THIS_SHOULD_GO_AWAY'] = 'test fodder'
    with fake_pip():
        ensurepip._uninstall_helper()
    self.assertNotIn('PIP_THIS_SHOULD_GO_AWAY', self.os_environ)
