# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_socket_fileno_rejects_invalid_socket

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(ValueError, 'negative file descriptor'):
        socket.socket(socket.AF_INET, socket.SOCK_STREAM, fileno=-1)
