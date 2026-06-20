# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: RequestBodyTest_test_list_body

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cases = (([b'foo', b'bar'], b'3\r\nfoo\r\n3\r\nbar\r\n0\r\n\r\n'), ((b'foo', b'bar'), b'3\r\nfoo\r\n3\r\nbar\r\n0\r\n\r\n'))
    for (body, expected) in cases:
        with self.subTest(body):
            self.conn = client.HTTPConnection('example.com')
            self.conn.sock = self.sock = FakeSocket('')
            self.conn.request('PUT', '/url', body)
            (msg, f) = self.get_headers_and_fp()
            self.assertNotIn('Content-Type', msg)
            self.assertNotIn('Content-Length', msg)
            self.assertEqual(msg.get('Transfer-Encoding'), 'chunked')
            self.assertEqual(expected, f.read())
