# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_debug_deprecation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = assert_python_ok('-Wdefault', '-c', 'pass', PYTHONTHREADDEBUG='1')
    msg = b'DeprecationWarning: The threading debug (PYTHONTHREADDEBUG environment variable) is deprecated and will be removed in Python 3.12'
    self.assertIn(msg, err)
