# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestCommandLine_test_run_as_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    assert_python_ok('-m', 'trace', '-l', '--module', 'timeit', '-n', '1')
    assert_python_failure('-m', 'trace', '-l', '--module', 'not_a_module_zzz')
