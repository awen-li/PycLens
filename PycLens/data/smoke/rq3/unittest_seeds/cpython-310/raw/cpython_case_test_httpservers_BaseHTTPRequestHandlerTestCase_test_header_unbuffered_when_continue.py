# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPRequestHandlerTestCase_test_header_unbuffered_when_continue

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _readAndReseek(f):
        pos = f.tell()
        f.seek(0)
        data = f.read()
        f.seek(pos)
        return data
    input = BytesIO(b'GET / HTTP/1.1\r\nExpect: 100-continue\r\n\r\n')
    output = BytesIO()
    self.handler.rfile = input
    self.handler.wfile = output
    self.handler.request_version = 'HTTP/1.1'
    self.handler.handle_one_request()
    self.assertNotEqual(_readAndReseek(output), b'')
    result = _readAndReseek(output).split(b'\r\n')
    self.assertEqual(result[0], b'HTTP/1.1 100 Continue')
    self.assertEqual(result[1], b'')
    self.assertEqual(result[2], b'HTTP/1.1 200 OK')
