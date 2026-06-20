# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPRequestHandlerTestCase_test_http_1_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.send_typical_request(b'GET / HTTP/1.1\r\n\r\n')
    self.verify_http_server_response(result[0])
    self.verify_expected_headers(result[1:-1])
    self.verify_get_called()
    self.assertEqual(result[-1], b'<html><body>Data</body></html>\r\n')
    self.assertEqual(self.handler.requestline, 'GET / HTTP/1.1')
    self.assertEqual(self.handler.command, 'GET')
    self.assertEqual(self.handler.path, '/')
    self.assertEqual(self.handler.request_version, 'HTTP/1.1')
    self.assertSequenceEqual(self.handler.headers.items(), ())
