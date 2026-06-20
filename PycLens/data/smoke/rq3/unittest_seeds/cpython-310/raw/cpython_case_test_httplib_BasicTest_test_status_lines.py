# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_status_lines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    body = 'HTTP/1.1 200 Ok\r\n\r\nText'
    sock = FakeSocket(body)
    resp = client.HTTPResponse(sock)
    resp.begin()
    self.assertEqual(resp.read(0), b'')
    self.assertFalse(resp.isclosed())
    self.assertFalse(resp.closed)
    self.assertEqual(resp.read(), b'Text')
    self.assertTrue(resp.isclosed())
    self.assertFalse(resp.closed)
    resp.close()
    self.assertTrue(resp.closed)
    body = 'HTTP/1.1 400.100 Not Ok\r\n\r\nText'
    sock = FakeSocket(body)
    resp = client.HTTPResponse(sock)
    self.assertRaises(client.BadStatusLine, resp.begin)
