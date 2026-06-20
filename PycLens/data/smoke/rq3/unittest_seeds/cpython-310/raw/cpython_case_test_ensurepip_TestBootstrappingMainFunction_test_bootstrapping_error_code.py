# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ensurepip.py
# case: TestBootstrappingMainFunction_test_bootstrapping_error_code

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.run_pip.return_value = 2
    exit_code = ensurepip._main([])
    self.assertEqual(exit_code, 2)
