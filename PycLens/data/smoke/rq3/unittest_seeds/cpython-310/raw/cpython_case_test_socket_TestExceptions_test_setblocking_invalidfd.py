# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: TestExceptions_test_setblocking_invalidfd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0, sock0.fileno())
    sock0.close()
    self.addCleanup(sock.detach)
    with self.assertRaises(OSError):
        sock.setblocking(False)
