# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_run_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    assert_python_failure('-m')
    assert_python_failure('-m', 'fnord43520xyz')
    assert_python_failure('-m', 'runpy', 'fnord43520xyz')
    assert_python_ok('-m', 'timeit', '-n', '1')
