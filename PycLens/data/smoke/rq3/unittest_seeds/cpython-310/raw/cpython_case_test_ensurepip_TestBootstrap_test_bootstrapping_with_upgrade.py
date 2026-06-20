# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ensurepip.py
# case: TestBootstrap_test_bootstrapping_with_upgrade

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ensurepip.bootstrap(upgrade=True)
    self.run_pip.assert_called_once_with(['install', '--no-cache-dir', '--no-index', '--find-links', unittest.mock.ANY, '--upgrade', 'setuptools', 'pip'], unittest.mock.ANY)
