# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: PersistenceTest_test_100_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    conn = FakeSocketHTTPConnection(b'HTTP/1.1 100 Continue\r\n\r\n')
    conn.request('GET', '/', headers={'Expect': '100-continue'})
    self.assertRaises(client.RemoteDisconnected, conn.getresponse)
    self.assertIsNone(conn.sock)
    conn.request('GET', '/reconnect')
    self.assertEqual(conn.connections, 2)
