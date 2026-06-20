# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_makepasv_issue43285_security_disabled

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.client.trust_server_pasv_ipv4_address = True
    (bad_host, port) = self.client.makepasv()
    self.assertEqual(bad_host, self.server.handler_instance.fake_pasv_server_ip)
    socket.create_connection((self.client.sock.getpeername()[0], port), timeout=TIMEOUT).close()
