# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: HeaderTests_test_malformed_headers_coped_with

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    body = 'HTTP/1.1 200 OK\r\nFirst: val\r\n: nval\r\nSecond: val\r\n\r\n'
    sock = FakeSocket(body)
    resp = client.HTTPResponse(sock)
    resp.begin()
    self.assertEqual(resp.getheader('First'), 'val')
    self.assertEqual(resp.getheader('Second'), 'val')
