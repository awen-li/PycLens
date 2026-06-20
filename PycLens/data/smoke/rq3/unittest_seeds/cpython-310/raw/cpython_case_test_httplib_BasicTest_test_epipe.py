# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_epipe

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock = EPipeSocket('HTTP/1.0 401 Authorization Required\r\nContent-type: text/html\r\nWWW-Authenticate: Basic realm="example"\r\n', b'Content-Length')
    conn = client.HTTPConnection('example.com')
    conn.sock = sock
    self.assertRaises(OSError, lambda : conn.request('PUT', '/url', 'body'))
    resp = conn.getresponse()
    self.assertEqual(401, resp.status)
    self.assertEqual('Basic realm="example"', resp.getheader('www-authenticate'))
