# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_socket_fileno_requires_valid_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    WSAENOTSOCK = 10038
    with self.assertRaises(OSError) as cm:
        socket.socket(fileno=os_helper.make_bad_fd())
    self.assertIn(cm.exception.errno, (errno.EBADF, WSAENOTSOCK))
    with self.assertRaises(OSError) as cm:
        socket.socket(socket.AF_INET, socket.SOCK_STREAM, fileno=os_helper.make_bad_fd())
    self.assertIn(cm.exception.errno, (errno.EBADF, WSAENOTSOCK))
