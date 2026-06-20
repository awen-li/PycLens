# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPRequestHandlerTestCase_test_request_length

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.send_typical_request(b'GET ' + b'x' * 65537)
    self.assertEqual(result[0], b'HTTP/1.1 414 Request-URI Too Long\r\n')
    self.assertFalse(self.handler.get_called)
    self.assertIsInstance(self.handler.requestline, str)
