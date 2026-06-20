# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FDInheritanceTests_test_set_inheritable_cloexec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(__file__, os.O_RDONLY)
    self.addCleanup(os.close, fd)
    self.assertEqual(fcntl.fcntl(fd, fcntl.F_GETFD) & fcntl.FD_CLOEXEC, fcntl.FD_CLOEXEC)
    os.set_inheritable(fd, True)
    self.assertEqual(fcntl.fcntl(fd, fcntl.F_GETFD) & fcntl.FD_CLOEXEC, 0)
