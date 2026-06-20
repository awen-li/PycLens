# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_signal.py
# case: WakeupFDTests_test_set_wakeup_fd_socket_result

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock1 = socket.socket()
    self.addCleanup(sock1.close)
    sock1.setblocking(False)
    fd1 = sock1.fileno()
    sock2 = socket.socket()
    self.addCleanup(sock2.close)
    sock2.setblocking(False)
    fd2 = sock2.fileno()
    signal.set_wakeup_fd(fd1)
    self.assertEqual(signal.set_wakeup_fd(fd2), fd1)
    self.assertEqual(signal.set_wakeup_fd(-1), fd2)
    self.assertEqual(signal.set_wakeup_fd(-1), -1)
