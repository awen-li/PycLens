# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ensurepip.py
# case: TestBootstrappingMainFunction_test_basic_bootstrapping

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exit_code = ensurepip._main([])
    self.run_pip.assert_called_once_with(['install', '--no-cache-dir', '--no-index', '--find-links', unittest.mock.ANY, 'setuptools', 'pip'], unittest.mock.ANY)
    additional_paths = self.run_pip.call_args[0][1]
    self.assertEqual(len(additional_paths), 2)
    self.assertEqual(exit_code, 0)
