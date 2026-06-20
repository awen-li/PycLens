# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socketserver.py
# case: MiscTestCase_test_shutdown_request_called_if_verify_request_false

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyServer(socketserver.TCPServer):

        def verify_request(self, request, client_address):
            return False
        shutdown_called = 0

        def shutdown_request(self, request):
            self.shutdown_called += 1
            socketserver.TCPServer.shutdown_request(self, request)
    server = MyServer((HOST, 0), socketserver.StreamRequestHandler)
    s = socket.socket(server.address_family, socket.SOCK_STREAM)
    s.connect(server.server_address)
    s.close()
    server.handle_request()
    self.assertEqual(server.shutdown_called, 1)
    server.server_close()
