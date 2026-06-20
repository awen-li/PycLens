# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestCommandLine_test_env_var_ignored_with_E

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import tracemalloc; print(tracemalloc.is_tracing())'
    (ok, stdout, stderr) = assert_python_ok('-E', '-c', code, PYTHONTRACEMALLOC='1')
    stdout = stdout.rstrip()
    self.assertEqual(stdout, b'False')
