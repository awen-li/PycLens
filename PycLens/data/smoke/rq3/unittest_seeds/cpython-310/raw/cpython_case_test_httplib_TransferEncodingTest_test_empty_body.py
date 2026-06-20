# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: TransferEncodingTest_test_empty_body

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    conn = client.HTTPConnection('example.com')
    conn.sock = FakeSocket(b'')
    conn.request('POST', '/', ())
    (_, headers, body) = self._parse_request(conn.sock.data)
    self.assertEqual(headers['Transfer-Encoding'], 'chunked')
    self.assertNotIn('content-length', [k.lower() for k in headers])
    self.assertEqual(body, b'0\r\n\r\n')
