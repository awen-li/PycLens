# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socketserver.py
# case: SocketServerTest_test_ThreadingUnixDatagramServer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.run_server(socketserver.ThreadingUnixDatagramServer, socketserver.DatagramRequestHandler, self.dgram_examine)
