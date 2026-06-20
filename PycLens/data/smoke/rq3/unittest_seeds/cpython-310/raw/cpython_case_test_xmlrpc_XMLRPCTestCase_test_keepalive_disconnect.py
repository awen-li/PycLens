# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: XMLRPCTestCase_test_keepalive_disconnect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class RequestHandler(http.server.BaseHTTPRequestHandler):
        protocol_version = 'HTTP/1.1'
        handled = False

        def do_POST(self):
            length = int(self.headers.get('Content-Length'))
            self.rfile.read(length)
            if self.handled:
                self.close_connection = True
                return
            response = xmlrpclib.dumps((5,), methodresponse=True)
            response = response.encode()
            self.send_response(http.HTTPStatus.OK)
            self.send_header('Content-Length', len(response))
            self.end_headers()
            self.wfile.write(response)
            self.handled = True
            self.close_connection = False

        def log_message(self, format, *args):
            pass

    def run_server():
        server.socket.settimeout(float(1))
        server.handle_request()
        server.handle_request()
    server = http.server.HTTPServer((socket_helper.HOST, 0), RequestHandler)
    self.addCleanup(server.server_close)
    thread = threading.Thread(target=run_server)
    thread.start()
    self.addCleanup(thread.join)
    url = 'http://{}:{}/'.format(*server.server_address)
    with xmlrpclib.ServerProxy(url) as p:
        self.assertEqual(p.method(), 5)
        self.assertEqual(p.method(), 5)
