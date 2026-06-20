# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: TunnelTests_test_set_tunnel_host_port_headers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tunnel_host = 'destination.com'
    tunnel_port = 8888
    tunnel_headers = {'User-Agent': 'Mozilla/5.0 (compatible, MSIE 11)'}
    self.conn.set_tunnel(tunnel_host, port=tunnel_port, headers=tunnel_headers)
    self.conn.request('HEAD', '/', '')
    self.assertEqual(self.conn.sock.host, self.host)
    self.assertEqual(self.conn.sock.port, client.HTTP_PORT)
    self.assertEqual(self.conn._tunnel_host, tunnel_host)
    self.assertEqual(self.conn._tunnel_port, tunnel_port)
    self.assertEqual(self.conn._tunnel_headers, tunnel_headers)
