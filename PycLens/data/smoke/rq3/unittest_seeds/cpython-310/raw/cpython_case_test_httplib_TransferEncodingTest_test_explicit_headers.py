# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: TransferEncodingTest_test_explicit_headers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    conn = client.HTTPConnection('example.com')
    conn.sock = FakeSocket(b'')
    conn.request('POST', '/', self._make_body(), {'Transfer-Encoding': 'chunked'})
    (_, headers, body) = self._parse_request(conn.sock.data)
    self.assertNotIn('content-length', [k.lower() for k in headers.keys()])
    self.assertEqual(headers['Transfer-Encoding'], 'chunked')
    self.assertEqual(body, self.expected_body)
    conn = client.HTTPConnection('example.com')
    conn.sock = FakeSocket(b'')
    conn.request('POST', '/', self.expected_body.decode('latin-1'), {'Transfer-Encoding': 'chunked'})
    (_, headers, body) = self._parse_request(conn.sock.data)
    self.assertNotIn('content-length', [k.lower() for k in headers.keys()])
    self.assertEqual(headers['Transfer-Encoding'], 'chunked')
    self.assertEqual(body, self.expected_body)
    conn = client.HTTPConnection('example.com')
    conn.sock = FakeSocket(b'')
    conn.request('POST', '/', headers={'Transfer-Encoding': 'gzip, chunked'}, encode_chunked=True, body=self._make_body())
    (_, headers, body) = self._parse_request(conn.sock.data)
    self.assertNotIn('content-length', [k.lower() for k in headers])
    self.assertEqual(headers['Transfer-Encoding'], 'gzip, chunked')
    self.assertEqual(self._parse_chunked(body), self.expected_body)
