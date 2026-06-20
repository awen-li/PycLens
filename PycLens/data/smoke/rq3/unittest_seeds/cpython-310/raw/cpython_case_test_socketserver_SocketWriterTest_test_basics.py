# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socketserver.py
# case: SocketWriterTest_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Handler(socketserver.StreamRequestHandler):

        def handle(self):
            self.server.wfile = self.wfile
            self.server.wfile_fileno = self.wfile.fileno()
            self.server.request_fileno = self.request.fileno()
    server = socketserver.TCPServer((HOST, 0), Handler)
    self.addCleanup(server.server_close)
    s = socket.socket(server.address_family, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    with s:
        s.connect(server.server_address)
    server.handle_request()
    self.assertIsInstance(server.wfile, io.BufferedIOBase)
    self.assertEqual(server.wfile_fileno, server.request_fileno)
