# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_makepasv_issue43285_security_enabled_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(self.client.trust_server_pasv_ipv4_address)
    (trusted_host, port) = self.client.makepasv()
    self.assertNotEqual(trusted_host, self.server.handler_instance.fake_pasv_server_ip)
    socket.create_connection((trusted_host, port), timeout=TIMEOUT).close()
