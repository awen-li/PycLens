# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: TransferEncodingTest_test_request

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for empty_lines in (False, True):
        conn = client.HTTPConnection('example.com')
        conn.sock = FakeSocket(b'')
        conn.request('POST', '/', self._make_body(empty_lines=empty_lines))
        (_, headers, body) = self._parse_request(conn.sock.data)
        body = self._parse_chunked(body)
        self.assertEqual(body, self.expected_body)
        self.assertEqual(headers['Transfer-Encoding'], 'chunked')
        self.assertNotIn('content-length', [k.lower() for k in headers])
