# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_unknown_socket_family_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    fd = sock.detach()
    unknown_family = max(socket.AddressFamily.__members__.values()) + 1
    unknown_type = max((kind for (name, kind) in socket.SocketKind.__members__.items() if name not in {'SOCK_NONBLOCK', 'SOCK_CLOEXEC'})) + 1
    with socket.socket(family=unknown_family, type=unknown_type, proto=23, fileno=fd) as s:
        self.assertEqual(s.family, unknown_family)
        self.assertEqual(s.type, unknown_type)
        self.assertIn(s.proto, {0, 23})
