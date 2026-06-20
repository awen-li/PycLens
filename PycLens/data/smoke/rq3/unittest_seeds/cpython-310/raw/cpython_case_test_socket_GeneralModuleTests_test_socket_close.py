# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_socket_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock = socket.socket()
    try:
        sock.bind((HOST, 0))
        socket.close(sock.fileno())
        with self.assertRaises(OSError):
            sock.listen(1)
    finally:
        with self.assertRaises(OSError):
            sock.close()
    with self.assertRaises(TypeError):
        socket.close(None)
    with self.assertRaises(OSError):
        socket.close(-1)
