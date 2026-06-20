# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socketserver.py
# case: MiscTestCase_test_threads_reaped

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
        pass
    server = MyServer((HOST, 0), socketserver.StreamRequestHandler)
    for n in range(10):
        with socket.create_connection(server.server_address):
            server.handle_request()
    self.assertLess(len(server._threads), 10)
    server.server_close()
