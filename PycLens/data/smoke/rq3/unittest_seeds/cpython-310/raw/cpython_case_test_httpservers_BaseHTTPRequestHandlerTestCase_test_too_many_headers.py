# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPRequestHandlerTestCase_test_too_many_headers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.send_typical_request(b'GET / HTTP/1.1\r\n' + b'X-Foo: bar\r\n' * 101 + b'\r\n')
    self.assertEqual(result[0], b'HTTP/1.1 431 Too many headers\r\n')
    self.assertFalse(self.handler.get_called)
    self.assertEqual(self.handler.requestline, 'GET / HTTP/1.1')
