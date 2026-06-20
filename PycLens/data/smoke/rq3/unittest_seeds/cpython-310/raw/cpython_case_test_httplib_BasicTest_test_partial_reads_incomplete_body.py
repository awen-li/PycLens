# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_partial_reads_incomplete_body

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    body = 'HTTP/1.1 200 Ok\r\nContent-Length: 10\r\n\r\nText'
    sock = FakeSocket(body)
    resp = client.HTTPResponse(sock)
    resp.begin()
    self.assertEqual(resp.read(2), b'Te')
    self.assertFalse(resp.isclosed())
    self.assertEqual(resp.read(2), b'xt')
    self.assertEqual(resp.read(1), b'')
    self.assertTrue(resp.isclosed())
