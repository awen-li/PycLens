# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: TransferEncodingTest_test_endheaders_chunked

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    conn = client.HTTPConnection('example.com')
    conn.sock = FakeSocket(b'')
    conn.putrequest('POST', '/')
    conn.endheaders(self._make_body(), encode_chunked=True)
    (_, _, body) = self._parse_request(conn.sock.data)
    body = self._parse_chunked(body)
    self.assertEqual(body, self.expected_body)
