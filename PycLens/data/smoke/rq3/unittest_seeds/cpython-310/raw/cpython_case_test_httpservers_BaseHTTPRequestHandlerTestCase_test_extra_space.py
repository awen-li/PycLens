# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPRequestHandlerTestCase_test_extra_space

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.send_typical_request(b'GET /spaced out HTTP/1.1\r\nHost: dummy\r\n\r\n')
    self.assertTrue(result[0].startswith(b'HTTP/1.1 400 '))
    self.verify_expected_headers(result[1:result.index(b'\r\n')])
    self.assertFalse(self.handler.get_called)
