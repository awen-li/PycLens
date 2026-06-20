# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: ForkTests_test_fork

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'if 1:\n            import os\n            from test import support\n            pid = os.fork()\n            if pid != 0:\n                support.wait_process(pid, exitcode=0)\n        '
    assert_python_ok('-c', code)
    assert_python_ok('-c', code, PYTHONMALLOC='malloc_debug')
