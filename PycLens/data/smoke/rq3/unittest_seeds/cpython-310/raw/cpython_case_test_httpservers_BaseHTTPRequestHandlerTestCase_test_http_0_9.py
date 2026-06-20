# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPRequestHandlerTestCase_test_http_0_9

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.send_typical_request(b'GET / HTTP/0.9\r\n\r\n')
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0], b'<html><body>Data</body></html>\r\n')
    self.verify_get_called()
