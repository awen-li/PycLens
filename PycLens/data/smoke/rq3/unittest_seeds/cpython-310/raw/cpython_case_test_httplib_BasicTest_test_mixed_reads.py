# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_mixed_reads

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    body = 'HTTP/1.1 200 Ok\r\nContent-Length: 13\r\n\r\nText\r\nAnother'
    sock = FakeSocket(body)
    resp = client.HTTPResponse(sock)
    resp.begin()
    self.assertEqual(resp.readline(), b'Text\r\n')
    self.assertFalse(resp.isclosed())
    self.assertEqual(resp.read(), b'Another')
    self.assertTrue(resp.isclosed())
    self.assertFalse(resp.closed)
    resp.close()
    self.assertTrue(resp.closed)
