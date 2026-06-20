# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_sock_ioctl

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(hasattr(socket.socket, 'ioctl'))
    self.assertTrue(hasattr(socket, 'SIO_RCVALL'))
    self.assertTrue(hasattr(socket, 'RCVALL_ON'))
    self.assertTrue(hasattr(socket, 'RCVALL_OFF'))
    self.assertTrue(hasattr(socket, 'SIO_KEEPALIVE_VALS'))
    s = socket.socket()
    self.addCleanup(s.close)
    self.assertRaises(ValueError, s.ioctl, -1, None)
    s.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 100, 100))
