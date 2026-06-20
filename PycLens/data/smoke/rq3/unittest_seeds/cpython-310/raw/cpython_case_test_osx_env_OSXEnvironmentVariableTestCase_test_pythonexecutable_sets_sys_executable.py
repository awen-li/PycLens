# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_osx_env.py
# case: OSXEnvironmentVariableTestCase_test_pythonexecutable_sets_sys_executable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._check_sys('PYTHONEXECUTABLE', '==', 'sys.executable')
