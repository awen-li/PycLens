# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ensurepip.py
# case: TestBootstrap_test_basic_bootstrapping

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ensurepip.bootstrap()
    self.run_pip.assert_called_once_with(['install', '--no-cache-dir', '--no-index', '--find-links', unittest.mock.ANY, 'setuptools', 'pip'], unittest.mock.ANY)
    additional_paths = self.run_pip.call_args[0][1]
    self.assertEqual(len(additional_paths), 2)
