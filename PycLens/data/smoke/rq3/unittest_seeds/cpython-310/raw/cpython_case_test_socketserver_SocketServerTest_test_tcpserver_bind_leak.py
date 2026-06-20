# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socketserver.py
# case: SocketServerTest_test_tcpserver_bind_leak

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(1024):
        with self.assertRaises(OverflowError):
            socketserver.TCPServer((HOST, -1), socketserver.StreamRequestHandler)
