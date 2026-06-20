# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_blocksize_send

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    blocksize = 8
    conn = client.HTTPConnection('example.com', blocksize=blocksize)
    sock = FakeSocket(None)
    conn.sock = sock
    expected = b'a' * blocksize + b'b'
    conn.send(io.BytesIO(expected))
    self.assertEqual(sock.sendall_calls, 2)
    self.assertEqual(sock.data, expected)
