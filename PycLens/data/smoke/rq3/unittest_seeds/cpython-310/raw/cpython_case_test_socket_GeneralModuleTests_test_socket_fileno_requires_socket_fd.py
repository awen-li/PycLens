# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_socket_fileno_requires_socket_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tempfile.NamedTemporaryFile() as afile:
        with self.assertRaises(OSError):
            socket.socket(fileno=afile.fileno())
        with self.assertRaises(OSError) as cm:
            socket.socket(socket.AF_INET, socket.SOCK_STREAM, fileno=afile.fileno())
        self.assertEqual(cm.exception.errno, errno.ENOTSOCK)
