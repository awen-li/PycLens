# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_blocksize_request

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    blocksize = 8
    conn = client.HTTPConnection('example.com', blocksize=blocksize)
    sock = FakeSocket(None)
    conn.sock = sock
    expected = b'a' * blocksize + b'b'
    conn.request('PUT', '/', io.BytesIO(expected), {'Content-Length': '9'})
    self.assertEqual(sock.sendall_calls, 3)
    body = sock.data.split(b'\r\n\r\n', 1)[1]
    self.assertEqual(body, expected)
