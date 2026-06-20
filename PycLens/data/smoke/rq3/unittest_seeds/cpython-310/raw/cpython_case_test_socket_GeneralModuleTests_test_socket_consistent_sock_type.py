# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_socket_consistent_sock_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    SOCK_NONBLOCK = getattr(socket, 'SOCK_NONBLOCK', 0)
    SOCK_CLOEXEC = getattr(socket, 'SOCK_CLOEXEC', 0)
    sock_type = socket.SOCK_STREAM | SOCK_NONBLOCK | SOCK_CLOEXEC
    with socket.socket(socket.AF_INET, sock_type) as s:
        self.assertEqual(s.type, socket.SOCK_STREAM)
        s.settimeout(1)
        self.assertEqual(s.type, socket.SOCK_STREAM)
        s.settimeout(0)
        self.assertEqual(s.type, socket.SOCK_STREAM)
        s.setblocking(True)
        self.assertEqual(s.type, socket.SOCK_STREAM)
        s.setblocking(False)
        self.assertEqual(s.type, socket.SOCK_STREAM)
