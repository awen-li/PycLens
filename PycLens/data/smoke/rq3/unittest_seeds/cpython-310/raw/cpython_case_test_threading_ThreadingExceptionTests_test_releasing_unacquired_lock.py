# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadingExceptionTests_test_releasing_unacquired_lock

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lock = threading.Lock()
    self.assertRaises(RuntimeError, lock.release)
