# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: InheritanceTest_test_get_inheritable_cloexec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock = socket.socket()
    with sock:
        fd = sock.fileno()
        self.assertEqual(sock.get_inheritable(), False)
        flags = fcntl.fcntl(fd, fcntl.F_GETFD)
        flags &= ~fcntl.FD_CLOEXEC
        fcntl.fcntl(fd, fcntl.F_SETFD, flags)
        self.assertEqual(sock.get_inheritable(), True)
