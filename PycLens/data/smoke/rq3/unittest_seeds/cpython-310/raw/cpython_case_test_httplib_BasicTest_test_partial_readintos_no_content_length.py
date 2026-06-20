# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_partial_readintos_no_content_length

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    body = 'HTTP/1.1 200 Ok\r\n\r\nText'
    sock = FakeSocket(body)
    resp = client.HTTPResponse(sock)
    resp.begin()
    b = bytearray(2)
    n = resp.readinto(b)
    self.assertEqual(n, 2)
    self.assertEqual(bytes(b), b'Te')
    self.assertFalse(resp.isclosed())
    n = resp.readinto(b)
    self.assertEqual(n, 2)
    self.assertEqual(bytes(b), b'xt')
    n = resp.readinto(b)
    self.assertEqual(n, 0)
    self.assertTrue(resp.isclosed())
