# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socketserver.py
# case: SocketServerTest_test_ForkingUDPServer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with simple_subprocess(self):
        self.run_server(socketserver.ForkingUDPServer, socketserver.DatagramRequestHandler, self.dgram_examine)
