# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: CreateServerTest_test_reuse_port

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not hasattr(socket, 'SO_REUSEPORT'):
        with self.assertRaises(ValueError):
            socket.create_server(('localhost', 0), reuse_port=True)
    else:
        with socket.create_server(('localhost', 0)) as sock:
            opt = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT)
            self.assertEqual(opt, 0)
        with socket.create_server(('localhost', 0), reuse_port=True) as sock:
            opt = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT)
            self.assertNotEqual(opt, 0)
