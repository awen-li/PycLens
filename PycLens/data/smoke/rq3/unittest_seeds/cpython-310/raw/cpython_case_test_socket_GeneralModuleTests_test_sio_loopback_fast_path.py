# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_sio_loopback_fast_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = socket.socket()
    self.addCleanup(s.close)
    try:
        s.ioctl(socket.SIO_LOOPBACK_FAST_PATH, True)
    except OSError as exc:
        WSAEOPNOTSUPP = 10045
        if exc.winerror == WSAEOPNOTSUPP:
            self.skipTest("SIO_LOOPBACK_FAST_PATH is defined but doesn't implemented in this Windows version")
        raise
    self.assertRaises(TypeError, s.ioctl, socket.SIO_LOOPBACK_FAST_PATH, None)
