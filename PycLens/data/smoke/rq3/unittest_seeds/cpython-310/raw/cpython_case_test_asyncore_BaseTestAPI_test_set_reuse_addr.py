# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: BaseTestAPI_test_set_reuse_addr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if HAS_UNIX_SOCKETS and self.family == socket.AF_UNIX:
        self.skipTest('Not applicable to AF_UNIX sockets.')
    with socket.socket(self.family) as sock:
        try:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except OSError:
            unittest.skip('SO_REUSEADDR not supported on this platform')
        else:
            s = asyncore.dispatcher(socket.socket(self.family))
            self.assertFalse(s.socket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR))
            s.socket.close()
            s.create_socket(self.family)
            s.set_reuse_addr()
            self.assertTrue(s.socket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR))
