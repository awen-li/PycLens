# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: PersistenceTest_test_reuse_reconnect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = (('1.0', '', False), ('1.0', 'Connection: keep-alive\r\n', True), ('1.1', '', True), ('1.1', 'Connection: close\r\n', False), ('1.0', 'Connection: keep-ALIVE\r\n', True), ('1.1', 'Connection: cloSE\r\n', False))
    for (version, header, reuse) in tests:
        with self.subTest(version=version, header=header):
            msg = 'HTTP/{} 200 OK\r\n{}Content-Length: 12\r\n\r\nDummy body\r\n'.format(version, header)
            conn = FakeSocketHTTPConnection(msg)
            self.assertIsNone(conn.sock)
            conn.request('GET', '/open-connection')
            with conn.getresponse() as response:
                self.assertEqual(conn.sock is None, not reuse)
                response.read()
            self.assertEqual(conn.sock is None, not reuse)
            self.assertEqual(conn.connections, 1)
            conn.request('GET', '/subsequent-request')
            self.assertEqual(conn.connections, 1 if reuse else 2)
