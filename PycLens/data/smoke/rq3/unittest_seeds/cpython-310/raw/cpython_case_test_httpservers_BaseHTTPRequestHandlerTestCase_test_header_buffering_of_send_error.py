# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPRequestHandlerTestCase_test_header_buffering_of_send_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    input = BytesIO(b'GET / HTTP/1.1\r\n\r\n')
    output = AuditableBytesIO()
    handler = SocketlessRequestHandler()
    handler.rfile = input
    handler.wfile = output
    handler.request_version = 'HTTP/1.1'
    handler.requestline = ''
    handler.command = None
    handler.send_error(418)
    self.assertEqual(output.numWrites, 2)
