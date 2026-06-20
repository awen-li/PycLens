# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_partial_readintos_past_end

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    body = 'HTTP/1.1 200 Ok\r\nContent-Length: 4\r\n\r\nText'
    sock = FakeSocket(body)
    resp = client.HTTPResponse(sock)
    resp.begin()
    b = bytearray(10)
    n = resp.readinto(b)
    self.assertEqual(n, 4)
    self.assertEqual(bytes(b)[:4], b'Text')
    self.assertTrue(resp.isclosed())
    self.assertFalse(resp.closed)
    resp.close()
    self.assertTrue(resp.closed)
