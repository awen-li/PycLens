# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_profile.py
# case: ProfileTest_test_run_profile_as_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    assert_python_failure('-m', self.profilermodule.__name__, '-m')
    assert_python_failure('-m', self.profilermodule.__name__, '-m', 'random_module_xyz')
    assert_python_ok('-m', self.profilermodule.__name__, '-m', 'timeit', '-n', '1')
