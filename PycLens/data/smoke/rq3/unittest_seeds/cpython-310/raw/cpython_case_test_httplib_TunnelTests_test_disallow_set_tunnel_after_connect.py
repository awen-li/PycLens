# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: TunnelTests_test_disallow_set_tunnel_after_connect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.conn.connect()
    self.assertRaises(RuntimeError, self.conn.set_tunnel, 'destination.com')
