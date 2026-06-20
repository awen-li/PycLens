# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: TunnelTests_test_connect_put_request

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.conn.set_tunnel('destination.com')
    self.conn.request('PUT', '/', '')
    self.assertEqual(self.conn.sock.host, self.host)
    self.assertEqual(self.conn.sock.port, client.HTTP_PORT)
    self.assertIn(b'CONNECT destination.com', self.conn.sock.data)
    self.assertIn(b'Host: destination.com', self.conn.sock.data)
