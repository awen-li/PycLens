# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_send_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = b'GET /foo HTTP/1.1\r\nHost: example.com\r\nAccept-Encoding: identity\r\nTransfer-Encoding: chunked\r\n\r\n'
    with open(__file__, 'rb') as body:
        conn = client.HTTPConnection('example.com')
        sock = FakeSocket(body)
        conn.sock = sock
        conn.request('GET', '/foo', body)
        self.assertTrue(sock.data.startswith(expected), '%r != %r' % (sock.data[:len(expected)], expected))
