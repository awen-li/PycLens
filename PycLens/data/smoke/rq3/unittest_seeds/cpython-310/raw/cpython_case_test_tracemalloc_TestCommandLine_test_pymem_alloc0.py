# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestCommandLine_test_pymem_alloc0

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import _testcapi; _testcapi.test_pymem_alloc0(); 1'
    assert_python_ok('-X', 'tracemalloc', '-c', code)
