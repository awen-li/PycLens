# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPRequestHandlerTestCase_test_header_length

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.send_typical_request(b'GET / HTTP/1.1\r\nX-Foo: bar' + b'r' * 65537 + b'\r\n\r\n')
    self.assertEqual(result[0], b'HTTP/1.1 431 Line too long\r\n')
    self.assertFalse(self.handler.get_called)
    self.assertEqual(self.handler.requestline, 'GET / HTTP/1.1')
