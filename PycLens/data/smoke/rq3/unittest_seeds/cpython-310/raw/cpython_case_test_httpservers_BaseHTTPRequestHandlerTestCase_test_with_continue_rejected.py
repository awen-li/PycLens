# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPRequestHandlerTestCase_test_with_continue_rejected

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    usual_handler = self.handler
    self.handler = RejectingSocketlessRequestHandler()
    result = self.send_typical_request(b'GET / HTTP/1.1\r\nExpect: 100-continue\r\n\r\n')
    self.assertEqual(result[0], b'HTTP/1.1 417 Expectation Failed\r\n')
    self.verify_expected_headers(result[1:-1])
    self.assertFalse(self.handler.get_called)
    self.assertEqual(sum((r == b'Connection: close\r\n' for r in result[1:-1])), 1)
    self.handler = usual_handler
