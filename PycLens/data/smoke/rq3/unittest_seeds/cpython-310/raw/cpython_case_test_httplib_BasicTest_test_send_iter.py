# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_send_iter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = b'GET /foo HTTP/1.1\r\nHost: example.com\r\nAccept-Encoding: identity\r\nContent-Length: 11\r\n\r\nonetwothree'

    def body():
        yield b'one'
        yield b'two'
        yield b'three'
    conn = client.HTTPConnection('example.com')
    sock = FakeSocket('')
    conn.sock = sock
    conn.request('GET', '/foo', body(), {'Content-Length': '11'})
    self.assertEqual(sock.data, expected)
