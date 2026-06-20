# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: HeaderTests_test_headers_debuglevel

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    body = b'HTTP/1.1 200 OK\r\nFirst: val\r\nSecond: val1\r\nSecond: val2\r\n'
    sock = FakeSocket(body)
    resp = client.HTTPResponse(sock, debuglevel=1)
    with support.captured_stdout() as output:
        resp.begin()
    lines = output.getvalue().splitlines()
    self.assertEqual(lines[0], "reply: 'HTTP/1.1 200 OK\\r\\n'")
    self.assertEqual(lines[1], 'header: First: val')
    self.assertEqual(lines[2], 'header: Second: val1')
    self.assertEqual(lines[3], 'header: Second: val2')
