# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestIPv6Environment_test_makepasv

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (host, port) = self.client.makepasv()
    conn = socket.create_connection((host, port), timeout=TIMEOUT)
    conn.close()
    self.assertEqual(self.server.handler_instance.last_received_cmd, 'epsv')
