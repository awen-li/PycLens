# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fcntl.py
# case: TestFcntl_test_flock

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.f = open(TESTFN, 'wb+')
    fileno = self.f.fileno()
    fcntl.flock(fileno, fcntl.LOCK_SH)
    fcntl.flock(fileno, fcntl.LOCK_UN)
    fcntl.flock(self.f, fcntl.LOCK_SH | fcntl.LOCK_NB)
    fcntl.flock(self.f, fcntl.LOCK_UN)
    fcntl.flock(fileno, fcntl.LOCK_EX)
    fcntl.flock(fileno, fcntl.LOCK_UN)
    self.assertRaises(ValueError, fcntl.flock, -1, fcntl.LOCK_SH)
    self.assertRaises(TypeError, fcntl.flock, 'spam', fcntl.LOCK_SH)
