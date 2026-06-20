# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_SocketType_is_socketobject

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _socket
    self.assertTrue(socket.SocketType is _socket.socket)
    s = socket.socket()
    self.assertIsInstance(s, socket.SocketType)
    s.close()
