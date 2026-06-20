# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_readinto_chunked_head

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    chunked_start = 'HTTP/1.1 200 OK\r\nTransfer-Encoding: chunked\r\n\r\na\r\nhello world\r\n1\r\nd\r\n'
    sock = FakeSocket(chunked_start + last_chunk + chunked_end)
    resp = client.HTTPResponse(sock, method='HEAD')
    resp.begin()
    b = bytearray(5)
    n = resp.readinto(b)
    self.assertEqual(n, 0)
    self.assertEqual(bytes(b), b'\x00' * 5)
    self.assertEqual(resp.status, 200)
    self.assertEqual(resp.reason, 'OK')
    self.assertTrue(resp.isclosed())
    self.assertFalse(resp.closed)
    resp.close()
    self.assertTrue(resp.closed)
